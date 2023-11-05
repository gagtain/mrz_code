# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class VerifiedFieldMap(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'w_field_type': 'TextFieldType',
        'w_lcid': 'LCID',
        'field_mrz': 'str',
        'field_visual': 'str',
        'field_barcode': 'str',
        'field_rfid': 'str',
        'matrix': 'list[VerificationResult]'
    }

    attribute_map = {
        'w_field_type': 'wFieldType',
        'w_lcid': 'wLCID',
        'field_mrz': 'Field_MRZ',
        'field_visual': 'Field_Visual',
        'field_barcode': 'Field_Barcode',
        'field_rfid': 'Field_RFID',
        'matrix': 'Matrix'
    }

    def __init__(self, w_field_type=None, w_lcid=None, field_mrz=None, field_visual=None, field_barcode=None, field_rfid=None, matrix=None, local_vars_configuration=None):  # noqa: E501
        """VerifiedFieldMap - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._w_field_type = None
        self._w_lcid = None
        self._field_mrz = None
        self._field_visual = None
        self._field_barcode = None
        self._field_rfid = None
        self._matrix = None
        self.discriminator = None

        if w_field_type is not None:
            self.w_field_type = w_field_type
        if w_lcid is not None:
            self.w_lcid = w_lcid
        if field_mrz is not None:
            self.field_mrz = field_mrz
        if field_visual is not None:
            self.field_visual = field_visual
        if field_barcode is not None:
            self.field_barcode = field_barcode
        if field_rfid is not None:
            self.field_rfid = field_rfid
        if matrix is not None:
            self.matrix = matrix

    @property
    def w_field_type(self):
        """Gets the w_field_type of this VerifiedFieldMap.  # noqa: E501


        :return: The w_field_type of this VerifiedFieldMap.  # noqa: E501
        :rtype: TextFieldType
        """
        return self._w_field_type

    @w_field_type.setter
    def w_field_type(self, w_field_type):
        """Sets the w_field_type of this VerifiedFieldMap.


        :param w_field_type: The w_field_type of this VerifiedFieldMap.  # noqa: E501
        :type w_field_type: TextFieldType
        """

        self._w_field_type = w_field_type

    @property
    def w_lcid(self):
        """Gets the w_lcid of this VerifiedFieldMap.  # noqa: E501


        :return: The w_lcid of this VerifiedFieldMap.  # noqa: E501
        :rtype: LCID
        """
        return self._w_lcid

    @w_lcid.setter
    def w_lcid(self, w_lcid):
        """Sets the w_lcid of this VerifiedFieldMap.


        :param w_lcid: The w_lcid of this VerifiedFieldMap.  # noqa: E501
        :type w_lcid: LCID
        """

        self._w_lcid = w_lcid

    @property
    def field_mrz(self):
        """Gets the field_mrz of this VerifiedFieldMap.  # noqa: E501

        Field data extracted from mrz(machine readable zone)  # noqa: E501

        :return: The field_mrz of this VerifiedFieldMap.  # noqa: E501
        :rtype: str
        """
        return self._field_mrz

    @field_mrz.setter
    def field_mrz(self, field_mrz):
        """Sets the field_mrz of this VerifiedFieldMap.

        Field data extracted from mrz(machine readable zone)  # noqa: E501

        :param field_mrz: The field_mrz of this VerifiedFieldMap.  # noqa: E501
        :type field_mrz: str
        """

        self._field_mrz = field_mrz

    @property
    def field_visual(self):
        """Gets the field_visual of this VerifiedFieldMap.  # noqa: E501

        Field data extracted from visual zone  # noqa: E501

        :return: The field_visual of this VerifiedFieldMap.  # noqa: E501
        :rtype: str
        """
        return self._field_visual

    @field_visual.setter
    def field_visual(self, field_visual):
        """Sets the field_visual of this VerifiedFieldMap.

        Field data extracted from visual zone  # noqa: E501

        :param field_visual: The field_visual of this VerifiedFieldMap.  # noqa: E501
        :type field_visual: str
        """

        self._field_visual = field_visual

    @property
    def field_barcode(self):
        """Gets the field_barcode of this VerifiedFieldMap.  # noqa: E501

        Field data extracted from barcode  # noqa: E501

        :return: The field_barcode of this VerifiedFieldMap.  # noqa: E501
        :rtype: str
        """
        return self._field_barcode

    @field_barcode.setter
    def field_barcode(self, field_barcode):
        """Sets the field_barcode of this VerifiedFieldMap.

        Field data extracted from barcode  # noqa: E501

        :param field_barcode: The field_barcode of this VerifiedFieldMap.  # noqa: E501
        :type field_barcode: str
        """

        self._field_barcode = field_barcode

    @property
    def field_rfid(self):
        """Gets the field_rfid of this VerifiedFieldMap.  # noqa: E501

        Field data extracted from rfid chip  # noqa: E501

        :return: The field_rfid of this VerifiedFieldMap.  # noqa: E501
        :rtype: str
        """
        return self._field_rfid

    @field_rfid.setter
    def field_rfid(self, field_rfid):
        """Sets the field_rfid of this VerifiedFieldMap.

        Field data extracted from rfid chip  # noqa: E501

        :param field_rfid: The field_rfid of this VerifiedFieldMap.  # noqa: E501
        :type field_rfid: str
        """

        self._field_rfid = field_rfid

    @property
    def matrix(self):
        """Gets the matrix of this VerifiedFieldMap.  # noqa: E501

        results comparison matrix. Elements of the matrix with indices 0, 1, 2, 3 take one of the values Disabled(0), Verified(1) or Not_Verified(2), elements with indices 4, 5, 6, 7, 8 are one of the values Disabled(0), Compare_Match(3) or Compare_Not_Match(4). Elements of the Matrix matrix have the following semantic meaning: - element with index 0 –– the result of verification of data from the MRZ; - 1 –– the result of verification of data from the RFID microcircuit; - 2 –– the result of verification of data from text areas of the document; - 3 –– the result of verification data from barcodes; - 4 - the result of comparing MRZ data and RFID microcircuits; - 5 - the result of comparing MRZ data and text areas of document filling; - 6 - the result of comparing MRZ data and bar codes; - 7 - the result of comparing the data of text areas of the document and the RFID chip; - 8 - the result of comparing the data of the text areas of the document and barcodes; - 9 - the result of comparing the data of the RFID chip and barcodes.  # noqa: E501

        :return: The matrix of this VerifiedFieldMap.  # noqa: E501
        :rtype: list[VerificationResult]
        """
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        """Sets the matrix of this VerifiedFieldMap.

        results comparison matrix. Elements of the matrix with indices 0, 1, 2, 3 take one of the values Disabled(0), Verified(1) or Not_Verified(2), elements with indices 4, 5, 6, 7, 8 are one of the values Disabled(0), Compare_Match(3) or Compare_Not_Match(4). Elements of the Matrix matrix have the following semantic meaning: - element with index 0 –– the result of verification of data from the MRZ; - 1 –– the result of verification of data from the RFID microcircuit; - 2 –– the result of verification of data from text areas of the document; - 3 –– the result of verification data from barcodes; - 4 - the result of comparing MRZ data and RFID microcircuits; - 5 - the result of comparing MRZ data and text areas of document filling; - 6 - the result of comparing MRZ data and bar codes; - 7 - the result of comparing the data of text areas of the document and the RFID chip; - 8 - the result of comparing the data of the text areas of the document and barcodes; - 9 - the result of comparing the data of the RFID chip and barcodes.  # noqa: E501

        :param matrix: The matrix of this VerifiedFieldMap.  # noqa: E501
        :type matrix: list[VerificationResult]
        """

        self._matrix = matrix

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
        if not isinstance(other, VerifiedFieldMap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerifiedFieldMap):
            return True

        return self.to_dict() != other.to_dict()
