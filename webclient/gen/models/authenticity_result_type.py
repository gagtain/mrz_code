# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


class AuthenticityResultType(object):
    
    

    UV_LUMINESCENCE = int("1")

    IR_B900 = int("2")

    IMAGE_PATTERN = int("4")

    AXIAL_PROTECTION = int("8")

    UV_FIBERS = int("16")

    IR_VISIBILITY = int("32")

    OCR_SECURITY_TEXT = int("64")

    IPI = int("128")

    PHOTO_EMBED_TYPE = int("512")

    OVI = int("1024")

    HOLOGRAMS = int("4096")

    PHOTO_AREA = int("8192")

    PORTRAIT_COMPARISON = int("32768")

    BARCODE_FORMAT_CHECK = int("65536")

    KINEGRAM = int("131072")

    LETTER_SCREEN = int("262144")

    HOLOGRAM_DETECTION = int("524288")

    FINGERPRINT_COMPARISON = int("1048576")

    LIVENESS = int("2097152")

    EXTENDED_OCR_CHECK = int("4194304")

    EXTENDED_MRZ_CHECK = int("8388608")

    allowable_values = [UV_LUMINESCENCE, IR_B900, IMAGE_PATTERN, AXIAL_PROTECTION, UV_FIBERS, IR_VISIBILITY, OCR_SECURITY_TEXT, IPI, PHOTO_EMBED_TYPE, OVI, HOLOGRAMS, PHOTO_AREA, PORTRAIT_COMPARISON, BARCODE_FORMAT_CHECK, KINEGRAM, LETTER_SCREEN, HOLOGRAM_DETECTION, FINGERPRINT_COMPARISON, LIVENESS, EXTENDED_OCR_CHECK, EXTENDED_MRZ_CHECK]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """AuthenticityResultType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, AuthenticityResultType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticityResultType):
            return True

        return self.to_dict() != other.to_dict()
