# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class OCRSecurityTextResult(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'int',
        'element_result': 'CheckResult',
        'element_diagnose': 'CheckDiagnose',
        'critical_flag': 'Critical',
        'light_type': 'Light',
        'field_rect': 'RectangleCoordinates',
        'etalon_result_type': 'int',
        'etalon_field_type': 'int',
        'etalon_light_type': 'int',
        'security_text_result_ocr': 'str',
        'etalon_result_ocr': 'str',
        'reserved1': 'int',
        'reserved2': 'int'
    }

    attribute_map = {
        'type': 'Type',
        'element_result': 'ElementResult',
        'element_diagnose': 'ElementDiagnose',
        'critical_flag': 'CriticalFlag',
        'light_type': 'LightType',
        'field_rect': 'FieldRect',
        'etalon_result_type': 'EtalonResultType',
        'etalon_field_type': 'EtalonFieldType',
        'etalon_light_type': 'EtalonLightType',
        'security_text_result_ocr': 'SecurityTextResultOCR',
        'etalon_result_ocr': 'EtalonResultOCR',
        'reserved1': 'Reserved1',
        'reserved2': 'Reserved2'
    }

    def __init__(self, type=0, element_result=None, element_diagnose=None, critical_flag=None, light_type=None, field_rect=None, etalon_result_type=None, etalon_field_type=None, etalon_light_type=None, security_text_result_ocr=None, etalon_result_ocr=None, reserved1=None, reserved2=None, local_vars_configuration=None):  # noqa: E501
        """OCRSecurityTextResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._element_result = None
        self._element_diagnose = None
        self._critical_flag = None
        self._light_type = None
        self._field_rect = None
        self._etalon_result_type = None
        self._etalon_field_type = None
        self._etalon_light_type = None
        self._security_text_result_ocr = None
        self._etalon_result_ocr = None
        self._reserved1 = None
        self._reserved2 = None
        self.discriminator = None

        self.type = type
        if element_result is not None:
            self.element_result = element_result
        if element_diagnose is not None:
            self.element_diagnose = element_diagnose
        if critical_flag is not None:
            self.critical_flag = critical_flag
        if light_type is not None:
            self.light_type = light_type
        if field_rect is not None:
            self.field_rect = field_rect
        if etalon_result_type is not None:
            self.etalon_result_type = etalon_result_type
        if etalon_field_type is not None:
            self.etalon_field_type = etalon_field_type
        if etalon_light_type is not None:
            self.etalon_light_type = etalon_light_type
        if security_text_result_ocr is not None:
            self.security_text_result_ocr = security_text_result_ocr
        if etalon_result_ocr is not None:
            self.etalon_result_ocr = etalon_result_ocr
        if reserved1 is not None:
            self.reserved1 = reserved1
        if reserved2 is not None:
            self.reserved2 = reserved2

    @property
    def type(self):
        """Gets the type of this OCRSecurityTextResult.  # noqa: E501

        Same as authenticity result type, but used for safe parsing of not-described values: https://docs.webclientforensics.com/develop/doc-reader-sdk/web-service/development/enums/authenticity-result-type/  # noqa: E501

        :return: The type of this OCRSecurityTextResult.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OCRSecurityTextResult.

        Same as authenticity result type, but used for safe parsing of not-described values: https://docs.webclientforensics.com/develop/doc-reader-sdk/web-service/development/enums/authenticity-result-type/  # noqa: E501

        :param type: The type of this OCRSecurityTextResult.  # noqa: E501
        :type type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def element_result(self):
        """Gets the element_result of this OCRSecurityTextResult.  # noqa: E501


        :return: The element_result of this OCRSecurityTextResult.  # noqa: E501
        :rtype: CheckResult
        """
        return self._element_result

    @element_result.setter
    def element_result(self, element_result):
        """Sets the element_result of this OCRSecurityTextResult.


        :param element_result: The element_result of this OCRSecurityTextResult.  # noqa: E501
        :type element_result: CheckResult
        """

        self._element_result = element_result

    @property
    def element_diagnose(self):
        """Gets the element_diagnose of this OCRSecurityTextResult.  # noqa: E501


        :return: The element_diagnose of this OCRSecurityTextResult.  # noqa: E501
        :rtype: CheckDiagnose
        """
        return self._element_diagnose

    @element_diagnose.setter
    def element_diagnose(self, element_diagnose):
        """Sets the element_diagnose of this OCRSecurityTextResult.


        :param element_diagnose: The element_diagnose of this OCRSecurityTextResult.  # noqa: E501
        :type element_diagnose: CheckDiagnose
        """

        self._element_diagnose = element_diagnose

    @property
    def critical_flag(self):
        """Gets the critical_flag of this OCRSecurityTextResult.  # noqa: E501


        :return: The critical_flag of this OCRSecurityTextResult.  # noqa: E501
        :rtype: Critical
        """
        return self._critical_flag

    @critical_flag.setter
    def critical_flag(self, critical_flag):
        """Sets the critical_flag of this OCRSecurityTextResult.


        :param critical_flag: The critical_flag of this OCRSecurityTextResult.  # noqa: E501
        :type critical_flag: Critical
        """

        self._critical_flag = critical_flag

    @property
    def light_type(self):
        """Gets the light_type of this OCRSecurityTextResult.  # noqa: E501


        :return: The light_type of this OCRSecurityTextResult.  # noqa: E501
        :rtype: Light
        """
        return self._light_type

    @light_type.setter
    def light_type(self, light_type):
        """Sets the light_type of this OCRSecurityTextResult.


        :param light_type: The light_type of this OCRSecurityTextResult.  # noqa: E501
        :type light_type: Light
        """

        self._light_type = light_type

    @property
    def field_rect(self):
        """Gets the field_rect of this OCRSecurityTextResult.  # noqa: E501


        :return: The field_rect of this OCRSecurityTextResult.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._field_rect

    @field_rect.setter
    def field_rect(self, field_rect):
        """Sets the field_rect of this OCRSecurityTextResult.


        :param field_rect: The field_rect of this OCRSecurityTextResult.  # noqa: E501
        :type field_rect: RectangleCoordinates
        """

        self._field_rect = field_rect

    @property
    def etalon_result_type(self):
        """Gets the etalon_result_type of this OCRSecurityTextResult.  # noqa: E501


        :return: The etalon_result_type of this OCRSecurityTextResult.  # noqa: E501
        :rtype: int
        """
        return self._etalon_result_type

    @etalon_result_type.setter
    def etalon_result_type(self, etalon_result_type):
        """Sets the etalon_result_type of this OCRSecurityTextResult.


        :param etalon_result_type: The etalon_result_type of this OCRSecurityTextResult.  # noqa: E501
        :type etalon_result_type: int
        """

        self._etalon_result_type = etalon_result_type

    @property
    def etalon_field_type(self):
        """Gets the etalon_field_type of this OCRSecurityTextResult.  # noqa: E501


        :return: The etalon_field_type of this OCRSecurityTextResult.  # noqa: E501
        :rtype: int
        """
        return self._etalon_field_type

    @etalon_field_type.setter
    def etalon_field_type(self, etalon_field_type):
        """Sets the etalon_field_type of this OCRSecurityTextResult.


        :param etalon_field_type: The etalon_field_type of this OCRSecurityTextResult.  # noqa: E501
        :type etalon_field_type: int
        """

        self._etalon_field_type = etalon_field_type

    @property
    def etalon_light_type(self):
        """Gets the etalon_light_type of this OCRSecurityTextResult.  # noqa: E501


        :return: The etalon_light_type of this OCRSecurityTextResult.  # noqa: E501
        :rtype: int
        """
        return self._etalon_light_type

    @etalon_light_type.setter
    def etalon_light_type(self, etalon_light_type):
        """Sets the etalon_light_type of this OCRSecurityTextResult.


        :param etalon_light_type: The etalon_light_type of this OCRSecurityTextResult.  # noqa: E501
        :type etalon_light_type: int
        """

        self._etalon_light_type = etalon_light_type

    @property
    def security_text_result_ocr(self):
        """Gets the security_text_result_ocr of this OCRSecurityTextResult.  # noqa: E501


        :return: The security_text_result_ocr of this OCRSecurityTextResult.  # noqa: E501
        :rtype: str
        """
        return self._security_text_result_ocr

    @security_text_result_ocr.setter
    def security_text_result_ocr(self, security_text_result_ocr):
        """Sets the security_text_result_ocr of this OCRSecurityTextResult.


        :param security_text_result_ocr: The security_text_result_ocr of this OCRSecurityTextResult.  # noqa: E501
        :type security_text_result_ocr: str
        """

        self._security_text_result_ocr = security_text_result_ocr

    @property
    def etalon_result_ocr(self):
        """Gets the etalon_result_ocr of this OCRSecurityTextResult.  # noqa: E501


        :return: The etalon_result_ocr of this OCRSecurityTextResult.  # noqa: E501
        :rtype: str
        """
        return self._etalon_result_ocr

    @etalon_result_ocr.setter
    def etalon_result_ocr(self, etalon_result_ocr):
        """Sets the etalon_result_ocr of this OCRSecurityTextResult.


        :param etalon_result_ocr: The etalon_result_ocr of this OCRSecurityTextResult.  # noqa: E501
        :type etalon_result_ocr: str
        """

        self._etalon_result_ocr = etalon_result_ocr

    @property
    def reserved1(self):
        """Gets the reserved1 of this OCRSecurityTextResult.  # noqa: E501


        :return: The reserved1 of this OCRSecurityTextResult.  # noqa: E501
        :rtype: int
        """
        return self._reserved1

    @reserved1.setter
    def reserved1(self, reserved1):
        """Sets the reserved1 of this OCRSecurityTextResult.


        :param reserved1: The reserved1 of this OCRSecurityTextResult.  # noqa: E501
        :type reserved1: int
        """

        self._reserved1 = reserved1

    @property
    def reserved2(self):
        """Gets the reserved2 of this OCRSecurityTextResult.  # noqa: E501


        :return: The reserved2 of this OCRSecurityTextResult.  # noqa: E501
        :rtype: int
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """Sets the reserved2 of this OCRSecurityTextResult.


        :param reserved2: The reserved2 of this OCRSecurityTextResult.  # noqa: E501
        :type reserved2: int
        """

        self._reserved2 = reserved2

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
        if not isinstance(other, OCRSecurityTextResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OCRSecurityTextResult):
            return True

        return self.to_dict() != other.to_dict()
