# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class DataModule(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'm_data': 'str',
        'm_length': 'int',
        'm_reserved1': 'int',
        'm_reserver2': 'int',
        'm_type': 'int'
    }

    attribute_map = {
        'm_data': 'mData',
        'm_length': 'mLength',
        'm_reserved1': 'mReserved1',
        'm_reserver2': 'mReserver2',
        'm_type': 'mType'
    }

    def __init__(self, m_data=None, m_length=None, m_reserved1=None, m_reserver2=None, m_type=None, local_vars_configuration=None):  # noqa: E501
        """DataModule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._m_data = None
        self._m_length = None
        self._m_reserved1 = None
        self._m_reserver2 = None
        self._m_type = None
        self.discriminator = None

        if m_data is not None:
            self.m_data = m_data
        if m_length is not None:
            self.m_length = m_length
        if m_reserved1 is not None:
            self.m_reserved1 = m_reserved1
        if m_reserver2 is not None:
            self.m_reserver2 = m_reserver2
        if m_type is not None:
            self.m_type = m_type

    @property
    def m_data(self):
        """Gets the m_data of this DataModule.  # noqa: E501


        :return: The m_data of this DataModule.  # noqa: E501
        :rtype: str
        """
        return self._m_data

    @m_data.setter
    def m_data(self, m_data):
        """Sets the m_data of this DataModule.


        :param m_data: The m_data of this DataModule.  # noqa: E501
        :type m_data: str
        """

        self._m_data = m_data

    @property
    def m_length(self):
        """Gets the m_length of this DataModule.  # noqa: E501


        :return: The m_length of this DataModule.  # noqa: E501
        :rtype: int
        """
        return self._m_length

    @m_length.setter
    def m_length(self, m_length):
        """Sets the m_length of this DataModule.


        :param m_length: The m_length of this DataModule.  # noqa: E501
        :type m_length: int
        """

        self._m_length = m_length

    @property
    def m_reserved1(self):
        """Gets the m_reserved1 of this DataModule.  # noqa: E501


        :return: The m_reserved1 of this DataModule.  # noqa: E501
        :rtype: int
        """
        return self._m_reserved1

    @m_reserved1.setter
    def m_reserved1(self, m_reserved1):
        """Sets the m_reserved1 of this DataModule.


        :param m_reserved1: The m_reserved1 of this DataModule.  # noqa: E501
        :type m_reserved1: int
        """

        self._m_reserved1 = m_reserved1

    @property
    def m_reserver2(self):
        """Gets the m_reserver2 of this DataModule.  # noqa: E501


        :return: The m_reserver2 of this DataModule.  # noqa: E501
        :rtype: int
        """
        return self._m_reserver2

    @m_reserver2.setter
    def m_reserver2(self, m_reserver2):
        """Sets the m_reserver2 of this DataModule.


        :param m_reserver2: The m_reserver2 of this DataModule.  # noqa: E501
        :type m_reserver2: int
        """

        self._m_reserver2 = m_reserver2

    @property
    def m_type(self):
        """Gets the m_type of this DataModule.  # noqa: E501


        :return: The m_type of this DataModule.  # noqa: E501
        :rtype: int
        """
        return self._m_type

    @m_type.setter
    def m_type(self, m_type):
        """Sets the m_type of this DataModule.


        :param m_type: The m_type of this DataModule.  # noqa: E501
        :type m_type: int
        """

        self._m_type = m_type

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
        if not isinstance(other, DataModule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataModule):
            return True

        return self.to_dict() != other.to_dict()
