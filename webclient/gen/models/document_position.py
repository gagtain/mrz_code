# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class DocumentPosition(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'doc_format': 'DocumentFormat',
        'angle': 'float',
        'width': 'int',
        'height': 'int',
        'center': 'Point',
        'left_bottom': 'Point',
        'left_top': 'Point',
        'right_bottom': 'Point',
        'right_top': 'Point',
        'dpi': 'int'
    }

    attribute_map = {
        'doc_format': 'docFormat',
        'angle': 'Angle',
        'width': 'Width',
        'height': 'Height',
        'center': 'Center',
        'left_bottom': 'LeftBottom',
        'left_top': 'LeftTop',
        'right_bottom': 'RightBottom',
        'right_top': 'RightTop',
        'dpi': 'Dpi'
    }

    def __init__(self, doc_format=None, angle=None, width=None, height=None, center=None, left_bottom=None, left_top=None, right_bottom=None, right_top=None, dpi=None, local_vars_configuration=None):  # noqa: E501
        """DocumentPosition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._doc_format = None
        self._angle = None
        self._width = None
        self._height = None
        self._center = None
        self._left_bottom = None
        self._left_top = None
        self._right_bottom = None
        self._right_top = None
        self._dpi = None
        self.discriminator = None

        if doc_format is not None:
            self.doc_format = doc_format
        if angle is not None:
            self.angle = angle
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if center is not None:
            self.center = center
        if left_bottom is not None:
            self.left_bottom = left_bottom
        if left_top is not None:
            self.left_top = left_top
        if right_bottom is not None:
            self.right_bottom = right_bottom
        if right_top is not None:
            self.right_top = right_top
        if dpi is not None:
            self.dpi = dpi

    @property
    def doc_format(self):
        """Gets the doc_format of this DocumentPosition.  # noqa: E501


        :return: The doc_format of this DocumentPosition.  # noqa: E501
        :rtype: DocumentFormat
        """
        return self._doc_format

    @doc_format.setter
    def doc_format(self, doc_format):
        """Sets the doc_format of this DocumentPosition.


        :param doc_format: The doc_format of this DocumentPosition.  # noqa: E501
        :type doc_format: DocumentFormat
        """

        self._doc_format = doc_format

    @property
    def angle(self):
        """Gets the angle of this DocumentPosition.  # noqa: E501


        :return: The angle of this DocumentPosition.  # noqa: E501
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this DocumentPosition.


        :param angle: The angle of this DocumentPosition.  # noqa: E501
        :type angle: float
        """

        self._angle = angle

    @property
    def width(self):
        """Gets the width of this DocumentPosition.  # noqa: E501


        :return: The width of this DocumentPosition.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DocumentPosition.


        :param width: The width of this DocumentPosition.  # noqa: E501
        :type width: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this DocumentPosition.  # noqa: E501


        :return: The height of this DocumentPosition.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DocumentPosition.


        :param height: The height of this DocumentPosition.  # noqa: E501
        :type height: int
        """

        self._height = height

    @property
    def center(self):
        """Gets the center of this DocumentPosition.  # noqa: E501


        :return: The center of this DocumentPosition.  # noqa: E501
        :rtype: Point
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this DocumentPosition.


        :param center: The center of this DocumentPosition.  # noqa: E501
        :type center: Point
        """

        self._center = center

    @property
    def left_bottom(self):
        """Gets the left_bottom of this DocumentPosition.  # noqa: E501


        :return: The left_bottom of this DocumentPosition.  # noqa: E501
        :rtype: Point
        """
        return self._left_bottom

    @left_bottom.setter
    def left_bottom(self, left_bottom):
        """Sets the left_bottom of this DocumentPosition.


        :param left_bottom: The left_bottom of this DocumentPosition.  # noqa: E501
        :type left_bottom: Point
        """

        self._left_bottom = left_bottom

    @property
    def left_top(self):
        """Gets the left_top of this DocumentPosition.  # noqa: E501


        :return: The left_top of this DocumentPosition.  # noqa: E501
        :rtype: Point
        """
        return self._left_top

    @left_top.setter
    def left_top(self, left_top):
        """Sets the left_top of this DocumentPosition.


        :param left_top: The left_top of this DocumentPosition.  # noqa: E501
        :type left_top: Point
        """

        self._left_top = left_top

    @property
    def right_bottom(self):
        """Gets the right_bottom of this DocumentPosition.  # noqa: E501


        :return: The right_bottom of this DocumentPosition.  # noqa: E501
        :rtype: Point
        """
        return self._right_bottom

    @right_bottom.setter
    def right_bottom(self, right_bottom):
        """Sets the right_bottom of this DocumentPosition.


        :param right_bottom: The right_bottom of this DocumentPosition.  # noqa: E501
        :type right_bottom: Point
        """

        self._right_bottom = right_bottom

    @property
    def right_top(self):
        """Gets the right_top of this DocumentPosition.  # noqa: E501


        :return: The right_top of this DocumentPosition.  # noqa: E501
        :rtype: Point
        """
        return self._right_top

    @right_top.setter
    def right_top(self, right_top):
        """Sets the right_top of this DocumentPosition.


        :param right_top: The right_top of this DocumentPosition.  # noqa: E501
        :type right_top: Point
        """

        self._right_top = right_top

    @property
    def dpi(self):
        """Gets the dpi of this DocumentPosition.  # noqa: E501


        :return: The dpi of this DocumentPosition.  # noqa: E501
        :rtype: int
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """Sets the dpi of this DocumentPosition.


        :param dpi: The dpi of this DocumentPosition.  # noqa: E501
        :type dpi: int
        """

        self._dpi = dpi

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
        if not isinstance(other, DocumentPosition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentPosition):
            return True

        return self.to_dict() != other.to_dict()
