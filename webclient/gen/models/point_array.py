# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class PointArray(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'points_list': 'list[Point]'
    }

    attribute_map = {
        'points_list': 'PointsList'
    }

    def __init__(self, points_list=None, local_vars_configuration=None):  # noqa: E501
        """PointArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._points_list = None
        self.discriminator = None

        if points_list is not None:
            self.points_list = points_list

    @property
    def points_list(self):
        """Gets the points_list of this PointArray.  # noqa: E501


        :return: The points_list of this PointArray.  # noqa: E501
        :rtype: list[Point]
        """
        return self._points_list

    @points_list.setter
    def points_list(self, points_list):
        """Sets the points_list of this PointArray.


        :param points_list: The points_list of this PointArray.  # noqa: E501
        :type points_list: list[Point]
        """

        self._points_list = points_list

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
        if not isinstance(other, PointArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PointArray):
            return True

        return self.to_dict() != other.to_dict()
