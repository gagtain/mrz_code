# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class TextFieldValue(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'source': 'Source',
        'value': 'str',
        'original_value': 'str',
        'original_symbols': 'list[OriginalSymbol]',
        'page_index': 'int',
        'probability': 'int',
        'field_rect': 'RectangleCoordinates',
        'rfid_origin': 'RfidOrigin'
    }

    attribute_map = {
        'source': 'source',
        'value': 'value',
        'original_value': 'originalValue',
        'original_symbols': 'originalSymbols',
        'page_index': 'pageIndex',
        'probability': 'probability',
        'field_rect': 'fieldRect',
        'rfid_origin': 'rfidOrigin'
    }

    def __init__(self, source=None, value=None, original_value=None, original_symbols=None, page_index=None, probability=None, field_rect=None, rfid_origin=None, local_vars_configuration=None):  # noqa: E501
        """TextFieldValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._value = None
        self._original_value = None
        self._original_symbols = None
        self._page_index = None
        self._probability = None
        self._field_rect = None
        self._rfid_origin = None
        self.discriminator = None

        self.source = source
        self.value = value
        if original_value is not None:
            self.original_value = original_value
        if original_symbols is not None:
            self.original_symbols = original_symbols
        self.page_index = page_index
        if probability is not None:
            self.probability = probability
        if field_rect is not None:
            self.field_rect = field_rect
        if rfid_origin is not None:
            self.rfid_origin = rfid_origin

    @property
    def source(self):
        """Gets the source of this TextFieldValue.  # noqa: E501


        :return: The source of this TextFieldValue.  # noqa: E501
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TextFieldValue.


        :param source: The source of this TextFieldValue.  # noqa: E501
        :type source: Source
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def value(self):
        """Gets the value of this TextFieldValue.  # noqa: E501

        Parsed/processed value. Date format converted for output, delimiters removed  # noqa: E501

        :return: The value of this TextFieldValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TextFieldValue.

        Parsed/processed value. Date format converted for output, delimiters removed  # noqa: E501

        :param value: The value of this TextFieldValue.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def original_value(self):
        """Gets the original_value of this TextFieldValue.  # noqa: E501

        Original value as seen in the document  # noqa: E501

        :return: The original_value of this TextFieldValue.  # noqa: E501
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        """Sets the original_value of this TextFieldValue.

        Original value as seen in the document  # noqa: E501

        :param original_value: The original_value of this TextFieldValue.  # noqa: E501
        :type original_value: str
        """

        self._original_value = original_value

    @property
    def original_symbols(self):
        """Gets the original_symbols of this TextFieldValue.  # noqa: E501


        :return: The original_symbols of this TextFieldValue.  # noqa: E501
        :rtype: list[OriginalSymbol]
        """
        return self._original_symbols

    @original_symbols.setter
    def original_symbols(self, original_symbols):
        """Sets the original_symbols of this TextFieldValue.


        :param original_symbols: The original_symbols of this TextFieldValue.  # noqa: E501
        :type original_symbols: list[OriginalSymbol]
        """

        self._original_symbols = original_symbols

    @property
    def page_index(self):
        """Gets the page_index of this TextFieldValue.  # noqa: E501

        Page index of the image from input list  # noqa: E501

        :return: The page_index of this TextFieldValue.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this TextFieldValue.

        Page index of the image from input list  # noqa: E501

        :param page_index: The page_index of this TextFieldValue.  # noqa: E501
        :type page_index: int
        """
        if self.local_vars_configuration.client_side_validation and page_index is None:  # noqa: E501
            raise ValueError("Invalid value for `page_index`, must not be `None`")  # noqa: E501

        self._page_index = page_index

    @property
    def probability(self):
        """Gets the probability of this TextFieldValue.  # noqa: E501

        Min recognition probability. Combined minimum probability from single characters probabilities  # noqa: E501

        :return: The probability of this TextFieldValue.  # noqa: E501
        :rtype: int
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """Sets the probability of this TextFieldValue.

        Min recognition probability. Combined minimum probability from single characters probabilities  # noqa: E501

        :param probability: The probability of this TextFieldValue.  # noqa: E501
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
    def field_rect(self):
        """Gets the field_rect of this TextFieldValue.  # noqa: E501


        :return: The field_rect of this TextFieldValue.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._field_rect

    @field_rect.setter
    def field_rect(self, field_rect):
        """Sets the field_rect of this TextFieldValue.


        :param field_rect: The field_rect of this TextFieldValue.  # noqa: E501
        :type field_rect: RectangleCoordinates
        """

        self._field_rect = field_rect

    @property
    def rfid_origin(self):
        """Gets the rfid_origin of this TextFieldValue.  # noqa: E501


        :return: The rfid_origin of this TextFieldValue.  # noqa: E501
        :rtype: RfidOrigin
        """
        return self._rfid_origin

    @rfid_origin.setter
    def rfid_origin(self, rfid_origin):
        """Sets the rfid_origin of this TextFieldValue.


        :param rfid_origin: The rfid_origin of this TextFieldValue.  # noqa: E501
        :type rfid_origin: RfidOrigin
        """

        self._rfid_origin = rfid_origin

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
        if not isinstance(other, TextFieldValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextFieldValue):
            return True

        return self.to_dict() != other.to_dict()
