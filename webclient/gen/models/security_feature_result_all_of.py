# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class SecurityFeatureResultAllOf(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'element_type': 'SecurityFeatureType',
        'element_rect': 'RectangleCoordinates',
        'visibility': 'Visibility',
        'critical_flag': 'Critical',
        'area_list': 'AreaContainer',
        'reserved2': 'int'
    }

    attribute_map = {
        'element_type': 'ElementType',
        'element_rect': 'ElementRect',
        'visibility': 'Visibility',
        'critical_flag': 'CriticalFlag',
        'area_list': 'AreaList',
        'reserved2': 'Reserved2'
    }

    def __init__(self, element_type=None, element_rect=None, visibility=None, critical_flag=None, area_list=None, reserved2=None, local_vars_configuration=None):  # noqa: E501
        """SecurityFeatureResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._element_type = None
        self._element_rect = None
        self._visibility = None
        self._critical_flag = None
        self._area_list = None
        self._reserved2 = None
        self.discriminator = None

        if element_type is not None:
            self.element_type = element_type
        if element_rect is not None:
            self.element_rect = element_rect
        if visibility is not None:
            self.visibility = visibility
        if critical_flag is not None:
            self.critical_flag = critical_flag
        if area_list is not None:
            self.area_list = area_list
        if reserved2 is not None:
            self.reserved2 = reserved2

    @property
    def element_type(self):
        """Gets the element_type of this SecurityFeatureResultAllOf.  # noqa: E501


        :return: The element_type of this SecurityFeatureResultAllOf.  # noqa: E501
        :rtype: SecurityFeatureType
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this SecurityFeatureResultAllOf.


        :param element_type: The element_type of this SecurityFeatureResultAllOf.  # noqa: E501
        :type element_type: SecurityFeatureType
        """

        self._element_type = element_type

    @property
    def element_rect(self):
        """Gets the element_rect of this SecurityFeatureResultAllOf.  # noqa: E501


        :return: The element_rect of this SecurityFeatureResultAllOf.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._element_rect

    @element_rect.setter
    def element_rect(self, element_rect):
        """Sets the element_rect of this SecurityFeatureResultAllOf.


        :param element_rect: The element_rect of this SecurityFeatureResultAllOf.  # noqa: E501
        :type element_rect: RectangleCoordinates
        """

        self._element_rect = element_rect

    @property
    def visibility(self):
        """Gets the visibility of this SecurityFeatureResultAllOf.  # noqa: E501


        :return: The visibility of this SecurityFeatureResultAllOf.  # noqa: E501
        :rtype: Visibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this SecurityFeatureResultAllOf.


        :param visibility: The visibility of this SecurityFeatureResultAllOf.  # noqa: E501
        :type visibility: Visibility
        """

        self._visibility = visibility

    @property
    def critical_flag(self):
        """Gets the critical_flag of this SecurityFeatureResultAllOf.  # noqa: E501


        :return: The critical_flag of this SecurityFeatureResultAllOf.  # noqa: E501
        :rtype: Critical
        """
        return self._critical_flag

    @critical_flag.setter
    def critical_flag(self, critical_flag):
        """Sets the critical_flag of this SecurityFeatureResultAllOf.


        :param critical_flag: The critical_flag of this SecurityFeatureResultAllOf.  # noqa: E501
        :type critical_flag: Critical
        """

        self._critical_flag = critical_flag

    @property
    def area_list(self):
        """Gets the area_list of this SecurityFeatureResultAllOf.  # noqa: E501


        :return: The area_list of this SecurityFeatureResultAllOf.  # noqa: E501
        :rtype: AreaContainer
        """
        return self._area_list

    @area_list.setter
    def area_list(self, area_list):
        """Sets the area_list of this SecurityFeatureResultAllOf.


        :param area_list: The area_list of this SecurityFeatureResultAllOf.  # noqa: E501
        :type area_list: AreaContainer
        """

        self._area_list = area_list

    @property
    def reserved2(self):
        """Gets the reserved2 of this SecurityFeatureResultAllOf.  # noqa: E501


        :return: The reserved2 of this SecurityFeatureResultAllOf.  # noqa: E501
        :rtype: int
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """Sets the reserved2 of this SecurityFeatureResultAllOf.


        :param reserved2: The reserved2 of this SecurityFeatureResultAllOf.  # noqa: E501
        :type reserved2: int
        """

        self._reserved2 = reserved2

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
        if not isinstance(other, SecurityFeatureResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityFeatureResultAllOf):
            return True

        return self.to_dict() != other.to_dict()
