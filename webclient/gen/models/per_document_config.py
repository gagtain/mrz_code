# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class PerDocumentConfig(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'doc_id': 'list[int]',
        'exclude_auth_checks': 'int'
    }

    attribute_map = {
        'doc_id': 'docID',
        'exclude_auth_checks': 'excludeAuthChecks'
    }

    def __init__(self, doc_id=None, exclude_auth_checks=None, local_vars_configuration=None):  # noqa: E501
        """PerDocumentConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._doc_id = None
        self._exclude_auth_checks = None
        self.discriminator = None

        if doc_id is not None:
            self.doc_id = doc_id
        if exclude_auth_checks is not None:
            self.exclude_auth_checks = exclude_auth_checks

    @property
    def doc_id(self):
        """Gets the doc_id of this PerDocumentConfig.  # noqa: E501

        Specific template IDs, for which apply current custom configuration  # noqa: E501

        :return: The doc_id of this PerDocumentConfig.  # noqa: E501
        :rtype: list[int]
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """Sets the doc_id of this PerDocumentConfig.

        Specific template IDs, for which apply current custom configuration  # noqa: E501

        :param doc_id: The doc_id of this PerDocumentConfig.  # noqa: E501
        :type doc_id: list[int]
        """

        self._doc_id = doc_id

    @property
    def exclude_auth_checks(self):
        """Gets the exclude_auth_checks of this PerDocumentConfig.  # noqa: E501

        Contains items from AuthenticityResultType as sum via OR operation  # noqa: E501

        :return: The exclude_auth_checks of this PerDocumentConfig.  # noqa: E501
        :rtype: int
        """
        return self._exclude_auth_checks

    @exclude_auth_checks.setter
    def exclude_auth_checks(self, exclude_auth_checks):
        """Sets the exclude_auth_checks of this PerDocumentConfig.

        Contains items from AuthenticityResultType as sum via OR operation  # noqa: E501

        :param exclude_auth_checks: The exclude_auth_checks of this PerDocumentConfig.  # noqa: E501
        :type exclude_auth_checks: int
        """

        self._exclude_auth_checks = exclude_auth_checks

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PerDocumentConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerDocumentConfig):
            return True

        return self.to_dict() != other.to_dict()
