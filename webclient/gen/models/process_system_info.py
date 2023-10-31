# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class ProcessSystemInfo(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'license': 'str',
        'recaptcha_token': 'str'
    }

    attribute_map = {
        'license': 'license',
        'recaptcha_token': 'recaptcha_token'
    }

    def __init__(self, license=None, recaptcha_token=None, local_vars_configuration=None):  # noqa: E501
        """ProcessSystemInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._license = None
        self._recaptcha_token = None
        self.discriminator = None

        if license is not None:
            self.license = license
        if recaptcha_token is not None:
            self.recaptcha_token = recaptcha_token

    @property
    def license(self):
        """Gets the license of this ProcessSystemInfo.  # noqa: E501

        Base64 encoded license file  # noqa: E501

        :return: The license of this ProcessSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ProcessSystemInfo.

        Base64 encoded license file  # noqa: E501

        :param license: The license of this ProcessSystemInfo.  # noqa: E501
        :type license: str
        """

        self._license = license

    @property
    def recaptcha_token(self):
        """Gets the recaptcha_token of this ProcessSystemInfo.  # noqa: E501

        For internal use. Demo-sites recaptcha token.  # noqa: E501

        :return: The recaptcha_token of this ProcessSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._recaptcha_token

    @recaptcha_token.setter
    def recaptcha_token(self, recaptcha_token):
        """Sets the recaptcha_token of this ProcessSystemInfo.

        For internal use. Demo-sites recaptcha token.  # noqa: E501

        :param recaptcha_token: The recaptcha_token of this ProcessSystemInfo.  # noqa: E501
        :type recaptcha_token: str
        """

        self._recaptcha_token = recaptcha_token

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
        if not isinstance(other, ProcessSystemInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessSystemInfo):
            return True

        return self.to_dict() != other.to_dict()
