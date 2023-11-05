# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class BcPDF417INFO(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'angle': 'float',
        'bc_column': 'int',
        'bc_error_level': 'int',
        'bc_row': 'int',
        'min_x': 'float',
        'min_y': 'float'
    }

    attribute_map = {
        'angle': 'Angle',
        'bc_column': 'bcColumn',
        'bc_error_level': 'bcErrorLevel',
        'bc_row': 'bcRow',
        'min_x': 'minX',
        'min_y': 'minY'
    }

    def __init__(self, angle=None, bc_column=None, bc_error_level=None, bc_row=None, min_x=None, min_y=None, local_vars_configuration=None):  # noqa: E501
        """BcPDF417INFO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._angle = None
        self._bc_column = None
        self._bc_error_level = None
        self._bc_row = None
        self._min_x = None
        self._min_y = None
        self.discriminator = None

        if angle is not None:
            self.angle = angle
        if bc_column is not None:
            self.bc_column = bc_column
        if bc_error_level is not None:
            self.bc_error_level = bc_error_level
        if bc_row is not None:
            self.bc_row = bc_row
        if min_x is not None:
            self.min_x = min_x
        if min_y is not None:
            self.min_y = min_y

    @property
    def angle(self):
        """Gets the angle of this BcPDF417INFO.  # noqa: E501


        :return: The angle of this BcPDF417INFO.  # noqa: E501
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this BcPDF417INFO.


        :param angle: The angle of this BcPDF417INFO.  # noqa: E501
        :type angle: float
        """

        self._angle = angle

    @property
    def bc_column(self):
        """Gets the bc_column of this BcPDF417INFO.  # noqa: E501


        :return: The bc_column of this BcPDF417INFO.  # noqa: E501
        :rtype: int
        """
        return self._bc_column

    @bc_column.setter
    def bc_column(self, bc_column):
        """Sets the bc_column of this BcPDF417INFO.


        :param bc_column: The bc_column of this BcPDF417INFO.  # noqa: E501
        :type bc_column: int
        """

        self._bc_column = bc_column

    @property
    def bc_error_level(self):
        """Gets the bc_error_level of this BcPDF417INFO.  # noqa: E501


        :return: The bc_error_level of this BcPDF417INFO.  # noqa: E501
        :rtype: int
        """
        return self._bc_error_level

    @bc_error_level.setter
    def bc_error_level(self, bc_error_level):
        """Sets the bc_error_level of this BcPDF417INFO.


        :param bc_error_level: The bc_error_level of this BcPDF417INFO.  # noqa: E501
        :type bc_error_level: int
        """

        self._bc_error_level = bc_error_level

    @property
    def bc_row(self):
        """Gets the bc_row of this BcPDF417INFO.  # noqa: E501


        :return: The bc_row of this BcPDF417INFO.  # noqa: E501
        :rtype: int
        """
        return self._bc_row

    @bc_row.setter
    def bc_row(self, bc_row):
        """Sets the bc_row of this BcPDF417INFO.


        :param bc_row: The bc_row of this BcPDF417INFO.  # noqa: E501
        :type bc_row: int
        """

        self._bc_row = bc_row

    @property
    def min_x(self):
        """Gets the min_x of this BcPDF417INFO.  # noqa: E501


        :return: The min_x of this BcPDF417INFO.  # noqa: E501
        :rtype: float
        """
        return self._min_x

    @min_x.setter
    def min_x(self, min_x):
        """Sets the min_x of this BcPDF417INFO.


        :param min_x: The min_x of this BcPDF417INFO.  # noqa: E501
        :type min_x: float
        """

        self._min_x = min_x

    @property
    def min_y(self):
        """Gets the min_y of this BcPDF417INFO.  # noqa: E501


        :return: The min_y of this BcPDF417INFO.  # noqa: E501
        :rtype: float
        """
        return self._min_y

    @min_y.setter
    def min_y(self, min_y):
        """Sets the min_y of this BcPDF417INFO.


        :param min_y: The min_y of this BcPDF417INFO.  # noqa: E501
        :type min_y: float
        """

        self._min_y = min_y

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
        if not isinstance(other, BcPDF417INFO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BcPDF417INFO):
            return True

        return self.to_dict() != other.to_dict()
