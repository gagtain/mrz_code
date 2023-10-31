# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class PhotoIdentResultAllOf(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'light_index': 'Light',
        'area': 'RectangleCoordinates',
        'source_image': 'ImageData',
        'result_images': 'RawImageContainerList',
        'field_types_count': 'int',
        'field_types_list': 'list[int]',
        'step': 'int',
        'angle': 'int',
        'reserved3': 'int'
    }

    attribute_map = {
        'light_index': 'LightIndex',
        'area': 'Area',
        'source_image': 'SourceImage',
        'result_images': 'ResultImages',
        'field_types_count': 'FieldTypesCount',
        'field_types_list': 'FieldTypesList',
        'step': 'Step',
        'angle': 'Angle',
        'reserved3': 'Reserved3'
    }

    def __init__(self, light_index=None, area=None, source_image=None, result_images=None, field_types_count=None, field_types_list=None, step=None, angle=None, reserved3=None, local_vars_configuration=None):  # noqa: E501
        """PhotoIdentResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._light_index = None
        self._area = None
        self._source_image = None
        self._result_images = None
        self._field_types_count = None
        self._field_types_list = None
        self._step = None
        self._angle = None
        self._reserved3 = None
        self.discriminator = None

        if light_index is not None:
            self.light_index = light_index
        if area is not None:
            self.area = area
        if source_image is not None:
            self.source_image = source_image
        if result_images is not None:
            self.result_images = result_images
        if field_types_count is not None:
            self.field_types_count = field_types_count
        if field_types_list is not None:
            self.field_types_list = field_types_list
        if step is not None:
            self.step = step
        if angle is not None:
            self.angle = angle
        if reserved3 is not None:
            self.reserved3 = reserved3

    @property
    def light_index(self):
        """Gets the light_index of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The light_index of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: Light
        """
        return self._light_index

    @light_index.setter
    def light_index(self, light_index):
        """Sets the light_index of this PhotoIdentResultAllOf.


        :param light_index: The light_index of this PhotoIdentResultAllOf.  # noqa: E501
        :type light_index: Light
        """

        self._light_index = light_index

    @property
    def area(self):
        """Gets the area of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The area of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this PhotoIdentResultAllOf.


        :param area: The area of this PhotoIdentResultAllOf.  # noqa: E501
        :type area: RectangleCoordinates
        """

        self._area = area

    @property
    def source_image(self):
        """Gets the source_image of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The source_image of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: ImageData
        """
        return self._source_image

    @source_image.setter
    def source_image(self, source_image):
        """Sets the source_image of this PhotoIdentResultAllOf.


        :param source_image: The source_image of this PhotoIdentResultAllOf.  # noqa: E501
        :type source_image: ImageData
        """

        self._source_image = source_image

    @property
    def result_images(self):
        """Gets the result_images of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The result_images of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: RawImageContainerList
        """
        return self._result_images

    @result_images.setter
    def result_images(self, result_images):
        """Sets the result_images of this PhotoIdentResultAllOf.


        :param result_images: The result_images of this PhotoIdentResultAllOf.  # noqa: E501
        :type result_images: RawImageContainerList
        """

        self._result_images = result_images

    @property
    def field_types_count(self):
        """Gets the field_types_count of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The field_types_count of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: int
        """
        return self._field_types_count

    @field_types_count.setter
    def field_types_count(self, field_types_count):
        """Sets the field_types_count of this PhotoIdentResultAllOf.


        :param field_types_count: The field_types_count of this PhotoIdentResultAllOf.  # noqa: E501
        :type field_types_count: int
        """

        self._field_types_count = field_types_count

    @property
    def field_types_list(self):
        """Gets the field_types_list of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The field_types_list of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: list[int]
        """
        return self._field_types_list

    @field_types_list.setter
    def field_types_list(self, field_types_list):
        """Sets the field_types_list of this PhotoIdentResultAllOf.


        :param field_types_list: The field_types_list of this PhotoIdentResultAllOf.  # noqa: E501
        :type field_types_list: list[int]
        """

        self._field_types_list = field_types_list

    @property
    def step(self):
        """Gets the step of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The step of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this PhotoIdentResultAllOf.


        :param step: The step of this PhotoIdentResultAllOf.  # noqa: E501
        :type step: int
        """

        self._step = step

    @property
    def angle(self):
        """Gets the angle of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The angle of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: int
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this PhotoIdentResultAllOf.


        :param angle: The angle of this PhotoIdentResultAllOf.  # noqa: E501
        :type angle: int
        """

        self._angle = angle

    @property
    def reserved3(self):
        """Gets the reserved3 of this PhotoIdentResultAllOf.  # noqa: E501


        :return: The reserved3 of this PhotoIdentResultAllOf.  # noqa: E501
        :rtype: int
        """
        return self._reserved3

    @reserved3.setter
    def reserved3(self, reserved3):
        """Sets the reserved3 of this PhotoIdentResultAllOf.


        :param reserved3: The reserved3 of this PhotoIdentResultAllOf.  # noqa: E501
        :type reserved3: int
        """

        self._reserved3 = reserved3

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
        if not isinstance(other, PhotoIdentResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhotoIdentResultAllOf):
            return True

        return self.to_dict() != other.to_dict()
