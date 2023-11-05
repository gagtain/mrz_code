# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""
A search filter that can be applied if the &quot;match+search&quot; mode is enabled. May include limit, threshold, group_ids. If the group_ids are specified, the search is performed only in these groups. Find more information in the &lt;a href&#x3D;&quot;https://dev.webclientforensics.com/FaceSDK-web-openapi/#tag/search/operation/search&quot; target&#x3D;&quot;_blank&quot;&gt;OpenAPI documentation&lt;/a&gt;.
"""
class FaceApiSearch(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'limit': 'int',
        'threshold': 'float',
        'group_ids': 'list[int]'
    }

    attribute_map = {
        'limit': 'limit',
        'threshold': 'threshold',
        'group_ids': 'group_ids'
    }

    def __init__(self, limit=None, threshold=None, group_ids=None, local_vars_configuration=None):  # noqa: E501
        """FaceApiSearch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._limit = None
        self._threshold = None
        self._group_ids = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if threshold is not None:
            self.threshold = threshold
        if group_ids is not None:
            self.group_ids = group_ids

    @property
    def limit(self):
        """Gets the limit of this FaceApiSearch.  # noqa: E501

        The maximum number of results to be returned.  # noqa: E501

        :return: The limit of this FaceApiSearch.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this FaceApiSearch.

        The maximum number of results to be returned.  # noqa: E501

        :param limit: The limit of this FaceApiSearch.  # noqa: E501
        :type limit: int
        """

        self._limit = limit

    @property
    def threshold(self):
        """Gets the threshold of this FaceApiSearch.  # noqa: E501

        The similarity threshold.  # noqa: E501

        :return: The threshold of this FaceApiSearch.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this FaceApiSearch.

        The similarity threshold.  # noqa: E501

        :param threshold: The threshold of this FaceApiSearch.  # noqa: E501
        :type threshold: float
        """

        self._threshold = threshold

    @property
    def group_ids(self):
        """Gets the group_ids of this FaceApiSearch.  # noqa: E501

         The groups where to conduct the search.  # noqa: E501

        :return: The group_ids of this FaceApiSearch.  # noqa: E501
        :rtype: list[int]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this FaceApiSearch.

         The groups where to conduct the search.  # noqa: E501

        :param group_ids: The group_ids of this FaceApiSearch.  # noqa: E501
        :type group_ids: list[int]
        """

        self._group_ids = group_ids

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
        if not isinstance(other, FaceApiSearch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FaceApiSearch):
            return True

        return self.to_dict() != other.to_dict()
