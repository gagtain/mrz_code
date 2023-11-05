# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class TransactionInfo(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'computer_name': 'str',
        'date_time': 'str',
        'transaction_id': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'computer_name': 'ComputerName',
        'date_time': 'DateTime',
        'transaction_id': 'TransactionID',
        'user_name': 'UserName'
    }

    def __init__(self, computer_name=None, date_time=None, transaction_id=None, user_name=None, local_vars_configuration=None):  # noqa: E501
        """TransactionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._computer_name = None
        self._date_time = None
        self._transaction_id = None
        self._user_name = None
        self.discriminator = None

        if computer_name is not None:
            self.computer_name = computer_name
        if date_time is not None:
            self.date_time = date_time
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def computer_name(self):
        """Gets the computer_name of this TransactionInfo.  # noqa: E501


        :return: The computer_name of this TransactionInfo.  # noqa: E501
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this TransactionInfo.


        :param computer_name: The computer_name of this TransactionInfo.  # noqa: E501
        :type computer_name: str
        """

        self._computer_name = computer_name

    @property
    def date_time(self):
        """Gets the date_time of this TransactionInfo.  # noqa: E501


        :return: The date_time of this TransactionInfo.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this TransactionInfo.


        :param date_time: The date_time of this TransactionInfo.  # noqa: E501
        :type date_time: str
        """

        self._date_time = date_time

    @property
    def transaction_id(self):
        """Gets the transaction_id of this TransactionInfo.  # noqa: E501


        :return: The transaction_id of this TransactionInfo.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this TransactionInfo.


        :param transaction_id: The transaction_id of this TransactionInfo.  # noqa: E501
        :type transaction_id: str
        """

        self._transaction_id = transaction_id

    @property
    def user_name(self):
        """Gets the user_name of this TransactionInfo.  # noqa: E501


        :return: The user_name of this TransactionInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TransactionInfo.


        :param user_name: The user_name of this TransactionInfo.  # noqa: E501
        :type user_name: str
        """

        self._user_name = user_name

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
        if not isinstance(other, TransactionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionInfo):
            return True

        return self.to_dict() != other.to_dict()
