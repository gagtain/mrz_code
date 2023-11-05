# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class DocBarCodeInfoAllOf(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'doc_bar_code_info': 'DocBarCodeInfoFieldsList'
    }

    attribute_map = {
        'doc_bar_code_info': 'DocBarCodeInfo'
    }

    def __init__(self, doc_bar_code_info=None, local_vars_configuration=None):  # noqa: E501
        """DocBarCodeInfoAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._doc_bar_code_info = None
        self.discriminator = None

        if doc_bar_code_info is not None:
            self.doc_bar_code_info = doc_bar_code_info

    @property
    def doc_bar_code_info(self):
        """Gets the doc_bar_code_info of this DocBarCodeInfoAllOf.  # noqa: E501


        :return: The doc_bar_code_info of this DocBarCodeInfoAllOf.  # noqa: E501
        :rtype: DocBarCodeInfoFieldsList
        """
        return self._doc_bar_code_info

    @doc_bar_code_info.setter
    def doc_bar_code_info(self, doc_bar_code_info):
        """Sets the doc_bar_code_info of this DocBarCodeInfoAllOf.


        :param doc_bar_code_info: The doc_bar_code_info of this DocBarCodeInfoAllOf.  # noqa: E501
        :type doc_bar_code_info: DocBarCodeInfoFieldsList
        """

        self._doc_bar_code_info = doc_bar_code_info

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
        if not isinstance(other, DocBarCodeInfoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocBarCodeInfoAllOf):
            return True

        return self.to_dict() != other.to_dict()
