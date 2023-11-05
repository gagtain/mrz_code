# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class OriginalSymbol(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'code': 'int',
        'probability': 'int',
        'rect': 'RectangleCoordinates'
    }

    attribute_map = {
        'code': 'code',
        'probability': 'probability',
        'rect': 'rect'
    }

    def __init__(self, code=None, probability=None, rect=None, local_vars_configuration=None):  # noqa: E501
        """OriginalSymbol - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._probability = None
        self._rect = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if probability is not None:
            self.probability = probability
        if rect is not None:
            self.rect = rect

    @property
    def code(self):
        """Gets the code of this OriginalSymbol.  # noqa: E501

        Unicode symbol code  # noqa: E501

        :return: The code of this OriginalSymbol.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OriginalSymbol.

        Unicode symbol code  # noqa: E501

        :param code: The code of this OriginalSymbol.  # noqa: E501
        :type code: int
        """

        self._code = code

    @property
    def probability(self):
        """Gets the probability of this OriginalSymbol.  # noqa: E501

        Probability of correctness reading of a single character  # noqa: E501

        :return: The probability of this OriginalSymbol.  # noqa: E501
        :rtype: int
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """Sets the probability of this OriginalSymbol.

        Probability of correctness reading of a single character  # noqa: E501

        :param probability: The probability of this OriginalSymbol.  # noqa: E501
        :type probability: int
        """
        if (self.local_vars_configuration.client_side_validation and
                probability is not None and probability > 100):  # noqa: E501
            raise ValueError("Invalid value for `probability`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                probability is not None and probability < 0):  # noqa: E501
            raise ValueError("Invalid value for `probability`, must be a value greater than or equal to `0`")  # noqa: E501

        self._probability = probability

    @property
    def rect(self):
        """Gets the rect of this OriginalSymbol.  # noqa: E501


        :return: The rect of this OriginalSymbol.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._rect

    @rect.setter
    def rect(self, rect):
        """Sets the rect of this OriginalSymbol.


        :param rect: The rect of this OriginalSymbol.  # noqa: E501
        :type rect: RectangleCoordinates
        """

        self._rect = rect

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
        if not isinstance(other, OriginalSymbol):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OriginalSymbol):
            return True

        return self.to_dict() != other.to_dict()
