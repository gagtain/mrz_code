# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""
Extended document type info and webclient&#39;s &#39;Information Reference Systems&#39; links
"""
class FDSIDList(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'icao_code': 'str',
        'list': 'list[int]',
        'd_type': 'DocumentType',
        'd_format': 'DocumentFormat',
        'd_mrz': 'bool',
        'd_description': 'str',
        'd_year': 'str',
        'd_country_name': 'str',
        'd_state_code': 'str',
        'd_state_name': 'str'
    }

    attribute_map = {
        'icao_code': 'ICAOCode',
        'list': 'List',
        'd_type': 'dType',
        'd_format': 'dFormat',
        'd_mrz': 'dMRZ',
        'd_description': 'dDescription',
        'd_year': 'dYear',
        'd_country_name': 'dCountryName',
        'd_state_code': 'dStateCode',
        'd_state_name': 'dStateName'
    }

    def __init__(self, icao_code=None, list=None, d_type=None, d_format=None, d_mrz=None, d_description=None, d_year=None, d_country_name=None, d_state_code=None, d_state_name=None, local_vars_configuration=None):  # noqa: E501
        """FDSIDList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._icao_code = None
        self._list = None
        self._d_type = None
        self._d_format = None
        self._d_mrz = None
        self._d_description = None
        self._d_year = None
        self._d_country_name = None
        self._d_state_code = None
        self._d_state_name = None
        self.discriminator = None

        if icao_code is not None:
            self.icao_code = icao_code
        if list is not None:
            self.list = list
        if d_type is not None:
            self.d_type = d_type
        if d_format is not None:
            self.d_format = d_format
        if d_mrz is not None:
            self.d_mrz = d_mrz
        if d_description is not None:
            self.d_description = d_description
        if d_year is not None:
            self.d_year = d_year
        if d_country_name is not None:
            self.d_country_name = d_country_name
        if d_state_code is not None:
            self.d_state_code = d_state_code
        if d_state_name is not None:
            self.d_state_name = d_state_name

    @property
    def icao_code(self):
        """Gets the icao_code of this FDSIDList.  # noqa: E501

        ICAO code of the issuing country  # noqa: E501

        :return: The icao_code of this FDSIDList.  # noqa: E501
        :rtype: str
        """
        return self._icao_code

    @icao_code.setter
    def icao_code(self, icao_code):
        """Sets the icao_code of this FDSIDList.

        ICAO code of the issuing country  # noqa: E501

        :param icao_code: The icao_code of this FDSIDList.  # noqa: E501
        :type icao_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                icao_code is not None and len(icao_code) > 3):
            raise ValueError("Invalid value for `icao_code`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                icao_code is not None and len(icao_code) < 3):
            raise ValueError("Invalid value for `icao_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._icao_code = icao_code

    @property
    def list(self):
        """Gets the list of this FDSIDList.  # noqa: E501

        Document identifiers in 'Information Reference Systems'  # noqa: E501

        :return: The list of this FDSIDList.  # noqa: E501
        :rtype: list[int]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this FDSIDList.

        Document identifiers in 'Information Reference Systems'  # noqa: E501

        :param list: The list of this FDSIDList.  # noqa: E501
        :type list: list[int]
        """

        self._list = list

    @property
    def d_type(self):
        """Gets the d_type of this FDSIDList.  # noqa: E501


        :return: The d_type of this FDSIDList.  # noqa: E501
        :rtype: DocumentType
        """
        return self._d_type

    @d_type.setter
    def d_type(self, d_type):
        """Sets the d_type of this FDSIDList.


        :param d_type: The d_type of this FDSIDList.  # noqa: E501
        :type d_type: DocumentType
        """

        self._d_type = d_type

    @property
    def d_format(self):
        """Gets the d_format of this FDSIDList.  # noqa: E501


        :return: The d_format of this FDSIDList.  # noqa: E501
        :rtype: DocumentFormat
        """
        return self._d_format

    @d_format.setter
    def d_format(self, d_format):
        """Sets the d_format of this FDSIDList.


        :param d_format: The d_format of this FDSIDList.  # noqa: E501
        :type d_format: DocumentFormat
        """

        self._d_format = d_format

    @property
    def d_mrz(self):
        """Gets the d_mrz of this FDSIDList.  # noqa: E501

        Flag indicating the presence of MRZ on the document  # noqa: E501

        :return: The d_mrz of this FDSIDList.  # noqa: E501
        :rtype: bool
        """
        return self._d_mrz

    @d_mrz.setter
    def d_mrz(self, d_mrz):
        """Sets the d_mrz of this FDSIDList.

        Flag indicating the presence of MRZ on the document  # noqa: E501

        :param d_mrz: The d_mrz of this FDSIDList.  # noqa: E501
        :type d_mrz: bool
        """

        self._d_mrz = d_mrz

    @property
    def d_description(self):
        """Gets the d_description of this FDSIDList.  # noqa: E501

        Document description  # noqa: E501

        :return: The d_description of this FDSIDList.  # noqa: E501
        :rtype: str
        """
        return self._d_description

    @d_description.setter
    def d_description(self, d_description):
        """Sets the d_description of this FDSIDList.

        Document description  # noqa: E501

        :param d_description: The d_description of this FDSIDList.  # noqa: E501
        :type d_description: str
        """

        self._d_description = d_description

    @property
    def d_year(self):
        """Gets the d_year of this FDSIDList.  # noqa: E501

        Year of publication of the document  # noqa: E501

        :return: The d_year of this FDSIDList.  # noqa: E501
        :rtype: str
        """
        return self._d_year

    @d_year.setter
    def d_year(self, d_year):
        """Sets the d_year of this FDSIDList.

        Year of publication of the document  # noqa: E501

        :param d_year: The d_year of this FDSIDList.  # noqa: E501
        :type d_year: str
        """

        self._d_year = d_year

    @property
    def d_country_name(self):
        """Gets the d_country_name of this FDSIDList.  # noqa: E501

        Issuing country name  # noqa: E501

        :return: The d_country_name of this FDSIDList.  # noqa: E501
        :rtype: str
        """
        return self._d_country_name

    @d_country_name.setter
    def d_country_name(self, d_country_name):
        """Sets the d_country_name of this FDSIDList.

        Issuing country name  # noqa: E501

        :param d_country_name: The d_country_name of this FDSIDList.  # noqa: E501
        :type d_country_name: str
        """

        self._d_country_name = d_country_name

    @property
    def d_state_code(self):
        """Gets the d_state_code of this FDSIDList.  # noqa: E501

        Issuing state code  # noqa: E501

        :return: The d_state_code of this FDSIDList.  # noqa: E501
        :rtype: str
        """
        return self._d_state_code

    @d_state_code.setter
    def d_state_code(self, d_state_code):
        """Sets the d_state_code of this FDSIDList.

        Issuing state code  # noqa: E501

        :param d_state_code: The d_state_code of this FDSIDList.  # noqa: E501
        :type d_state_code: str
        """

        self._d_state_code = d_state_code

    @property
    def d_state_name(self):
        """Gets the d_state_name of this FDSIDList.  # noqa: E501

        Issuing state name  # noqa: E501

        :return: The d_state_name of this FDSIDList.  # noqa: E501
        :rtype: str
        """
        return self._d_state_name

    @d_state_name.setter
    def d_state_name(self, d_state_name):
        """Sets the d_state_name of this FDSIDList.

        Issuing state name  # noqa: E501

        :param d_state_name: The d_state_name of this FDSIDList.  # noqa: E501
        :type d_state_name: str
        """

        self._d_state_name = d_state_name

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
        if not isinstance(other, FDSIDList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FDSIDList):
            return True

        return self.to_dict() != other.to_dict()
