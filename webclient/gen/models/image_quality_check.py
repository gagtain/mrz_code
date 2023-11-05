# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class ImageQualityCheck(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'ImageQualityCheckType',
        'result': 'CheckResult',
        'feature_type': 'SecurityFeatureType',
        'areas': 'AreaArray',
        'mean': 'float',
        'std_dev': 'float',
        'probability': 'int'
    }

    attribute_map = {
        'type': 'type',
        'result': 'result',
        'feature_type': 'featureType',
        'areas': 'areas',
        'mean': 'mean',
        'std_dev': 'std_dev',
        'probability': 'probability'
    }

    def __init__(self, type=None, result=None, feature_type=None, areas=None, mean=None, std_dev=None, probability=None, local_vars_configuration=None):  # noqa: E501
        """ImageQualityCheck - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._result = None
        self._feature_type = None
        self._areas = None
        self._mean = None
        self._std_dev = None
        self._probability = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if result is not None:
            self.result = result
        if feature_type is not None:
            self.feature_type = feature_type
        if areas is not None:
            self.areas = areas
        if mean is not None:
            self.mean = mean
        if std_dev is not None:
            self.std_dev = std_dev
        if probability is not None:
            self.probability = probability

    @property
    def type(self):
        """Gets the type of this ImageQualityCheck.  # noqa: E501


        :return: The type of this ImageQualityCheck.  # noqa: E501
        :rtype: ImageQualityCheckType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageQualityCheck.


        :param type: The type of this ImageQualityCheck.  # noqa: E501
        :type type: ImageQualityCheckType
        """

        self._type = type

    @property
    def result(self):
        """Gets the result of this ImageQualityCheck.  # noqa: E501


        :return: The result of this ImageQualityCheck.  # noqa: E501
        :rtype: CheckResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ImageQualityCheck.


        :param result: The result of this ImageQualityCheck.  # noqa: E501
        :type result: CheckResult
        """

        self._result = result

    @property
    def feature_type(self):
        """Gets the feature_type of this ImageQualityCheck.  # noqa: E501


        :return: The feature_type of this ImageQualityCheck.  # noqa: E501
        :rtype: SecurityFeatureType
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this ImageQualityCheck.


        :param feature_type: The feature_type of this ImageQualityCheck.  # noqa: E501
        :type feature_type: SecurityFeatureType
        """

        self._feature_type = feature_type

    @property
    def areas(self):
        """Gets the areas of this ImageQualityCheck.  # noqa: E501


        :return: The areas of this ImageQualityCheck.  # noqa: E501
        :rtype: AreaArray
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        """Sets the areas of this ImageQualityCheck.


        :param areas: The areas of this ImageQualityCheck.  # noqa: E501
        :type areas: AreaArray
        """

        self._areas = areas

    @property
    def mean(self):
        """Gets the mean of this ImageQualityCheck.  # noqa: E501


        :return: The mean of this ImageQualityCheck.  # noqa: E501
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this ImageQualityCheck.


        :param mean: The mean of this ImageQualityCheck.  # noqa: E501
        :type mean: float
        """

        self._mean = mean

    @property
    def std_dev(self):
        """Gets the std_dev of this ImageQualityCheck.  # noqa: E501


        :return: The std_dev of this ImageQualityCheck.  # noqa: E501
        :rtype: float
        """
        return self._std_dev

    @std_dev.setter
    def std_dev(self, std_dev):
        """Sets the std_dev of this ImageQualityCheck.


        :param std_dev: The std_dev of this ImageQualityCheck.  # noqa: E501
        :type std_dev: float
        """

        self._std_dev = std_dev

    @property
    def probability(self):
        """Gets the probability of this ImageQualityCheck.  # noqa: E501


        :return: The probability of this ImageQualityCheck.  # noqa: E501
        :rtype: int
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """Sets the probability of this ImageQualityCheck.


        :param probability: The probability of this ImageQualityCheck.  # noqa: E501
        :type probability: int
        """

        self._probability = probability

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
        if not isinstance(other, ImageQualityCheck):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageQualityCheck):
            return True

        return self.to_dict() != other.to_dict()
