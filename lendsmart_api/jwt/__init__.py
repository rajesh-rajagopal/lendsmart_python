import hmac
import sys

from lendsmart_api.jwt import compat

if sys.version_info[0] == 3 and sys.version_info[1] == 2:
    # PyJWT expects hmac.compare_digest to exist even under python 3.2
    hmac.compare_digest = compat.compare_digest

import jwt as jwt_lib

try:
    import json
except ImportError:
    import simplejson as json

import time

if sys.version_info[0] == 3 and sys.version_info[1] == 2:
    # PyJWT expects hmac.compare_digest to exist even under python 3.2
    hmac.compare_digest = compat.compare_digest


__all__ = ['Jwt', 'JwtDecodeError']


class JwtDecodeError(Exception):
    pass


class Jwt(object):
    """Base class for building a Json Web Token"""
    GENERATE = object()

    def __init__(self, secret_key, issuer, service_account_name, subject=None,
                 algorithm='HS256', secret_name="lendsmart_lambda",
                 secret_id="1123653585066795008", user_account_id="1000", ttl=3600, valid_until=None):
        self.secret_key = secret_key
        """:type str: The secret used to encode the JWT"""
        self.issuer = issuer
        """:type str: The issuer of this JWT"""
        self.subject = subject
        """:type str: The subject of this JWT, ommited from payload by default"""
        self.algorithm = algorithm
        """:type str: The algorithm used to encode the JWT, defaults to 'HS256'"""
        self.service_account_name = service_account_name
        """:type str: Store service account name."""
        self.ttl = ttl
        """:type int: Time to live of the JWT in seconds, defaults to 1 hour"""
        self.valid_until = valid_until
        """:type int: Time in secs since epoch this JWT is valid for. Overrides ttl if provided."""
        self.secret_id = secret_id
        """:type str: Store an identification of secret"""
        self.secret_name = secret_name
        """:type str: Refer name of secret"""
        self.user_account_id = user_account_id
        """:type str: user account id"""

        self.__decoded_payload = None
        self.__decoded_headers = None

    def _generate_payload(self):
        """:rtype: dict the payload of the JWT to send"""
        raise NotImplementedError('Subclass must provide a payload.')

    def _generate_headers(self):
        """:rtype dict: Additional headers to include in the JWT, defaults to an empty dict"""
        return {}

    @classmethod
    def _from_jwt(cls, headers, payload, key=None):
        """
        Class specific implementation of from_jwt which should take jwt components and return
        and instance of this Class with jwt information loaded.
        :return: Jwt object containing the headers, payload and key
        """
        jwt = Jwt(
            secret_key=key,
            issuer=payload.get('iss', None),
            subject=payload.get('sub', None),
            algorithm=headers.get('alg', None),
            valid_until=payload.get('exp', None),
            service_account_name=payload.get('lendsmart_sh/serviceaccount/service-account.name', None),
            secret_id=payload.get('lendsmart_sh/useraccount/secret.uid', None),
            secret_name=payload.get('lendsmart_sh/useraccount/secret.name', None),
            user_account_id=payload.get('lendsmart_sh/serviceaccount/service-account.uid', None),
        )
        jwt.__decoded_payload = payload
        jwt.__decoded_headers = headers
        return jwt

    @property
    def payload(self):
        if self.__decoded_payload:
            return self.__decoded_payload

        payload = {}
        payload['iss'] = self.issuer
        payload['exp'] = str(time.time() + self.ttl)
        if self.service_account_name is not None:
            payload[self.subject] = self.service_account_name
        if self.valid_until:
            payload['exp'] = self.valid_until
        if self.subject:
            payload['sub'] = self.subject + "::" + self.service_account_name
        if self.secret_name:
            payload['lendsmart_sh/serviceaccount/secret.name'] = self.secret_name
        if self.secret_id:
            payload['lendsmart_sh/useraccount/secret.uid'] = self.secret_id
        if self.user_account_id:
            payload['lendsmart_sh/serviceaccount/service-account.uid'] = self.user_account_id

        return payload

    @property
    def headers(self):
        if self.__decoded_headers:
            return self.__decoded_headers

        headers = self._generate_headers().copy()
        headers['typ'] = 'JWT'
        headers['alg'] = self.algorithm
        return headers

    def to_jwt(self, algorithm=None, ttl=None):
        """
        Encode this JWT object into a JWT string
        :param str algorithm: override the algorithm used to encode the JWT
        :param int ttl: override the ttl configured in the constructor
        :rtype: str The JWT string
        """

        if not self.secret_key:
            raise ValueError('JWT does not have a signing key configured.')

        headers = self.headers.copy()
        if algorithm:
            headers['alg'] = algorithm
        algorithm = algorithm or self.algorithm

        payload = self.payload.copy()
        if ttl:
            payload['exp'] = str(time.time() + ttl )

        return jwt_lib.encode(payload, self.secret_key, algorithm=algorithm, headers=headers)

    @classmethod
    def from_jwt(cls, jwt, key=''):
        """
        Decode a JWT string into a Jwt object
        :param str jwt: JWT string
        :param Optional[str] key: key used to verify JWT signature, if not provided then validation
                                  is skipped.
        :raises JwtDecodeError if decoding JWT fails for any reason.
        :return: A DecodedJwt object containing the jwt information.
        """
        verify = True if key else False

        try:
            payload = jwt_lib.decode(bytes(jwt), key, options={
                'verify_signature': verify,
                'verify_exp': True,
                'verify_service_account': True,
            })
            headers = jwt_lib.get_unverified_header(jwt)
        except Exception as e:
            raise JwtDecodeError(getattr(e, 'message', str(e)))

        return cls._from_jwt(headers, payload, key)

    def __str__(self):
        return '<JWT {}>'.format(self.to_jwt())
