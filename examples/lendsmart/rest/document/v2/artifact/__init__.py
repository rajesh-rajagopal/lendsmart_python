# coding=utf-8

from lendsmart.base import deserialize
from lendsmart.base import values
from lendsmart.base.instance_context import InstanceContext
from lendsmart.base.instance_resource import InstanceResource
from lendsmart.base.list_resource import ListResource
from lendsmart.base.page import Page


class ArtifactList(ListResource):
    """  """

    def __init__(self, version, service_sid):
        """
        Initialize the ArtifactList

        :param Version version: Version that contains the resource
        :param service_sid: The unique id of the Service this user belongs to.

        :returns: lendsmart.rest.document.v2.artifact.ArtifactList
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactList
        """
        super(ArtifactList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Users'.format(**self._solution)

    def create(self, identity, role_sid=values.unset, attributes=values.unset,
               friendly_name=values.unset):
        """
        Create a new ArtifactInstance

        :param unicode identity: A unique string that identifies the user within this service - often a username or email address.
        :param unicode role_sid: The unique id of the Role assigned to this user.
        :param unicode attributes: An optional string used to contain any metadata or other information for the User.
        :param unicode friendly_name: An optional human readable string representing the user.

        :returns: Newly created ArtifactInstance
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactInstance
        """
        data = values.of({
            'Identity': identity,
            'RoleSid': role_sid,
            'Attributes': attributes,
            'FriendlyName': friendly_name,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ArtifactInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def list(self, limit=None, page_size=None):
        """
        Lists ArtifactInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[lendsmart.rest.document.v2.artifact.ArtifactInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def get(self, sid):
        """
        Constructs a ArtifactContext

        :param sid: Key that uniquely defines the user to fetch.

        :returns: lendsmart.rest.document.v2.artifact.ArtifactContext
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactContext
        """
        return ArtifactContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ArtifactContext

        :param sid: Key that uniquely defines the user to fetch.

        :returns: lendsmart.rest.document.v2.artifact.ArtifactContext
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactContext
        """
        return ArtifactContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Lendsmart.Document.V2.ArtifactList>'


class ArtifactContext(InstanceContext):
    """  """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the ArtifactContext

        :param Version version: Version that contains the resource
        :param service_sid: Sid of the Service this user belongs to.
        :param sid: Key that uniquely defines the user to fetch.

        :returns: lendsmart.rest.document.v2.artifact.ArtifactContext
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactContext
        """
        super(ArtifactContext, self).__init__(version)

        # Path Solution
        self._uri = '/documents/{document_sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ArtifactInstance

        :returns: Fetched ArtifactInstance
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ArtifactInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Lendsmart.Document.V2.ArtifactContext {}>'.format(context)


class ArtifactInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the ArtifactInstance

        :returns: lendsmart.rest.document.v2.artifact.ArtifactInstance
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactInstance
        """
        super(ArtifactInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'attributes': payload['attributes'],
            'friendly_name': payload['friendly_name'],
            'role_sid': payload['role_sid'],
            'identity': payload['identity'],
            'is_online': payload['is_online'],
            'is_notifiable': payload['is_notifiable'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'joined_channels_count': deserialize.integer(payload['joined_channels_count']),
            'links': payload['links'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ArtifactContext for this ArtifactInstance
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactContext
        """
        if self._context is None:
            self._context = ArtifactContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account responsible for this user.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The unique id of the Service this user belongs to.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def attributes(self):
        """
        :returns: An optional string metadata field you can use to store any data you wish.
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def friendly_name(self):
        """
        :returns: The human-readable name of this user.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def role_sid(self):
        """
        :returns: The unique id of the [Role][role] assigned to this user.
        :rtype: unicode
        """
        return self._properties['role_sid']

    @property
    def identity(self):
        """
        :returns: A unique string that identifies the user within this service - often a username or email address.
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def is_online(self):
        """
        :returns: Indicates whether the User is actively connected to the Service instance and online.
        :rtype: bool
        """
        return self._properties['is_online']

    @property
    def is_notifiable(self):
        """
        :returns: Indicates whether the User has a potentially valid Push Notification registration  for the Service instance.
        :rtype: bool
        """
        return self._properties['is_notifiable']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def joined_channels_count(self):
        """
        :returns: The number of Channels this User is a Member of.
        :rtype: unicode
        """
        return self._properties['joined_channels_count']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def url(self):
        """
        :returns: An absolute URL for this user.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a ArtifactInstance

        :returns: Fetched ArtifactInstance
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Lendsmart.Document.V2.ArtifactInstance {}>'.format(context)
