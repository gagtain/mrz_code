# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class BcROIDETECT(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bottom': 'int',
        'left': 'int',
        'right': 'int',
        'top': 'int'
    }

    attribute_map = {
        'bottom': 'bottom',
        'left': 'left',
        'right': 'right',
        'top': 'top'
    }

    def __init__(self, bottom=None, left=None, right=None, top=None, local_vars_configuration=None):  # noqa: E501
        """BcROIDETECT - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bottom = None
        self._left = None
        self._right = None
        self._top = None
        self.discriminator = None

        if bottom is not None:
            self.bottom = bottom
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        if top is not None:
            self.top = top

    @property
    def bottom(self):
        """Gets the bottom of this BcROIDETECT.  # noqa: E501


        :return: The bottom of this BcROIDETECT.  # noqa: E501
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this BcROIDETECT.


        :param bottom: The bottom of this BcROIDETECT.  # noqa: E501
        :type bottom: int
        """

        self._bottom = bottom

    @property
    def left(self):
        """Gets the left of this BcROIDETECT.  # noqa: E501


        :return: The left of this BcROIDETECT.  # noqa: E501
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this BcROIDETECT.


        :param left: The left of this BcROIDETECT.  # noqa: E501
        :type left: int
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this BcROIDETECT.  # noqa: E501


        :return: The right of this BcROIDETECT.  # noqa: E501
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this BcROIDETECT.


        :param right: The right of this BcROIDETECT.  # noqa: E501
        :type right: int
        """

        self._right = right

    @property
    def top(self):
        """Gets the top of this BcROIDETECT.  # noqa: E501


        :return: The top of this BcROIDETECT.  # noqa: E501
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this BcROIDETECT.


        :param top: The top of this BcROIDETECT.  # noqa: E501
        :type top: int
        """

        self._top = top

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
        if not isinstance(other, BcROIDETECT):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BcROIDETECT):
            return True

        return self.to_dict() != other.to_dict()
