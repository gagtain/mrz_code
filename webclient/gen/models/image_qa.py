# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class ImageQA(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'dpi_threshold': 'int',
        'angle_threshold': 'int',
        'focus_check': 'bool',
        'glares_check': 'bool',
        'colorness_check': 'bool',
        'moire_check': 'bool',
        'document_position_indent': 'int'
    }

    attribute_map = {
        'dpi_threshold': 'dpiThreshold',
        'angle_threshold': 'angleThreshold',
        'focus_check': 'focusCheck',
        'glares_check': 'glaresCheck',
        'colorness_check': 'colornessCheck',
        'moire_check': 'moireCheck',
        'document_position_indent': 'documentPositionIndent'
    }

    def __init__(self, dpi_threshold=None, angle_threshold=None, focus_check=None, glares_check=None, colorness_check=None, moire_check=None, document_position_indent=None, local_vars_configuration=None):  # noqa: E501
        """ImageQA - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dpi_threshold = None
        self._angle_threshold = None
        self._focus_check = None
        self._glares_check = None
        self._colorness_check = None
        self._moire_check = None
        self._document_position_indent = None
        self.discriminator = None

        if dpi_threshold is not None:
            self.dpi_threshold = dpi_threshold
        if angle_threshold is not None:
            self.angle_threshold = angle_threshold
        if focus_check is not None:
            self.focus_check = focus_check
        if glares_check is not None:
            self.glares_check = glares_check
        if colorness_check is not None:
            self.colorness_check = colorness_check
        if moire_check is not None:
            self.moire_check = moire_check
        if document_position_indent is not None:
            self.document_position_indent = document_position_indent

    @property
    def dpi_threshold(self):
        """Gets the dpi_threshold of this ImageQA.  # noqa: E501

        This parameter sets threshold for Image QA check of the presented document physical dpi. If actual document dpi is below this threshold, check will fail.  # noqa: E501

        :return: The dpi_threshold of this ImageQA.  # noqa: E501
        :rtype: int
        """
        return self._dpi_threshold

    @dpi_threshold.setter
    def dpi_threshold(self, dpi_threshold):
        """Sets the dpi_threshold of this ImageQA.

        This parameter sets threshold for Image QA check of the presented document physical dpi. If actual document dpi is below this threshold, check will fail.  # noqa: E501

        :param dpi_threshold: The dpi_threshold of this ImageQA.  # noqa: E501
        :type dpi_threshold: int
        """

        self._dpi_threshold = dpi_threshold

    @property
    def angle_threshold(self):
        """Gets the angle_threshold of this ImageQA.  # noqa: E501

        This parameter sets threshold for Image QA check of the presented document perspective angle in degrees. If actual document perspective angle is above this threshold, check will fail.  # noqa: E501

        :return: The angle_threshold of this ImageQA.  # noqa: E501
        :rtype: int
        """
        return self._angle_threshold

    @angle_threshold.setter
    def angle_threshold(self, angle_threshold):
        """Sets the angle_threshold of this ImageQA.

        This parameter sets threshold for Image QA check of the presented document perspective angle in degrees. If actual document perspective angle is above this threshold, check will fail.  # noqa: E501

        :param angle_threshold: The angle_threshold of this ImageQA.  # noqa: E501
        :type angle_threshold: int
        """

        self._angle_threshold = angle_threshold

    @property
    def focus_check(self):
        """Gets the focus_check of this ImageQA.  # noqa: E501

        This option enables focus check while performing image quality validation.  # noqa: E501

        :return: The focus_check of this ImageQA.  # noqa: E501
        :rtype: bool
        """
        return self._focus_check

    @focus_check.setter
    def focus_check(self, focus_check):
        """Sets the focus_check of this ImageQA.

        This option enables focus check while performing image quality validation.  # noqa: E501

        :param focus_check: The focus_check of this ImageQA.  # noqa: E501
        :type focus_check: bool
        """

        self._focus_check = focus_check

    @property
    def glares_check(self):
        """Gets the glares_check of this ImageQA.  # noqa: E501

        This option enables glares check while performing image quality validation.  # noqa: E501

        :return: The glares_check of this ImageQA.  # noqa: E501
        :rtype: bool
        """
        return self._glares_check

    @glares_check.setter
    def glares_check(self, glares_check):
        """Sets the glares_check of this ImageQA.

        This option enables glares check while performing image quality validation.  # noqa: E501

        :param glares_check: The glares_check of this ImageQA.  # noqa: E501
        :type glares_check: bool
        """

        self._glares_check = glares_check

    @property
    def colorness_check(self):
        """Gets the colorness_check of this ImageQA.  # noqa: E501

        This option enables colorness check while performing image quality validation.  # noqa: E501

        :return: The colorness_check of this ImageQA.  # noqa: E501
        :rtype: bool
        """
        return self._colorness_check

    @colorness_check.setter
    def colorness_check(self, colorness_check):
        """Sets the colorness_check of this ImageQA.

        This option enables colorness check while performing image quality validation.  # noqa: E501

        :param colorness_check: The colorness_check of this ImageQA.  # noqa: E501
        :type colorness_check: bool
        """

        self._colorness_check = colorness_check

    @property
    def moire_check(self):
        """Gets the moire_check of this ImageQA.  # noqa: E501

        This option enables screen capture (moire patterns) check while performing image quality validation.  # noqa: E501

        :return: The moire_check of this ImageQA.  # noqa: E501
        :rtype: bool
        """
        return self._moire_check

    @moire_check.setter
    def moire_check(self, moire_check):
        """Sets the moire_check of this ImageQA.

        This option enables screen capture (moire patterns) check while performing image quality validation.  # noqa: E501

        :param moire_check: The moire_check of this ImageQA.  # noqa: E501
        :type moire_check: bool
        """

        self._moire_check = moire_check

    @property
    def document_position_indent(self):
        """Gets the document_position_indent of this ImageQA.  # noqa: E501

        This parameter specifies the necessary margin. Default 0.  # noqa: E501

        :return: The document_position_indent of this ImageQA.  # noqa: E501
        :rtype: int
        """
        return self._document_position_indent

    @document_position_indent.setter
    def document_position_indent(self, document_position_indent):
        """Sets the document_position_indent of this ImageQA.

        This parameter specifies the necessary margin. Default 0.  # noqa: E501

        :param document_position_indent: The document_position_indent of this ImageQA.  # noqa: E501
        :type document_position_indent: int
        """

        self._document_position_indent = document_position_indent

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
        if not isinstance(other, ImageQA):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageQA):
            return True

        return self.to_dict() != other.to_dict()
