# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class ImagesFieldValue(object):
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
        'original_page_index': 'int',
        'page_index': 'int',
        'light_index': 'Light',
        'container_type': 'int',
        'field_rect': 'RectangleCoordinates',
        'rfid_origin': 'RfidOrigin'
    }

    attribute_map = {
        'source': 'source',
        'value': 'value',
        'original_value': 'originalValue',
        'original_page_index': 'originalPageIndex',
        'page_index': 'pageIndex',
        'light_index': 'lightIndex',
        'container_type': 'containerType',
        'field_rect': 'fieldRect',
        'rfid_origin': 'rfidOrigin'
    }

    def __init__(self, source=None, value=None, original_value=None, original_page_index=None, page_index=None, light_index=None, container_type=0, field_rect=None, rfid_origin=None, local_vars_configuration=None):  # noqa: E501
        """ImagesFieldValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._value = None
        self._original_value = None
        self._original_page_index = None
        self._page_index = None
        self._light_index = None
        self._container_type = None
        self._field_rect = None
        self._rfid_origin = None
        self.discriminator = None

        self.source = source
        self.value = value
        if original_value is not None:
            self.original_value = original_value
        if original_page_index is not None:
            self.original_page_index = original_page_index
        self.page_index = page_index
        self.light_index = light_index
        self.container_type = container_type
        if field_rect is not None:
            self.field_rect = field_rect
        if rfid_origin is not None:
            self.rfid_origin = rfid_origin

    @property
    def source(self):
        """Gets the source of this ImagesFieldValue.  # noqa: E501


        :return: The source of this ImagesFieldValue.  # noqa: E501
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ImagesFieldValue.


        :param source: The source of this ImagesFieldValue.  # noqa: E501
        :type source: Source
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def value(self):
        """Gets the value of this ImagesFieldValue.  # noqa: E501

        Base64 encoded image  # noqa: E501

        :return: The value of this ImagesFieldValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ImagesFieldValue.

        Base64 encoded image  # noqa: E501

        :param value: The value of this ImagesFieldValue.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def original_value(self):
        """Gets the original_value of this ImagesFieldValue.  # noqa: E501

        Base64 encoded image  # noqa: E501

        :return: The original_value of this ImagesFieldValue.  # noqa: E501
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        """Sets the original_value of this ImagesFieldValue.

        Base64 encoded image  # noqa: E501

        :param original_value: The original_value of this ImagesFieldValue.  # noqa: E501
        :type original_value: str
        """

        self._original_value = original_value

    @property
    def original_page_index(self):
        """Gets the original_page_index of this ImagesFieldValue.  # noqa: E501

        Original page index  # noqa: E501

        :return: The original_page_index of this ImagesFieldValue.  # noqa: E501
        :rtype: int
        """
        return self._original_page_index

    @original_page_index.setter
    def original_page_index(self, original_page_index):
        """Sets the original_page_index of this ImagesFieldValue.

        Original page index  # noqa: E501

        :param original_page_index: The original_page_index of this ImagesFieldValue.  # noqa: E501
        :type original_page_index: int
        """

        self._original_page_index = original_page_index

    @property
    def page_index(self):
        """Gets the page_index of this ImagesFieldValue.  # noqa: E501

        Page index of the image from input list  # noqa: E501

        :return: The page_index of this ImagesFieldValue.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ImagesFieldValue.

        Page index of the image from input list  # noqa: E501

        :param page_index: The page_index of this ImagesFieldValue.  # noqa: E501
        :type page_index: int
        """
        if self.local_vars_configuration.client_side_validation and page_index is None:  # noqa: E501
            raise ValueError("Invalid value for `page_index`, must not be `None`")  # noqa: E501

        self._page_index = page_index

    @property
    def light_index(self):
        """Gets the light_index of this ImagesFieldValue.  # noqa: E501


        :return: The light_index of this ImagesFieldValue.  # noqa: E501
        :rtype: Light
        """
        return self._light_index

    @light_index.setter
    def light_index(self, light_index):
        """Sets the light_index of this ImagesFieldValue.


        :param light_index: The light_index of this ImagesFieldValue.  # noqa: E501
        :type light_index: Light
        """
        if self.local_vars_configuration.client_side_validation and light_index is None:  # noqa: E501
            raise ValueError("Invalid value for `light_index`, must not be `None`")  # noqa: E501

        self._light_index = light_index

    @property
    def container_type(self):
        """Gets the container_type of this ImagesFieldValue.  # noqa: E501

        Same as Result type, but used for safe parsing of not-described values. See Result type.  # noqa: E501

        :return: The container_type of this ImagesFieldValue.  # noqa: E501
        :rtype: int
        """
        return self._container_type

    @container_type.setter
    def container_type(self, container_type):
        """Sets the container_type of this ImagesFieldValue.

        Same as Result type, but used for safe parsing of not-described values. See Result type.  # noqa: E501

        :param container_type: The container_type of this ImagesFieldValue.  # noqa: E501
        :type container_type: int
        """
        if self.local_vars_configuration.client_side_validation and container_type is None:  # noqa: E501
            raise ValueError("Invalid value for `container_type`, must not be `None`")  # noqa: E501

        self._container_type = container_type

    @property
    def field_rect(self):
        """Gets the field_rect of this ImagesFieldValue.  # noqa: E501


        :return: The field_rect of this ImagesFieldValue.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._field_rect

    @field_rect.setter
    def field_rect(self, field_rect):
        """Sets the field_rect of this ImagesFieldValue.


        :param field_rect: The field_rect of this ImagesFieldValue.  # noqa: E501
        :type field_rect: RectangleCoordinates
        """

        self._field_rect = field_rect

    @property
    def rfid_origin(self):
        """Gets the rfid_origin of this ImagesFieldValue.  # noqa: E501


        :return: The rfid_origin of this ImagesFieldValue.  # noqa: E501
        :rtype: RfidOrigin
        """
        return self._rfid_origin

    @rfid_origin.setter
    def rfid_origin(self, rfid_origin):
        """Sets the rfid_origin of this ImagesFieldValue.


        :param rfid_origin: The rfid_origin of this ImagesFieldValue.  # noqa: E501
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
        if not isinstance(other, ImagesFieldValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImagesFieldValue):
            return True

        return self.to_dict() != other.to_dict()
