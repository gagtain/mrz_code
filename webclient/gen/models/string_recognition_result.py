# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""
Describes single row recognition results in multi-line text field of a document
"""
class StringRecognitionResult(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'string_result': 'list[SymbolRecognitionResult]'
    }

    attribute_map = {
        'string_result': 'StringResult'
    }

    def __init__(self, string_result=None, local_vars_configuration=None):  # noqa: E501
        """StringRecognitionResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._string_result = None
        self.discriminator = None

        self.string_result = string_result

    @property
    def string_result(self):
        """Gets the string_result of this StringRecognitionResult.  # noqa: E501

        Array of recognition results for individual characters of a string  # noqa: E501

        :return: The string_result of this StringRecognitionResult.  # noqa: E501
        :rtype: list[SymbolRecognitionResult]
        """
        return self._string_result

    @string_result.setter
    def string_result(self, string_result):
        """Sets the string_result of this StringRecognitionResult.

        Array of recognition results for individual characters of a string  # noqa: E501

        :param string_result: The string_result of this StringRecognitionResult.  # noqa: E501
        :type string_result: list[SymbolRecognitionResult]
        """
        if self.local_vars_configuration.client_side_validation and string_result is None:  # noqa: E501
            raise ValueError("Invalid value for `string_result`, must not be `None`")  # noqa: E501

        self._string_result = string_result

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
        if not isinstance(other, StringRecognitionResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StringRecognitionResult):
            return True

        return self.to_dict() != other.to_dict()
