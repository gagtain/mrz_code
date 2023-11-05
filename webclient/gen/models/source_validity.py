# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class SourceValidity(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'source': 'Source',
        'status': 'CheckResult'
    }

    attribute_map = {
        'source': 'source',
        'status': 'status'
    }

    def __init__(self, source=None, status=None, local_vars_configuration=None):  # noqa: E501
        """SourceValidity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._status = None
        self.discriminator = None

        self.source = source
        self.status = status

    @property
    def source(self):
        """Gets the source of this SourceValidity.  # noqa: E501


        :return: The source of this SourceValidity.  # noqa: E501
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SourceValidity.


        :param source: The source of this SourceValidity.  # noqa: E501
        :type source: Source
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def status(self):
        """Gets the status of this SourceValidity.  # noqa: E501


        :return: The status of this SourceValidity.  # noqa: E501
        :rtype: CheckResult
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SourceValidity.


        :param status: The status of this SourceValidity.  # noqa: E501
        :type status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, SourceValidity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceValidity):
            return True

        return self.to_dict() != other.to_dict()
