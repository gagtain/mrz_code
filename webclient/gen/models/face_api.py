# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class FaceApi(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'mode': 'str',
        'search': 'FaceApiSearch',
        'threshold': 'int',
        'service_timeout': 'int',
        'proxy': 'str',
        'proxy_userpwd': 'str',
        'proxy_type': 'int'
    }

    attribute_map = {
        'url': 'url',
        'mode': 'mode',
        'search': 'search',
        'threshold': 'threshold',
        'service_timeout': 'serviceTimeout',
        'proxy': 'proxy',
        'proxy_userpwd': 'proxy_userpwd',
        'proxy_type': 'proxy_type'
    }

    def __init__(self, url=None, mode=None, search=None, threshold=None, service_timeout=None, proxy=None, proxy_userpwd=None, proxy_type=None, local_vars_configuration=None):  # noqa: E501
        """FaceApi - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._mode = None
        self._search = None
        self._threshold = None
        self._service_timeout = None
        self._proxy = None
        self._proxy_userpwd = None
        self._proxy_type = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if mode is not None:
            self.mode = mode
        if search is not None:
            self.search = search
        if threshold is not None:
            self.threshold = threshold
        if service_timeout is not None:
            self.service_timeout = service_timeout
        if proxy is not None:
            self.proxy = proxy
        if proxy_userpwd is not None:
            self.proxy_userpwd = proxy_userpwd
        if proxy_type is not None:
            self.proxy_type = proxy_type

    @property
    def url(self):
        """Gets the url of this FaceApi.  # noqa: E501

        The URL of the webclient Face Web service to be used.  # noqa: E501

        :return: The url of this FaceApi.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FaceApi.

        The URL of the webclient Face Web service to be used.  # noqa: E501

        :param url: The url of this FaceApi.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def mode(self):
        """Gets the mode of this FaceApi.  # noqa: E501

        The processing mode: \"match\" or \"match+search\".  # noqa: E501

        :return: The mode of this FaceApi.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this FaceApi.

        The processing mode: \"match\" or \"match+search\".  # noqa: E501

        :param mode: The mode of this FaceApi.  # noqa: E501
        :type mode: str
        """

        self._mode = mode

    @property
    def search(self):
        """Gets the search of this FaceApi.  # noqa: E501


        :return: The search of this FaceApi.  # noqa: E501
        :rtype: FaceApiSearch
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this FaceApi.


        :param search: The search of this FaceApi.  # noqa: E501
        :type search: FaceApiSearch
        """

        self._search = search

    @property
    def threshold(self):
        """Gets the threshold of this FaceApi.  # noqa: E501

        The similarity threshold, 0-100. Above 75 means that the faces' similarity is verified, below 75 is not.  # noqa: E501

        :return: The threshold of this FaceApi.  # noqa: E501
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this FaceApi.

        The similarity threshold, 0-100. Above 75 means that the faces' similarity is verified, below 75 is not.  # noqa: E501

        :param threshold: The threshold of this FaceApi.  # noqa: E501
        :type threshold: int
        """

        self._threshold = threshold

    @property
    def service_timeout(self):
        """Gets the service_timeout of this FaceApi.  # noqa: E501

        The webclient Face Web service requests timeout, ms.  # noqa: E501

        :return: The service_timeout of this FaceApi.  # noqa: E501
        :rtype: int
        """
        return self._service_timeout

    @service_timeout.setter
    def service_timeout(self, service_timeout):
        """Sets the service_timeout of this FaceApi.

        The webclient Face Web service requests timeout, ms.  # noqa: E501

        :param service_timeout: The service_timeout of this FaceApi.  # noqa: E501
        :type service_timeout: int
        """

        self._service_timeout = service_timeout

    @property
    def proxy(self):
        """Gets the proxy of this FaceApi.  # noqa: E501

        Proxy to use, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXY.html\" target=\"_blank\">cURL standard</a>.  # noqa: E501

        :return: The proxy of this FaceApi.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this FaceApi.

        Proxy to use, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXY.html\" target=\"_blank\">cURL standard</a>.  # noqa: E501

        :param proxy: The proxy of this FaceApi.  # noqa: E501
        :type proxy: str
        """

        self._proxy = proxy

    @property
    def proxy_userpwd(self):
        """Gets the proxy_userpwd of this FaceApi.  # noqa: E501

        Username and password to use for proxy authentication, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXYUSERPWD.html\" target=\"_blank\">cURL standard</a>.  # noqa: E501

        :return: The proxy_userpwd of this FaceApi.  # noqa: E501
        :rtype: str
        """
        return self._proxy_userpwd

    @proxy_userpwd.setter
    def proxy_userpwd(self, proxy_userpwd):
        """Sets the proxy_userpwd of this FaceApi.

        Username and password to use for proxy authentication, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXYUSERPWD.html\" target=\"_blank\">cURL standard</a>.  # noqa: E501

        :param proxy_userpwd: The proxy_userpwd of this FaceApi.  # noqa: E501
        :type proxy_userpwd: str
        """

        self._proxy_userpwd = proxy_userpwd

    @property
    def proxy_type(self):
        """Gets the proxy_type of this FaceApi.  # noqa: E501

        Proxy protocol type, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXYTYPE.html\" target=\"_blank\">cURL standard</a>.  # noqa: E501

        :return: The proxy_type of this FaceApi.  # noqa: E501
        :rtype: int
        """
        return self._proxy_type

    @proxy_type.setter
    def proxy_type(self, proxy_type):
        """Sets the proxy_type of this FaceApi.

        Proxy protocol type, should be set according to the <a href=\"https://curl.se/libcurl/c/CURLOPT_PROXYTYPE.html\" target=\"_blank\">cURL standard</a>.  # noqa: E501

        :param proxy_type: The proxy_type of this FaceApi.  # noqa: E501
        :type proxy_type: int
        """

        self._proxy_type = proxy_type

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
        if not isinstance(other, FaceApi):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FaceApi):
            return True

        return self.to_dict() != other.to_dict()
