# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class AuthenticityResultAllOf(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'authenticity_check_list': 'AuthenticityCheckList'
    }

    attribute_map = {
        'authenticity_check_list': 'AuthenticityCheckList'
    }

    def __init__(self, authenticity_check_list=None, local_vars_configuration=None):  # noqa: E501
        """AuthenticityResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authenticity_check_list = None
        self.discriminator = None

        self.authenticity_check_list = authenticity_check_list

    @property
    def authenticity_check_list(self):
        """Gets the authenticity_check_list of this AuthenticityResultAllOf.  # noqa: E501


        :return: The authenticity_check_list of this AuthenticityResultAllOf.  # noqa: E501
        :rtype: AuthenticityCheckList
        """
        return self._authenticity_check_list

    @authenticity_check_list.setter
    def authenticity_check_list(self, authenticity_check_list):
        """Sets the authenticity_check_list of this AuthenticityResultAllOf.


        :param authenticity_check_list: The authenticity_check_list of this AuthenticityResultAllOf.  # noqa: E501
        :type authenticity_check_list: AuthenticityCheckList
        """
        if self.local_vars_configuration.client_side_validation and authenticity_check_list is None:  # noqa: E501
            raise ValueError("Invalid value for `authenticity_check_list`, must not be `None`")  # noqa: E501

        self._authenticity_check_list = authenticity_check_list

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
        if not isinstance(other, AuthenticityResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticityResultAllOf):
            return True

        return self.to_dict() != other.to_dict()
