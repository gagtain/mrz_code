# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class DocBarCodeInfoFieldsList(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'n_fields': 'int',
        'p_array_fields': 'list[PArrayField]'
    }

    attribute_map = {
        'n_fields': 'nFields',
        'p_array_fields': 'pArrayFields'
    }

    def __init__(self, n_fields=None, p_array_fields=None, local_vars_configuration=None):  # noqa: E501
        """DocBarCodeInfoFieldsList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._n_fields = None
        self._p_array_fields = None
        self.discriminator = None

        if n_fields is not None:
            self.n_fields = n_fields
        if p_array_fields is not None:
            self.p_array_fields = p_array_fields

    @property
    def n_fields(self):
        """Gets the n_fields of this DocBarCodeInfoFieldsList.  # noqa: E501

        Count of array fields  # noqa: E501

        :return: The n_fields of this DocBarCodeInfoFieldsList.  # noqa: E501
        :rtype: int
        """
        return self._n_fields

    @n_fields.setter
    def n_fields(self, n_fields):
        """Sets the n_fields of this DocBarCodeInfoFieldsList.

        Count of array fields  # noqa: E501

        :param n_fields: The n_fields of this DocBarCodeInfoFieldsList.  # noqa: E501
        :type n_fields: int
        """

        self._n_fields = n_fields

    @property
    def p_array_fields(self):
        """Gets the p_array_fields of this DocBarCodeInfoFieldsList.  # noqa: E501

        Data from barcode  # noqa: E501

        :return: The p_array_fields of this DocBarCodeInfoFieldsList.  # noqa: E501
        :rtype: list[PArrayField]
        """
        return self._p_array_fields

    @p_array_fields.setter
    def p_array_fields(self, p_array_fields):
        """Sets the p_array_fields of this DocBarCodeInfoFieldsList.

        Data from barcode  # noqa: E501

        :param p_array_fields: The p_array_fields of this DocBarCodeInfoFieldsList.  # noqa: E501
        :type p_array_fields: list[PArrayField]
        """

        self._p_array_fields = p_array_fields

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
        if not isinstance(other, DocBarCodeInfoFieldsList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocBarCodeInfoFieldsList):
            return True

        return self.to_dict() != other.to_dict()
