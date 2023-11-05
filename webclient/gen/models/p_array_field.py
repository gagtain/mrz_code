# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class PArrayField(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bc_angle_detect': 'float',
        'bc_code_result': 'int',
        'bc_count_module': 'int',
        'bc_data_module': 'list[DataModule]',
        'bc_pdf417_info': 'BcPDF417INFO',
        'bc_roi_detect': 'BcROIDETECT',
        'bc_text_decoder_types': 'int',
        'bc_text_field_type': 'int',
        'bc_type_decode': 'int',
        'bc_type_detect': 'int'
    }

    attribute_map = {
        'bc_angle_detect': 'bcAngle_DETECT',
        'bc_code_result': 'bcCodeResult',
        'bc_count_module': 'bcCountModule',
        'bc_data_module': 'bcDataModule',
        'bc_pdf417_info': 'bcPDF417INFO',
        'bc_roi_detect': 'bcROI_DETECT',
        'bc_text_decoder_types': 'bcTextDecoderTypes',
        'bc_text_field_type': 'bcTextFieldType',
        'bc_type_decode': 'bcType_DECODE',
        'bc_type_detect': 'bcType_DETECT'
    }

    def __init__(self, bc_angle_detect=None, bc_code_result=None, bc_count_module=None, bc_data_module=None, bc_pdf417_info=None, bc_roi_detect=None, bc_text_decoder_types=None, bc_text_field_type=None, bc_type_decode=None, bc_type_detect=None, local_vars_configuration=None):  # noqa: E501
        """PArrayField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bc_angle_detect = None
        self._bc_code_result = None
        self._bc_count_module = None
        self._bc_data_module = None
        self._bc_pdf417_info = None
        self._bc_roi_detect = None
        self._bc_text_decoder_types = None
        self._bc_text_field_type = None
        self._bc_type_decode = None
        self._bc_type_detect = None
        self.discriminator = None

        if bc_angle_detect is not None:
            self.bc_angle_detect = bc_angle_detect
        if bc_code_result is not None:
            self.bc_code_result = bc_code_result
        if bc_count_module is not None:
            self.bc_count_module = bc_count_module
        if bc_data_module is not None:
            self.bc_data_module = bc_data_module
        if bc_pdf417_info is not None:
            self.bc_pdf417_info = bc_pdf417_info
        if bc_roi_detect is not None:
            self.bc_roi_detect = bc_roi_detect
        if bc_text_decoder_types is not None:
            self.bc_text_decoder_types = bc_text_decoder_types
        if bc_text_field_type is not None:
            self.bc_text_field_type = bc_text_field_type
        if bc_type_decode is not None:
            self.bc_type_decode = bc_type_decode
        if bc_type_detect is not None:
            self.bc_type_detect = bc_type_detect

    @property
    def bc_angle_detect(self):
        """Gets the bc_angle_detect of this PArrayField.  # noqa: E501


        :return: The bc_angle_detect of this PArrayField.  # noqa: E501
        :rtype: float
        """
        return self._bc_angle_detect

    @bc_angle_detect.setter
    def bc_angle_detect(self, bc_angle_detect):
        """Sets the bc_angle_detect of this PArrayField.


        :param bc_angle_detect: The bc_angle_detect of this PArrayField.  # noqa: E501
        :type bc_angle_detect: float
        """

        self._bc_angle_detect = bc_angle_detect

    @property
    def bc_code_result(self):
        """Gets the bc_code_result of this PArrayField.  # noqa: E501


        :return: The bc_code_result of this PArrayField.  # noqa: E501
        :rtype: int
        """
        return self._bc_code_result

    @bc_code_result.setter
    def bc_code_result(self, bc_code_result):
        """Sets the bc_code_result of this PArrayField.


        :param bc_code_result: The bc_code_result of this PArrayField.  # noqa: E501
        :type bc_code_result: int
        """

        self._bc_code_result = bc_code_result

    @property
    def bc_count_module(self):
        """Gets the bc_count_module of this PArrayField.  # noqa: E501


        :return: The bc_count_module of this PArrayField.  # noqa: E501
        :rtype: int
        """
        return self._bc_count_module

    @bc_count_module.setter
    def bc_count_module(self, bc_count_module):
        """Sets the bc_count_module of this PArrayField.


        :param bc_count_module: The bc_count_module of this PArrayField.  # noqa: E501
        :type bc_count_module: int
        """

        self._bc_count_module = bc_count_module

    @property
    def bc_data_module(self):
        """Gets the bc_data_module of this PArrayField.  # noqa: E501


        :return: The bc_data_module of this PArrayField.  # noqa: E501
        :rtype: list[DataModule]
        """
        return self._bc_data_module

    @bc_data_module.setter
    def bc_data_module(self, bc_data_module):
        """Sets the bc_data_module of this PArrayField.


        :param bc_data_module: The bc_data_module of this PArrayField.  # noqa: E501
        :type bc_data_module: list[DataModule]
        """

        self._bc_data_module = bc_data_module

    @property
    def bc_pdf417_info(self):
        """Gets the bc_pdf417_info of this PArrayField.  # noqa: E501


        :return: The bc_pdf417_info of this PArrayField.  # noqa: E501
        :rtype: BcPDF417INFO
        """
        return self._bc_pdf417_info

    @bc_pdf417_info.setter
    def bc_pdf417_info(self, bc_pdf417_info):
        """Sets the bc_pdf417_info of this PArrayField.


        :param bc_pdf417_info: The bc_pdf417_info of this PArrayField.  # noqa: E501
        :type bc_pdf417_info: BcPDF417INFO
        """

        self._bc_pdf417_info = bc_pdf417_info

    @property
    def bc_roi_detect(self):
        """Gets the bc_roi_detect of this PArrayField.  # noqa: E501


        :return: The bc_roi_detect of this PArrayField.  # noqa: E501
        :rtype: BcROIDETECT
        """
        return self._bc_roi_detect

    @bc_roi_detect.setter
    def bc_roi_detect(self, bc_roi_detect):
        """Sets the bc_roi_detect of this PArrayField.


        :param bc_roi_detect: The bc_roi_detect of this PArrayField.  # noqa: E501
        :type bc_roi_detect: BcROIDETECT
        """

        self._bc_roi_detect = bc_roi_detect

    @property
    def bc_text_decoder_types(self):
        """Gets the bc_text_decoder_types of this PArrayField.  # noqa: E501


        :return: The bc_text_decoder_types of this PArrayField.  # noqa: E501
        :rtype: int
        """
        return self._bc_text_decoder_types

    @bc_text_decoder_types.setter
    def bc_text_decoder_types(self, bc_text_decoder_types):
        """Sets the bc_text_decoder_types of this PArrayField.


        :param bc_text_decoder_types: The bc_text_decoder_types of this PArrayField.  # noqa: E501
        :type bc_text_decoder_types: int
        """

        self._bc_text_decoder_types = bc_text_decoder_types

    @property
    def bc_text_field_type(self):
        """Gets the bc_text_field_type of this PArrayField.  # noqa: E501


        :return: The bc_text_field_type of this PArrayField.  # noqa: E501
        :rtype: int
        """
        return self._bc_text_field_type

    @bc_text_field_type.setter
    def bc_text_field_type(self, bc_text_field_type):
        """Sets the bc_text_field_type of this PArrayField.


        :param bc_text_field_type: The bc_text_field_type of this PArrayField.  # noqa: E501
        :type bc_text_field_type: int
        """

        self._bc_text_field_type = bc_text_field_type

    @property
    def bc_type_decode(self):
        """Gets the bc_type_decode of this PArrayField.  # noqa: E501


        :return: The bc_type_decode of this PArrayField.  # noqa: E501
        :rtype: int
        """
        return self._bc_type_decode

    @bc_type_decode.setter
    def bc_type_decode(self, bc_type_decode):
        """Sets the bc_type_decode of this PArrayField.


        :param bc_type_decode: The bc_type_decode of this PArrayField.  # noqa: E501
        :type bc_type_decode: int
        """

        self._bc_type_decode = bc_type_decode

    @property
    def bc_type_detect(self):
        """Gets the bc_type_detect of this PArrayField.  # noqa: E501


        :return: The bc_type_detect of this PArrayField.  # noqa: E501
        :rtype: int
        """
        return self._bc_type_detect

    @bc_type_detect.setter
    def bc_type_detect(self, bc_type_detect):
        """Sets the bc_type_detect of this PArrayField.


        :param bc_type_detect: The bc_type_detect of this PArrayField.  # noqa: E501
        :type bc_type_detect: int
        """

        self._bc_type_detect = bc_type_detect

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
        if not isinstance(other, PArrayField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PArrayField):
            return True

        return self.to_dict() != other.to_dict()
