# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from lendsmart.base.domain import Domain
from lendsmart.rest.document.v2 import V2


class Document(Domain):

    def __init__(self, lendsmart):
        """
        Initialize the Document Domain

        :returns: Domain for Document
        :rtype: lendsmart.rest.document.Document
        """
        super(Document, self).__init__(lendsmart)

        self.base_url = 'https://api.lendsmart.ai'

        # Versions
        self._v2 = None

    @property
    def v2(self):
        """
        :returns: Version v2 of document
        :rtype: lendsmart.rest.document.v2.V2
        """
        if self._v2 is None:
            self._v2 = V2(self)
        return self._v2

    @property
    def artifact(self):
        """
        :rtype: lendsmart.rest.document.v2.ArtifactList
        """
        return self.v2.artifact

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<LendSmart.Document>'