# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class SecurityFeatureResult(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'int',
        'element_result': 'CheckResult',
        'element_diagnose': 'CheckDiagnose',
        'element_type': 'SecurityFeatureType',
        'element_rect': 'RectangleCoordinates',
        'visibility': 'Visibility',
        'critical_flag': 'Critical',
        'area_list': 'AreaContainer',
        'reserved2': 'int'
    }

    attribute_map = {
        'type': 'Type',
        'element_result': 'ElementResult',
        'element_diagnose': 'ElementDiagnose',
        'element_type': 'ElementType',
        'element_rect': 'ElementRect',
        'visibility': 'Visibility',
        'critical_flag': 'CriticalFlag',
        'area_list': 'AreaList',
        'reserved2': 'Reserved2'
    }

    def __init__(self, type=0, element_result=None, element_diagnose=None, element_type=None, element_rect=None, visibility=None, critical_flag=None, area_list=None, reserved2=None, local_vars_configuration=None):  # noqa: E501
        """SecurityFeatureResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._element_result = None
        self._element_diagnose = None
        self._element_type = None
        self._element_rect = None
        self._visibility = None
        self._critical_flag = None
        self._area_list = None
        self._reserved2 = None
        self.discriminator = None

        self.type = type
        if element_result is not None:
            self.element_result = element_result
        if element_diagnose is not None:
            self.element_diagnose = element_diagnose
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
    def type(self):
        """Gets the type of this SecurityFeatureResult.  # noqa: E501

        Same as authenticity result type, but used for safe parsing of not-described values: https://docs.webclientforensics.com/develop/doc-reader-sdk/web-service/development/enums/authenticity-result-type/  # noqa: E501

        :return: The type of this SecurityFeatureResult.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SecurityFeatureResult.

        Same as authenticity result type, but used for safe parsing of not-described values: https://docs.webclientforensics.com/develop/doc-reader-sdk/web-service/development/enums/authenticity-result-type/  # noqa: E501

        :param type: The type of this SecurityFeatureResult.  # noqa: E501
        :type type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def element_result(self):
        """Gets the element_result of this SecurityFeatureResult.  # noqa: E501


        :return: The element_result of this SecurityFeatureResult.  # noqa: E501
        :rtype: CheckResult
        """
        return self._element_result

    @element_result.setter
    def element_result(self, element_result):
        """Sets the element_result of this SecurityFeatureResult.


        :param element_result: The element_result of this SecurityFeatureResult.  # noqa: E501
        :type element_result: CheckResult
        """

        self._element_result = element_result

    @property
    def element_diagnose(self):
        """Gets the element_diagnose of this SecurityFeatureResult.  # noqa: E501


        :return: The element_diagnose of this SecurityFeatureResult.  # noqa: E501
        :rtype: CheckDiagnose
        """
        return self._element_diagnose

    @element_diagnose.setter
    def element_diagnose(self, element_diagnose):
        """Sets the element_diagnose of this SecurityFeatureResult.


        :param element_diagnose: The element_diagnose of this SecurityFeatureResult.  # noqa: E501
        :type element_diagnose: CheckDiagnose
        """

        self._element_diagnose = element_diagnose

    @property
    def element_type(self):
        """Gets the element_type of this SecurityFeatureResult.  # noqa: E501


        :return: The element_type of this SecurityFeatureResult.  # noqa: E501
        :rtype: SecurityFeatureType
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this SecurityFeatureResult.


        :param element_type: The element_type of this SecurityFeatureResult.  # noqa: E501
        :type element_type: SecurityFeatureType
        """

        self._element_type = element_type

    @property
    def element_rect(self):
        """Gets the element_rect of this SecurityFeatureResult.  # noqa: E501


        :return: The element_rect of this SecurityFeatureResult.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._element_rect

    @element_rect.setter
    def element_rect(self, element_rect):
        """Sets the element_rect of this SecurityFeatureResult.


        :param element_rect: The element_rect of this SecurityFeatureResult.  # noqa: E501
        :type element_rect: RectangleCoordinates
        """

        self._element_rect = element_rect

    @property
    def visibility(self):
        """Gets the visibility of this SecurityFeatureResult.  # noqa: E501


        :return: The visibility of this SecurityFeatureResult.  # noqa: E501
        :rtype: Visibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this SecurityFeatureResult.


        :param visibility: The visibility of this SecurityFeatureResult.  # noqa: E501
        :type visibility: Visibility
        """

        self._visibility = visibility

    @property
    def critical_flag(self):
        """Gets the critical_flag of this SecurityFeatureResult.  # noqa: E501


        :return: The critical_flag of this SecurityFeatureResult.  # noqa: E501
        :rtype: Critical
        """
        return self._critical_flag

    @critical_flag.setter
    def critical_flag(self, critical_flag):
        """Sets the critical_flag of this SecurityFeatureResult.


        :param critical_flag: The critical_flag of this SecurityFeatureResult.  # noqa: E501
        :type critical_flag: Critical
        """

        self._critical_flag = critical_flag

    @property
    def area_list(self):
        """Gets the area_list of this SecurityFeatureResult.  # noqa: E501


        :return: The area_list of this SecurityFeatureResult.  # noqa: E501
        :rtype: AreaContainer
        """
        return self._area_list

    @area_list.setter
    def area_list(self, area_list):
        """Sets the area_list of this SecurityFeatureResult.


        :param area_list: The area_list of this SecurityFeatureResult.  # noqa: E501
        :type area_list: AreaContainer
        """

        self._area_list = area_list

    @property
    def reserved2(self):
        """Gets the reserved2 of this SecurityFeatureResult.  # noqa: E501


        :return: The reserved2 of this SecurityFeatureResult.  # noqa: E501
        :rtype: int
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """Sets the reserved2 of this SecurityFeatureResult.


        :param reserved2: The reserved2 of this SecurityFeatureResult.  # noqa: E501
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
        if not isinstance(other, SecurityFeatureResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityFeatureResult):
            return True

        return self.to_dict() != other.to_dict()
