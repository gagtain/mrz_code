# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""
Coordinates of the rectangle region on a document image(result type 1). Represented by two points - (left, top) + (right, bottom)
"""
class RectangleCoordinates(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'left': 'int',
        'top': 'int',
        'right': 'int',
        'bottom': 'int'
    }

    attribute_map = {
        'left': 'left',
        'top': 'top',
        'right': 'right',
        'bottom': 'bottom'
    }

    def __init__(self, left=None, top=None, right=None, bottom=None, local_vars_configuration=None):  # noqa: E501
        """RectangleCoordinates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._left = None
        self._top = None
        self._right = None
        self._bottom = None
        self.discriminator = None

        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @property
    def left(self):
        """Gets the left of this RectangleCoordinates.  # noqa: E501


        :return: The left of this RectangleCoordinates.  # noqa: E501
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this RectangleCoordinates.


        :param left: The left of this RectangleCoordinates.  # noqa: E501
        :type left: int
        """
        if self.local_vars_configuration.client_side_validation and left is None:  # noqa: E501
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501

        self._left = left

    @property
    def top(self):
        """Gets the top of this RectangleCoordinates.  # noqa: E501


        :return: The top of this RectangleCoordinates.  # noqa: E501
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this RectangleCoordinates.


        :param top: The top of this RectangleCoordinates.  # noqa: E501
        :type top: int
        """
        if self.local_vars_configuration.client_side_validation and top is None:  # noqa: E501
            raise ValueError("Invalid value for `top`, must not be `None`")  # noqa: E501

        self._top = top

    @property
    def right(self):
        """Gets the right of this RectangleCoordinates.  # noqa: E501


        :return: The right of this RectangleCoordinates.  # noqa: E501
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this RectangleCoordinates.


        :param right: The right of this RectangleCoordinates.  # noqa: E501
        :type right: int
        """
        if self.local_vars_configuration.client_side_validation and right is None:  # noqa: E501
            raise ValueError("Invalid value for `right`, must not be `None`")  # noqa: E501

        self._right = right

    @property
    def bottom(self):
        """Gets the bottom of this RectangleCoordinates.  # noqa: E501


        :return: The bottom of this RectangleCoordinates.  # noqa: E501
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this RectangleCoordinates.


        :param bottom: The bottom of this RectangleCoordinates.  # noqa: E501
        :type bottom: int
        """
        if self.local_vars_configuration.client_side_validation and bottom is None:  # noqa: E501
            raise ValueError("Invalid value for `bottom`, must not be `None`")  # noqa: E501

        self._bottom = bottom

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
        if not isinstance(other, RectangleCoordinates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RectangleCoordinates):
            return True

        return self.to_dict() != other.to_dict()
