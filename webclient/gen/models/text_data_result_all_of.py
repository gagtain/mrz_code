# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class TextDataResultAllOf(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'doc_visual_extended_info': 'DocVisualExtendedInfo'
    }

    attribute_map = {
        'doc_visual_extended_info': 'DocVisualExtendedInfo'
    }

    def __init__(self, doc_visual_extended_info=None, local_vars_configuration=None):  # noqa: E501
        """TextDataResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._doc_visual_extended_info = None
        self.discriminator = None

        if doc_visual_extended_info is not None:
            self.doc_visual_extended_info = doc_visual_extended_info

    @property
    def doc_visual_extended_info(self):
        """Gets the doc_visual_extended_info of this TextDataResultAllOf.  # noqa: E501


        :return: The doc_visual_extended_info of this TextDataResultAllOf.  # noqa: E501
        :rtype: DocVisualExtendedInfo
        """
        return self._doc_visual_extended_info

    @doc_visual_extended_info.setter
    def doc_visual_extended_info(self, doc_visual_extended_info):
        """Sets the doc_visual_extended_info of this TextDataResultAllOf.


        :param doc_visual_extended_info: The doc_visual_extended_info of this TextDataResultAllOf.  # noqa: E501
        :type doc_visual_extended_info: DocVisualExtendedInfo
        """

        self._doc_visual_extended_info = doc_visual_extended_info

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
        if not isinstance(other, TextDataResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextDataResultAllOf):
            return True

        return self.to_dict() != other.to_dict()
