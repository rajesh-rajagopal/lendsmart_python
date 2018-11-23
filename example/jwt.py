from lendsmart_api.jwt import Jwt


ISSUER = 'rioos_sh/serviceaccount'
SUBJECT = 'rioos_sh/serviceaccount/service-account.name'
SECRET_KEY = """copy paste the private key generated for the service account
dfasdfasdf
adfasdfasfsdfas
sfaa sfdafsdf
"""
jwt = Jwt(SECRET_KEY, ISSUER, SUBJECT)

print jwt.to_jwt()
