# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""
Contains cropped and rotated with perspective compensation image of document. Single input image can contain multiple document side/pages, which will be returned as separated results. Most of coordinates in other types defined on that image
"""
class DocumentImageResultAllOf(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'raw_image_container': 'ImageData'
    }

    attribute_map = {
        'raw_image_container': 'RawImageContainer'
    }

    def __init__(self, raw_image_container=None, local_vars_configuration=None):  # noqa: E501
        """DocumentImageResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._raw_image_container = None
        self.discriminator = None

        self.raw_image_container = raw_image_container

    @property
    def raw_image_container(self):
        """Gets the raw_image_container of this DocumentImageResultAllOf.  # noqa: E501


        :return: The raw_image_container of this DocumentImageResultAllOf.  # noqa: E501
        :rtype: ImageData
        """
        return self._raw_image_container

    @raw_image_container.setter
    def raw_image_container(self, raw_image_container):
        """Sets the raw_image_container of this DocumentImageResultAllOf.


        :param raw_image_container: The raw_image_container of this DocumentImageResultAllOf.  # noqa: E501
        :type raw_image_container: ImageData
        """
        if self.local_vars_configuration.client_side_validation and raw_image_container is None:  # noqa: E501
            raise ValueError("Invalid value for `raw_image_container`, must not be `None`")  # noqa: E501

        self._raw_image_container = raw_image_container

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
        if not isinstance(other, DocumentImageResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentImageResultAllOf):
            return True

        return self.to_dict() != other.to_dict()
