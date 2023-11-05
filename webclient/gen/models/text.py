# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""
Contains all document text fields data with validity and cross-source compare checks
"""
class Text(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'CheckResult',
        'validity_status': 'CheckResult',
        'comparison_status': 'CheckResult',
        'field_list': 'list[TextField]',
        'available_source_list': 'list[TextAvailableSource]'
    }

    attribute_map = {
        'status': 'status',
        'validity_status': 'validityStatus',
        'comparison_status': 'comparisonStatus',
        'field_list': 'fieldList',
        'available_source_list': 'availableSourceList'
    }

    def __init__(self, status=None, validity_status=None, comparison_status=None, field_list=None, available_source_list=None, local_vars_configuration=None):  # noqa: E501
        """Text - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._validity_status = None
        self._comparison_status = None
        self._field_list = None
        self._available_source_list = None
        self.discriminator = None

        self.status = status
        self.validity_status = validity_status
        self.comparison_status = comparison_status
        self.field_list = field_list
        self.available_source_list = available_source_list

    @property
    def status(self):
        """Gets the status of this Text.  # noqa: E501


        :return: The status of this Text.  # noqa: E501
        :rtype: CheckResult
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Text.


        :param status: The status of this Text.  # noqa: E501
        :type status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def validity_status(self):
        """Gets the validity_status of this Text.  # noqa: E501


        :return: The validity_status of this Text.  # noqa: E501
        :rtype: CheckResult
        """
        return self._validity_status

    @validity_status.setter
    def validity_status(self, validity_status):
        """Sets the validity_status of this Text.


        :param validity_status: The validity_status of this Text.  # noqa: E501
        :type validity_status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and validity_status is None:  # noqa: E501
            raise ValueError("Invalid value for `validity_status`, must not be `None`")  # noqa: E501

        self._validity_status = validity_status

    @property
    def comparison_status(self):
        """Gets the comparison_status of this Text.  # noqa: E501


        :return: The comparison_status of this Text.  # noqa: E501
        :rtype: CheckResult
        """
        return self._comparison_status

    @comparison_status.setter
    def comparison_status(self, comparison_status):
        """Sets the comparison_status of this Text.


        :param comparison_status: The comparison_status of this Text.  # noqa: E501
        :type comparison_status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and comparison_status is None:  # noqa: E501
            raise ValueError("Invalid value for `comparison_status`, must not be `None`")  # noqa: E501

        self._comparison_status = comparison_status

    @property
    def field_list(self):
        """Gets the field_list of this Text.  # noqa: E501


        :return: The field_list of this Text.  # noqa: E501
        :rtype: list[TextField]
        """
        return self._field_list

    @field_list.setter
    def field_list(self, field_list):
        """Sets the field_list of this Text.


        :param field_list: The field_list of this Text.  # noqa: E501
        :type field_list: list[TextField]
        """
        if self.local_vars_configuration.client_side_validation and field_list is None:  # noqa: E501
            raise ValueError("Invalid value for `field_list`, must not be `None`")  # noqa: E501

        self._field_list = field_list

    @property
    def available_source_list(self):
        """Gets the available_source_list of this Text.  # noqa: E501


        :return: The available_source_list of this Text.  # noqa: E501
        :rtype: list[TextAvailableSource]
        """
        return self._available_source_list

    @available_source_list.setter
    def available_source_list(self, available_source_list):
        """Sets the available_source_list of this Text.


        :param available_source_list: The available_source_list of this Text.  # noqa: E501
        :type available_source_list: list[TextAvailableSource]
        """
        if self.local_vars_configuration.client_side_validation and available_source_list is None:  # noqa: E501
            raise ValueError("Invalid value for `available_source_list`, must not be `None`")  # noqa: E501

        self._available_source_list = available_source_list

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
        if not isinstance(other, Text):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Text):
            return True

        return self.to_dict() != other.to_dict()
