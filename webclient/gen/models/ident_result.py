# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class IdentResult(object):
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
        'light_index': 'Light',
        'area': 'RectangleCoordinates',
        'image': 'ImageData',
        'etalon_image': 'ImageData',
        'percent_value': 'int',
        'area_list': 'AreaContainer'
    }

    attribute_map = {
        'type': 'Type',
        'element_result': 'ElementResult',
        'element_diagnose': 'ElementDiagnose',
        'element_type': 'ElementType',
        'light_index': 'LightIndex',
        'area': 'Area',
        'image': 'Image',
        'etalon_image': 'EtalonImage',
        'percent_value': 'PercentValue',
        'area_list': 'AreaList'
    }

    def __init__(self, type=0, element_result=None, element_diagnose=None, element_type=None, light_index=None, area=None, image=None, etalon_image=None, percent_value=None, area_list=None, local_vars_configuration=None):  # noqa: E501
        """IdentResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._element_result = None
        self._element_diagnose = None
        self._element_type = None
        self._light_index = None
        self._area = None
        self._image = None
        self._etalon_image = None
        self._percent_value = None
        self._area_list = None
        self.discriminator = None

        self.type = type
        if element_result is not None:
            self.element_result = element_result
        if element_diagnose is not None:
            self.element_diagnose = element_diagnose
        if element_type is not None:
            self.element_type = element_type
        if light_index is not None:
            self.light_index = light_index
        if area is not None:
            self.area = area
        if image is not None:
            self.image = image
        if etalon_image is not None:
            self.etalon_image = etalon_image
        if percent_value is not None:
            self.percent_value = percent_value
        if area_list is not None:
            self.area_list = area_list

    @property
    def type(self):
        """Gets the type of this IdentResult.  # noqa: E501

        Same as authenticity result type, but used for safe parsing of not-described values: https://docs.webclientforensics.com/develop/doc-reader-sdk/web-service/development/enums/authenticity-result-type/  # noqa: E501

        :return: The type of this IdentResult.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentResult.

        Same as authenticity result type, but used for safe parsing of not-described values: https://docs.webclientforensics.com/develop/doc-reader-sdk/web-service/development/enums/authenticity-result-type/  # noqa: E501

        :param type: The type of this IdentResult.  # noqa: E501
        :type type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def element_result(self):
        """Gets the element_result of this IdentResult.  # noqa: E501


        :return: The element_result of this IdentResult.  # noqa: E501
        :rtype: CheckResult
        """
        return self._element_result

    @element_result.setter
    def element_result(self, element_result):
        """Sets the element_result of this IdentResult.


        :param element_result: The element_result of this IdentResult.  # noqa: E501
        :type element_result: CheckResult
        """

        self._element_result = element_result

    @property
    def element_diagnose(self):
        """Gets the element_diagnose of this IdentResult.  # noqa: E501


        :return: The element_diagnose of this IdentResult.  # noqa: E501
        :rtype: CheckDiagnose
        """
        return self._element_diagnose

    @element_diagnose.setter
    def element_diagnose(self, element_diagnose):
        """Sets the element_diagnose of this IdentResult.


        :param element_diagnose: The element_diagnose of this IdentResult.  # noqa: E501
        :type element_diagnose: CheckDiagnose
        """

        self._element_diagnose = element_diagnose

    @property
    def element_type(self):
        """Gets the element_type of this IdentResult.  # noqa: E501


        :return: The element_type of this IdentResult.  # noqa: E501
        :rtype: SecurityFeatureType
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this IdentResult.


        :param element_type: The element_type of this IdentResult.  # noqa: E501
        :type element_type: SecurityFeatureType
        """

        self._element_type = element_type

    @property
    def light_index(self):
        """Gets the light_index of this IdentResult.  # noqa: E501


        :return: The light_index of this IdentResult.  # noqa: E501
        :rtype: Light
        """
        return self._light_index

    @light_index.setter
    def light_index(self, light_index):
        """Sets the light_index of this IdentResult.


        :param light_index: The light_index of this IdentResult.  # noqa: E501
        :type light_index: Light
        """

        self._light_index = light_index

    @property
    def area(self):
        """Gets the area of this IdentResult.  # noqa: E501


        :return: The area of this IdentResult.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this IdentResult.


        :param area: The area of this IdentResult.  # noqa: E501
        :type area: RectangleCoordinates
        """

        self._area = area

    @property
    def image(self):
        """Gets the image of this IdentResult.  # noqa: E501


        :return: The image of this IdentResult.  # noqa: E501
        :rtype: ImageData
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IdentResult.


        :param image: The image of this IdentResult.  # noqa: E501
        :type image: ImageData
        """

        self._image = image

    @property
    def etalon_image(self):
        """Gets the etalon_image of this IdentResult.  # noqa: E501


        :return: The etalon_image of this IdentResult.  # noqa: E501
        :rtype: ImageData
        """
        return self._etalon_image

    @etalon_image.setter
    def etalon_image(self, etalon_image):
        """Sets the etalon_image of this IdentResult.


        :param etalon_image: The etalon_image of this IdentResult.  # noqa: E501
        :type etalon_image: ImageData
        """

        self._etalon_image = etalon_image

    @property
    def percent_value(self):
        """Gets the percent_value of this IdentResult.  # noqa: E501

        Probability percent for IMAGE_PATTERN check or element's visibility for IR_VISIBILITY  # noqa: E501

        :return: The percent_value of this IdentResult.  # noqa: E501
        :rtype: int
        """
        return self._percent_value

    @percent_value.setter
    def percent_value(self, percent_value):
        """Sets the percent_value of this IdentResult.

        Probability percent for IMAGE_PATTERN check or element's visibility for IR_VISIBILITY  # noqa: E501

        :param percent_value: The percent_value of this IdentResult.  # noqa: E501
        :type percent_value: int
        """

        self._percent_value = percent_value

    @property
    def area_list(self):
        """Gets the area_list of this IdentResult.  # noqa: E501


        :return: The area_list of this IdentResult.  # noqa: E501
        :rtype: AreaContainer
        """
        return self._area_list

    @area_list.setter
    def area_list(self, area_list):
        """Sets the area_list of this IdentResult.


        :param area_list: The area_list of this IdentResult.  # noqa: E501
        :type area_list: AreaContainer
        """

        self._area_list = area_list

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
        if not isinstance(other, IdentResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentResult):
            return True

        return self.to_dict() != other.to_dict()
