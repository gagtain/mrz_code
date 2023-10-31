# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class ListVerifiedFields(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'p_field_maps': 'list[VerifiedFieldMap]'
    }

    attribute_map = {
        'p_field_maps': 'pFieldMaps'
    }

    def __init__(self, p_field_maps=None, local_vars_configuration=None):  # noqa: E501
        """ListVerifiedFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._p_field_maps = None
        self.discriminator = None

        if p_field_maps is not None:
            self.p_field_maps = p_field_maps

    @property
    def p_field_maps(self):
        """Gets the p_field_maps of this ListVerifiedFields.  # noqa: E501


        :return: The p_field_maps of this ListVerifiedFields.  # noqa: E501
        :rtype: list[VerifiedFieldMap]
        """
        return self._p_field_maps

    @p_field_maps.setter
    def p_field_maps(self, p_field_maps):
        """Sets the p_field_maps of this ListVerifiedFields.


        :param p_field_maps: The p_field_maps of this ListVerifiedFields.  # noqa: E501
        :type p_field_maps: list[VerifiedFieldMap]
        """

        self._p_field_maps = p_field_maps

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
        if not isinstance(other, ListVerifiedFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListVerifiedFields):
            return True

        return self.to_dict() != other.to_dict()
