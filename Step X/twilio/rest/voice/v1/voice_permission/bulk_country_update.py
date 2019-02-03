# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class BulkCountryUpdateList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the BulkCountryUpdateList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdateList
        :rtype: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdateList
        """
        super(BulkCountryUpdateList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/DialingPermissions/BulkCountryUpdates'.format(**self._solution)

    def create(self, update_request):
        """
        Create a new BulkCountryUpdateInstance

        :param unicode update_request: URL encoded JSON array of update objects

        :returns: Newly created BulkCountryUpdateInstance
        :rtype: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdateInstance
        """
        data = values.of({'UpdateRequest': update_request, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return BulkCountryUpdateInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.BulkCountryUpdateList>'


class BulkCountryUpdatePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the BulkCountryUpdatePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdatePage
        :rtype: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdatePage
        """
        super(BulkCountryUpdatePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BulkCountryUpdateInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdateInstance
        :rtype: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdateInstance
        """
        return BulkCountryUpdateInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.BulkCountryUpdatePage>'


class BulkCountryUpdateInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the BulkCountryUpdateInstance

        :returns: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdateInstance
        :rtype: twilio.rest.voice.v1.voice_permission.bulk_country_update.BulkCountryUpdateInstance
        """
        super(BulkCountryUpdateInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'update_count': deserialize.integer(payload['update_count']),
            'update_request': payload['update_request'],
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def update_count(self):
        """
        :returns: The number of countries updated
        :rtype: unicode
        """
        return self._properties['update_count']

    @property
    def update_request(self):
        """
        :returns: A URL encoded JSON array of update objects
        :rtype: unicode
        """
        return self._properties['update_request']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.BulkCountryUpdateInstance>'
