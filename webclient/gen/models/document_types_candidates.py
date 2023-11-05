# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class DocumentTypesCandidates(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'rec_result': 'DocumentTypeRecognitionResult',
        'candidates': 'list[OneCandidate]'
    }

    attribute_map = {
        'rec_result': 'RecResult',
        'candidates': 'Candidates'
    }

    def __init__(self, rec_result=None, candidates=None, local_vars_configuration=None):  # noqa: E501
        """DocumentTypesCandidates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rec_result = None
        self._candidates = None
        self.discriminator = None

        if rec_result is not None:
            self.rec_result = rec_result
        if candidates is not None:
            self.candidates = candidates

    @property
    def rec_result(self):
        """Gets the rec_result of this DocumentTypesCandidates.  # noqa: E501


        :return: The rec_result of this DocumentTypesCandidates.  # noqa: E501
        :rtype: DocumentTypeRecognitionResult
        """
        return self._rec_result

    @rec_result.setter
    def rec_result(self, rec_result):
        """Sets the rec_result of this DocumentTypesCandidates.


        :param rec_result: The rec_result of this DocumentTypesCandidates.  # noqa: E501
        :type rec_result: DocumentTypeRecognitionResult
        """

        self._rec_result = rec_result

    @property
    def candidates(self):
        """Gets the candidates of this DocumentTypesCandidates.  # noqa: E501


        :return: The candidates of this DocumentTypesCandidates.  # noqa: E501
        :rtype: list[OneCandidate]
        """
        return self._candidates

    @candidates.setter
    def candidates(self, candidates):
        """Sets the candidates of this DocumentTypesCandidates.


        :param candidates: The candidates of this DocumentTypesCandidates.  # noqa: E501
        :type candidates: list[OneCandidate]
        """

        self._candidates = candidates

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
        if not isinstance(other, DocumentTypesCandidates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentTypesCandidates):
            return True

        return self.to_dict() != other.to_dict()
