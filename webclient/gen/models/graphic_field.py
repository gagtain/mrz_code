# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class GraphicField(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'field_type': 'GraphicFieldType',
        'image': 'ImageData',
        'field_rect': 'RectangleCoordinates',
        'rfid_origin_dg': 'int',
        'rfid_origin_dg_tag': 'int',
        'rfid_origin_tag_entry': 'int',
        'rfid_origin_entry_view': 'int'
    }

    attribute_map = {
        'field_type': 'FieldType',
        'image': 'image',
        'field_rect': 'FieldRect',
        'rfid_origin_dg': 'RFID_OriginDG',
        'rfid_origin_dg_tag': 'RFID_OriginDGTag',
        'rfid_origin_tag_entry': 'RFID_OriginTagEntry',
        'rfid_origin_entry_view': 'RFID_OriginEntryView'
    }

    def __init__(self, field_type=None, image=None, field_rect=None, rfid_origin_dg=None, rfid_origin_dg_tag=None, rfid_origin_tag_entry=None, rfid_origin_entry_view=None, local_vars_configuration=None):  # noqa: E501
        """GraphicField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_type = None
        self._image = None
        self._field_rect = None
        self._rfid_origin_dg = None
        self._rfid_origin_dg_tag = None
        self._rfid_origin_tag_entry = None
        self._rfid_origin_entry_view = None
        self.discriminator = None

        self.field_type = field_type
        self.image = image
        if field_rect is not None:
            self.field_rect = field_rect
        if rfid_origin_dg is not None:
            self.rfid_origin_dg = rfid_origin_dg
        if rfid_origin_dg_tag is not None:
            self.rfid_origin_dg_tag = rfid_origin_dg_tag
        if rfid_origin_tag_entry is not None:
            self.rfid_origin_tag_entry = rfid_origin_tag_entry
        if rfid_origin_entry_view is not None:
            self.rfid_origin_entry_view = rfid_origin_entry_view

    @property
    def field_type(self):
        """Gets the field_type of this GraphicField.  # noqa: E501


        :return: The field_type of this GraphicField.  # noqa: E501
        :rtype: GraphicFieldType
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this GraphicField.


        :param field_type: The field_type of this GraphicField.  # noqa: E501
        :type field_type: GraphicFieldType
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501

        self._field_type = field_type

    @property
    def image(self):
        """Gets the image of this GraphicField.  # noqa: E501


        :return: The image of this GraphicField.  # noqa: E501
        :rtype: ImageData
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this GraphicField.


        :param image: The image of this GraphicField.  # noqa: E501
        :type image: ImageData
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def field_rect(self):
        """Gets the field_rect of this GraphicField.  # noqa: E501


        :return: The field_rect of this GraphicField.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._field_rect

    @field_rect.setter
    def field_rect(self, field_rect):
        """Sets the field_rect of this GraphicField.


        :param field_rect: The field_rect of this GraphicField.  # noqa: E501
        :type field_rect: RectangleCoordinates
        """

        self._field_rect = field_rect

    @property
    def rfid_origin_dg(self):
        """Gets the rfid_origin_dg of this GraphicField.  # noqa: E501

        Source data group file. Only for Result.RFID_GRAPHICS result.  # noqa: E501

        :return: The rfid_origin_dg of this GraphicField.  # noqa: E501
        :rtype: int
        """
        return self._rfid_origin_dg

    @rfid_origin_dg.setter
    def rfid_origin_dg(self, rfid_origin_dg):
        """Sets the rfid_origin_dg of this GraphicField.

        Source data group file. Only for Result.RFID_GRAPHICS result.  # noqa: E501

        :param rfid_origin_dg: The rfid_origin_dg of this GraphicField.  # noqa: E501
        :type rfid_origin_dg: int
        """

        self._rfid_origin_dg = rfid_origin_dg

    @property
    def rfid_origin_dg_tag(self):
        """Gets the rfid_origin_dg_tag of this GraphicField.  # noqa: E501

        Index of the source record of the image with biometric information in the information data group. Only for Result.RFID_GRAPHICS result.  # noqa: E501

        :return: The rfid_origin_dg_tag of this GraphicField.  # noqa: E501
        :rtype: int
        """
        return self._rfid_origin_dg_tag

    @rfid_origin_dg_tag.setter
    def rfid_origin_dg_tag(self, rfid_origin_dg_tag):
        """Sets the rfid_origin_dg_tag of this GraphicField.

        Index of the source record of the image with biometric information in the information data group. Only for Result.RFID_GRAPHICS result.  # noqa: E501

        :param rfid_origin_dg_tag: The rfid_origin_dg_tag of this GraphicField.  # noqa: E501
        :type rfid_origin_dg_tag: int
        """

        self._rfid_origin_dg_tag = rfid_origin_dg_tag

    @property
    def rfid_origin_tag_entry(self):
        """Gets the rfid_origin_tag_entry of this GraphicField.  # noqa: E501

        Index of the template in the record with biometric data. Only for Result.RFID_GRAPHICS result.  # noqa: E501

        :return: The rfid_origin_tag_entry of this GraphicField.  # noqa: E501
        :rtype: int
        """
        return self._rfid_origin_tag_entry

    @rfid_origin_tag_entry.setter
    def rfid_origin_tag_entry(self, rfid_origin_tag_entry):
        """Sets the rfid_origin_tag_entry of this GraphicField.

        Index of the template in the record with biometric data. Only for Result.RFID_GRAPHICS result.  # noqa: E501

        :param rfid_origin_tag_entry: The rfid_origin_tag_entry of this GraphicField.  # noqa: E501
        :type rfid_origin_tag_entry: int
        """

        self._rfid_origin_tag_entry = rfid_origin_tag_entry

    @property
    def rfid_origin_entry_view(self):
        """Gets the rfid_origin_entry_view of this GraphicField.  # noqa: E501

        Index of the variant of the biometric data template. Only for Result.RFID_GRAPHICS result.  # noqa: E501

        :return: The rfid_origin_entry_view of this GraphicField.  # noqa: E501
        :rtype: int
        """
        return self._rfid_origin_entry_view

    @rfid_origin_entry_view.setter
    def rfid_origin_entry_view(self, rfid_origin_entry_view):
        """Sets the rfid_origin_entry_view of this GraphicField.

        Index of the variant of the biometric data template. Only for Result.RFID_GRAPHICS result.  # noqa: E501

        :param rfid_origin_entry_view: The rfid_origin_entry_view of this GraphicField.  # noqa: E501
        :type rfid_origin_entry_view: int
        """

        self._rfid_origin_entry_view = rfid_origin_entry_view

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
        if not isinstance(other, GraphicField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GraphicField):
            return True

        return self.to_dict() != other.to_dict()
