# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class ProcessRequest(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'tag': 'str',
        'process_param': 'ProcessParams',
        'list': 'list[ProcessRequestImage]',
        'live_portrait': 'str',
        'ext_portrait': 'str',
        'container_list': 'ContainerList',
        'system_info': 'ProcessSystemInfo',
        'pass_back_object': 'dict(str, object)'
    }

    attribute_map = {
        'tag': 'tag',
        'process_param': 'processParam',
        'list': 'List',
        'live_portrait': 'livePortrait',
        'ext_portrait': 'extPortrait',
        'container_list': 'ContainerList',
        'system_info': 'systemInfo',
        'pass_back_object': 'passBackObject'
    }

    def __init__(self, tag=None, process_param=None, list=None, live_portrait=None, ext_portrait=None, container_list=None, system_info=None, pass_back_object=None, local_vars_configuration=None):  # noqa: E501
        """ProcessRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag = None
        self._process_param = None
        self._list = None
        self._live_portrait = None
        self._ext_portrait = None
        self._container_list = None
        self._system_info = None
        self._pass_back_object = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        self.process_param = process_param
        if list is not None:
            self.list = list
        if live_portrait is not None:
            self.live_portrait = live_portrait
        if ext_portrait is not None:
            self.ext_portrait = ext_portrait
        if container_list is not None:
            self.container_list = container_list
        if system_info is not None:
            self.system_info = system_info
        if pass_back_object is not None:
            self.pass_back_object = pass_back_object

    @property
    def tag(self):
        """Gets the tag of this ProcessRequest.  # noqa: E501

        session id  # noqa: E501

        :return: The tag of this ProcessRequest.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ProcessRequest.

        session id  # noqa: E501

        :param tag: The tag of this ProcessRequest.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def process_param(self):
        """Gets the process_param of this ProcessRequest.  # noqa: E501


        :return: The process_param of this ProcessRequest.  # noqa: E501
        :rtype: ProcessParams
        """
        return self._process_param

    @process_param.setter
    def process_param(self, process_param):
        """Sets the process_param of this ProcessRequest.


        :param process_param: The process_param of this ProcessRequest.  # noqa: E501
        :type process_param: ProcessParams
        """
        if self.local_vars_configuration.client_side_validation and process_param is None:  # noqa: E501
            raise ValueError("Invalid value for `process_param`, must not be `None`")  # noqa: E501

        self._process_param = process_param

    @property
    def list(self):
        """Gets the list of this ProcessRequest.  # noqa: E501


        :return: The list of this ProcessRequest.  # noqa: E501
        :rtype: list[ProcessRequestImage]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ProcessRequest.


        :param list: The list of this ProcessRequest.  # noqa: E501
        :type list: list[ProcessRequestImage]
        """

        self._list = list

    @property
    def live_portrait(self):
        """Gets the live_portrait of this ProcessRequest.  # noqa: E501

        Live portrait photo  # noqa: E501

        :return: The live_portrait of this ProcessRequest.  # noqa: E501
        :rtype: str
        """
        return self._live_portrait

    @live_portrait.setter
    def live_portrait(self, live_portrait):
        """Sets the live_portrait of this ProcessRequest.

        Live portrait photo  # noqa: E501

        :param live_portrait: The live_portrait of this ProcessRequest.  # noqa: E501
        :type live_portrait: str
        """

        self._live_portrait = live_portrait

    @property
    def ext_portrait(self):
        """Gets the ext_portrait of this ProcessRequest.  # noqa: E501

        Portrait photo from an external source  # noqa: E501

        :return: The ext_portrait of this ProcessRequest.  # noqa: E501
        :rtype: str
        """
        return self._ext_portrait

    @ext_portrait.setter
    def ext_portrait(self, ext_portrait):
        """Sets the ext_portrait of this ProcessRequest.

        Portrait photo from an external source  # noqa: E501

        :param ext_portrait: The ext_portrait of this ProcessRequest.  # noqa: E501
        :type ext_portrait: str
        """

        self._ext_portrait = ext_portrait

    @property
    def container_list(self):
        """Gets the container_list of this ProcessRequest.  # noqa: E501


        :return: The container_list of this ProcessRequest.  # noqa: E501
        :rtype: ContainerList
        """
        return self._container_list

    @container_list.setter
    def container_list(self, container_list):
        """Sets the container_list of this ProcessRequest.


        :param container_list: The container_list of this ProcessRequest.  # noqa: E501
        :type container_list: ContainerList
        """

        self._container_list = container_list

    @property
    def system_info(self):
        """Gets the system_info of this ProcessRequest.  # noqa: E501


        :return: The system_info of this ProcessRequest.  # noqa: E501
        :rtype: ProcessSystemInfo
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this ProcessRequest.


        :param system_info: The system_info of this ProcessRequest.  # noqa: E501
        :type system_info: ProcessSystemInfo
        """

        self._system_info = system_info

    @property
    def pass_back_object(self):
        """Gets the pass_back_object of this ProcessRequest.  # noqa: E501

        Free-form object to be included in response. Must be object, not list or simple value. Do not affect document processing. Use it freely to pass your app params. Stored in process logs.  # noqa: E501

        :return: The pass_back_object of this ProcessRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._pass_back_object

    @pass_back_object.setter
    def pass_back_object(self, pass_back_object):
        """Sets the pass_back_object of this ProcessRequest.

        Free-form object to be included in response. Must be object, not list or simple value. Do not affect document processing. Use it freely to pass your app params. Stored in process logs.  # noqa: E501

        :param pass_back_object: The pass_back_object of this ProcessRequest.  # noqa: E501
        :type pass_back_object: dict(str, object)
        """

        self._pass_back_object = pass_back_object

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
        if not isinstance(other, ProcessRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessRequest):
            return True

        return self.to_dict() != other.to_dict()
