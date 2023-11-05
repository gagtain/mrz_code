# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""
Describes an individual character recognition candidate
"""
class SymbolCandidate(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'symbol_code': 'int',
        'symbol_probability': 'int'
    }

    attribute_map = {
        'symbol_code': 'SymbolCode',
        'symbol_probability': 'SymbolProbability'
    }

    def __init__(self, symbol_code=None, symbol_probability=None, local_vars_configuration=None):  # noqa: E501
        """SymbolCandidate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol_code = None
        self._symbol_probability = None
        self.discriminator = None

        self.symbol_code = symbol_code
        self.symbol_probability = symbol_probability

    @property
    def symbol_code(self):
        """Gets the symbol_code of this SymbolCandidate.  # noqa: E501

        Unicode symbol code  # noqa: E501

        :return: The symbol_code of this SymbolCandidate.  # noqa: E501
        :rtype: int
        """
        return self._symbol_code

    @symbol_code.setter
    def symbol_code(self, symbol_code):
        """Sets the symbol_code of this SymbolCandidate.

        Unicode symbol code  # noqa: E501

        :param symbol_code: The symbol_code of this SymbolCandidate.  # noqa: E501
        :type symbol_code: int
        """
        if self.local_vars_configuration.client_side_validation and symbol_code is None:  # noqa: E501
            raise ValueError("Invalid value for `symbol_code`, must not be `None`")  # noqa: E501

        self._symbol_code = symbol_code

    @property
    def symbol_probability(self):
        """Gets the symbol_probability of this SymbolCandidate.  # noqa: E501

        character recognition probability (0–100,%)  # noqa: E501

        :return: The symbol_probability of this SymbolCandidate.  # noqa: E501
        :rtype: int
        """
        return self._symbol_probability

    @symbol_probability.setter
    def symbol_probability(self, symbol_probability):
        """Sets the symbol_probability of this SymbolCandidate.

        character recognition probability (0–100,%)  # noqa: E501

        :param symbol_probability: The symbol_probability of this SymbolCandidate.  # noqa: E501
        :type symbol_probability: int
        """
        if self.local_vars_configuration.client_side_validation and symbol_probability is None:  # noqa: E501
            raise ValueError("Invalid value for `symbol_probability`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                symbol_probability is not None and symbol_probability > 100):  # noqa: E501
            raise ValueError("Invalid value for `symbol_probability`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                symbol_probability is not None and symbol_probability < 0):  # noqa: E501
            raise ValueError("Invalid value for `symbol_probability`, must be a value greater than or equal to `0`")  # noqa: E501

        self._symbol_probability = symbol_probability

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
        if not isinstance(other, SymbolCandidate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SymbolCandidate):
            return True

        return self.to_dict() != other.to_dict()
