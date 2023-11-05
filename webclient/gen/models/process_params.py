# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""

"""
class ProcessParams(object):
    """webclient
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'one_shot_identification': 'bool',
        'use_face_api': 'bool',
        'face_api': 'FaceApi',
        'do_detect_can': 'bool',
        'image_output_max_height': 'int',
        'image_output_max_width': 'int',
        'scenario': 'Scenario',
        'result_type_output': 'list[Result]',
        'double_page_spread': 'bool',
        'generate_double_page_spread_image': 'bool',
        'field_types_filter': 'list[TextFieldType]',
        'date_format': 'str',
        'measure_system': 'MeasureSystem',
        'image_dpi_out_max': 'int',
        'already_cropped': 'bool',
        'custom_params': 'dict(str, object)',
        'config': 'list[PerDocumentConfig]',
        'log': 'bool',
        'log_level': 'LogLevel',
        'force_doc_id': 'int',
        'match_text_field_mask': 'bool',
        'fast_doc_detect': 'bool',
        'update_ocr_validity_by_glare': 'bool',
        'check_required_text_fields': 'bool',
        'return_cropped_barcode': 'bool',
        'image_qa': 'ImageQA',
        'respect_image_quality': 'bool',
        'force_doc_format': 'DocumentFormat',
        'no_graphics': 'bool',
        'document_area_min': 'float',
        'depersonalize_log': 'bool',
        'multi_doc_on_image': 'bool',
        'shift_expiry_date': 'int',
        'minimal_holder_age': 'int',
        'return_uncropped_image': 'bool',
        'mrz_formats_filter': 'list[MRZFormat]',
        'force_read_mrz_before_locate': 'bool',
        'parse_barcodes': 'bool',
        'convert_case': 'TextPostProcessing',
        'split_names': 'bool',
        'disable_perforation_ocr': 'bool',
        'document_group_filter': 'list[DocumentType]',
        'process_auth': 'int',
        'device_id': 'int',
        'device_type': 'int',
        'device_type_hex': 'str',
        'ignore_device_id_from_image': 'bool',
        'document_id_list': 'list[int]',
        'rfid': 'ProcessParamsRfid'
    }

    attribute_map = {
        'one_shot_identification': 'oneShotIdentification',
        'use_face_api': 'useFaceApi',
        'face_api': 'faceApi',
        'do_detect_can': 'doDetectCan',
        'image_output_max_height': 'imageOutputMaxHeight',
        'image_output_max_width': 'imageOutputMaxWidth',
        'scenario': 'scenario',
        'result_type_output': 'resultTypeOutput',
        'double_page_spread': 'doublePageSpread',
        'generate_double_page_spread_image': 'generateDoublePageSpreadImage',
        'field_types_filter': 'fieldTypesFilter',
        'date_format': 'dateFormat',
        'measure_system': 'measureSystem',
        'image_dpi_out_max': 'imageDpiOutMax',
        'already_cropped': 'alreadyCropped',
        'custom_params': 'customParams',
        'config': 'config',
        'log': 'log',
        'log_level': 'logLevel',
        'force_doc_id': 'forceDocID',
        'match_text_field_mask': 'matchTextFieldMask',
        'fast_doc_detect': 'fastDocDetect',
        'update_ocr_validity_by_glare': 'updateOCRValidityByGlare',
        'check_required_text_fields': 'checkRequiredTextFields',
        'return_cropped_barcode': 'returnCroppedBarcode',
        'image_qa': 'imageQa',
        'respect_image_quality': 'respectImageQuality',
        'force_doc_format': 'forceDocFormat',
        'no_graphics': 'noGraphics',
        'document_area_min': 'documentAreaMin',
        'depersonalize_log': 'depersonalizeLog',
        'multi_doc_on_image': 'multiDocOnImage',
        'shift_expiry_date': 'shiftExpiryDate',
        'minimal_holder_age': 'minimalHolderAge',
        'return_uncropped_image': 'returnUncroppedImage',
        'mrz_formats_filter': 'mrzFormatsFilter',
        'force_read_mrz_before_locate': 'forceReadMrzBeforeLocate',
        'parse_barcodes': 'parseBarcodes',
        'convert_case': 'convertCase',
        'split_names': 'splitNames',
        'disable_perforation_ocr': 'disablePerforationOCR',
        'document_group_filter': 'documentGroupFilter',
        'process_auth': 'processAuth',
        'device_id': 'deviceId',
        'device_type': 'deviceType',
        'device_type_hex': 'deviceTypeHex',
        'ignore_device_id_from_image': 'ignoreDeviceIdFromImage',
        'document_id_list': 'documentIdList',
        'rfid': 'rfid'
    }

    def __init__(self, one_shot_identification=None, use_face_api=None, face_api=None, do_detect_can=None, image_output_max_height=None, image_output_max_width=None, scenario=None, result_type_output=None, double_page_spread=None, generate_double_page_spread_image=None, field_types_filter=None, date_format=None, measure_system=None, image_dpi_out_max=None, already_cropped=None, custom_params=None, config=None, log=None, log_level=None, force_doc_id=None, match_text_field_mask=None, fast_doc_detect=None, update_ocr_validity_by_glare=None, check_required_text_fields=None, return_cropped_barcode=None, image_qa=None, respect_image_quality=None, force_doc_format=None, no_graphics=None, document_area_min=None, depersonalize_log=None, multi_doc_on_image=None, shift_expiry_date=None, minimal_holder_age=None, return_uncropped_image=None, mrz_formats_filter=None, force_read_mrz_before_locate=None, parse_barcodes=None, convert_case=None, split_names=None, disable_perforation_ocr=None, document_group_filter=None, process_auth=None, device_id=None, device_type=None, device_type_hex=None, ignore_device_id_from_image=None, document_id_list=None, rfid=None, local_vars_configuration=None):  # noqa: E501
        """ProcessParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._one_shot_identification = None
        self._use_face_api = None
        self._face_api = None
        self._do_detect_can = None
        self._image_output_max_height = None
        self._image_output_max_width = None
        self._scenario = None
        self._result_type_output = None
        self._double_page_spread = None
        self._generate_double_page_spread_image = None
        self._field_types_filter = None
        self._date_format = None
        self._measure_system = None
        self._image_dpi_out_max = None
        self._already_cropped = None
        self._custom_params = None
        self._config = None
        self._log = None
        self._log_level = None
        self._force_doc_id = None
        self._match_text_field_mask = None
        self._fast_doc_detect = None
        self._update_ocr_validity_by_glare = None
        self._check_required_text_fields = None
        self._return_cropped_barcode = None
        self._image_qa = None
        self._respect_image_quality = None
        self._force_doc_format = None
        self._no_graphics = None
        self._document_area_min = None
        self._depersonalize_log = None
        self._multi_doc_on_image = None
        self._shift_expiry_date = None
        self._minimal_holder_age = None
        self._return_uncropped_image = None
        self._mrz_formats_filter = None
        self._force_read_mrz_before_locate = None
        self._parse_barcodes = None
        self._convert_case = None
        self._split_names = None
        self._disable_perforation_ocr = None
        self._document_group_filter = None
        self._process_auth = None
        self._device_id = None
        self._device_type = None
        self._device_type_hex = None
        self._ignore_device_id_from_image = None
        self._document_id_list = None
        self._rfid = None
        self.discriminator = None

        if one_shot_identification is not None:
            self.one_shot_identification = one_shot_identification
        if use_face_api is not None:
            self.use_face_api = use_face_api
        if face_api is not None:
            self.face_api = face_api
        if do_detect_can is not None:
            self.do_detect_can = do_detect_can
        if image_output_max_height is not None:
            self.image_output_max_height = image_output_max_height
        if image_output_max_width is not None:
            self.image_output_max_width = image_output_max_width
        self.scenario = scenario
        if result_type_output is not None:
            self.result_type_output = result_type_output
        if double_page_spread is not None:
            self.double_page_spread = double_page_spread
        if generate_double_page_spread_image is not None:
            self.generate_double_page_spread_image = generate_double_page_spread_image
        if field_types_filter is not None:
            self.field_types_filter = field_types_filter
        if date_format is not None:
            self.date_format = date_format
        if measure_system is not None:
            self.measure_system = measure_system
        if image_dpi_out_max is not None:
            self.image_dpi_out_max = image_dpi_out_max
        if already_cropped is not None:
            self.already_cropped = already_cropped
        if custom_params is not None:
            self.custom_params = custom_params
        if config is not None:
            self.config = config
        if log is not None:
            self.log = log
        if log_level is not None:
            self.log_level = log_level
        if force_doc_id is not None:
            self.force_doc_id = force_doc_id
        if match_text_field_mask is not None:
            self.match_text_field_mask = match_text_field_mask
        if fast_doc_detect is not None:
            self.fast_doc_detect = fast_doc_detect
        if update_ocr_validity_by_glare is not None:
            self.update_ocr_validity_by_glare = update_ocr_validity_by_glare
        if check_required_text_fields is not None:
            self.check_required_text_fields = check_required_text_fields
        if return_cropped_barcode is not None:
            self.return_cropped_barcode = return_cropped_barcode
        if image_qa is not None:
            self.image_qa = image_qa
        if respect_image_quality is not None:
            self.respect_image_quality = respect_image_quality
        if force_doc_format is not None:
            self.force_doc_format = force_doc_format
        if no_graphics is not None:
            self.no_graphics = no_graphics
        if document_area_min is not None:
            self.document_area_min = document_area_min
        if depersonalize_log is not None:
            self.depersonalize_log = depersonalize_log
        if multi_doc_on_image is not None:
            self.multi_doc_on_image = multi_doc_on_image
        if shift_expiry_date is not None:
            self.shift_expiry_date = shift_expiry_date
        if minimal_holder_age is not None:
            self.minimal_holder_age = minimal_holder_age
        if return_uncropped_image is not None:
            self.return_uncropped_image = return_uncropped_image
        if mrz_formats_filter is not None:
            self.mrz_formats_filter = mrz_formats_filter
        if force_read_mrz_before_locate is not None:
            self.force_read_mrz_before_locate = force_read_mrz_before_locate
        if parse_barcodes is not None:
            self.parse_barcodes = parse_barcodes
        if convert_case is not None:
            self.convert_case = convert_case
        if split_names is not None:
            self.split_names = split_names
        if disable_perforation_ocr is not None:
            self.disable_perforation_ocr = disable_perforation_ocr
        if document_group_filter is not None:
            self.document_group_filter = document_group_filter
        if process_auth is not None:
            self.process_auth = process_auth
        if device_id is not None:
            self.device_id = device_id
        if device_type is not None:
            self.device_type = device_type
        if device_type_hex is not None:
            self.device_type_hex = device_type_hex
        if ignore_device_id_from_image is not None:
            self.ignore_device_id_from_image = ignore_device_id_from_image
        if document_id_list is not None:
            self.document_id_list = document_id_list
        if rfid is not None:
            self.rfid = rfid

    @property
    def one_shot_identification(self):
        """Gets the one_shot_identification of this ProcessParams.  # noqa: E501

        This parameter allows processing an image that contains a person and a document and compare the portrait photo from the document with the person's face  # noqa: E501

        :return: The one_shot_identification of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._one_shot_identification

    @one_shot_identification.setter
    def one_shot_identification(self, one_shot_identification):
        """Sets the one_shot_identification of this ProcessParams.

        This parameter allows processing an image that contains a person and a document and compare the portrait photo from the document with the person's face  # noqa: E501

        :param one_shot_identification: The one_shot_identification of this ProcessParams.  # noqa: E501
        :type one_shot_identification: bool
        """

        self._one_shot_identification = one_shot_identification

    @property
    def use_face_api(self):
        """Gets the use_face_api of this ProcessParams.  # noqa: E501

        This parameter allows comparing faces on webclient Face Web Service  # noqa: E501

        :return: The use_face_api of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._use_face_api

    @use_face_api.setter
    def use_face_api(self, use_face_api):
        """Sets the use_face_api of this ProcessParams.

        This parameter allows comparing faces on webclient Face Web Service  # noqa: E501

        :param use_face_api: The use_face_api of this ProcessParams.  # noqa: E501
        :type use_face_api: bool
        """

        self._use_face_api = use_face_api

    @property
    def face_api(self):
        """Gets the face_api of this ProcessParams.  # noqa: E501


        :return: The face_api of this ProcessParams.  # noqa: E501
        :rtype: FaceApi
        """
        return self._face_api

    @face_api.setter
    def face_api(self, face_api):
        """Sets the face_api of this ProcessParams.


        :param face_api: The face_api of this ProcessParams.  # noqa: E501
        :type face_api: FaceApi
        """

        self._face_api = face_api

    @property
    def do_detect_can(self):
        """Gets the do_detect_can of this ProcessParams.  # noqa: E501

        This parameter allows enabling the CAN (Card Access Number) detection and recognition when using scenarios with document location and MRZ reading, such as the MrzAndLocate scenario.  # noqa: E501

        :return: The do_detect_can of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._do_detect_can

    @do_detect_can.setter
    def do_detect_can(self, do_detect_can):
        """Sets the do_detect_can of this ProcessParams.

        This parameter allows enabling the CAN (Card Access Number) detection and recognition when using scenarios with document location and MRZ reading, such as the MrzAndLocate scenario.  # noqa: E501

        :param do_detect_can: The do_detect_can of this ProcessParams.  # noqa: E501
        :type do_detect_can: bool
        """

        self._do_detect_can = do_detect_can

    @property
    def image_output_max_height(self):
        """Gets the image_output_max_height of this ProcessParams.  # noqa: E501

        This parameter allows setting maximum height in pixels of output images and thus reducing image size to desired. Does not change the aspect ratio. Changes disabled if equals to 0. Default 0.  # noqa: E501

        :return: The image_output_max_height of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._image_output_max_height

    @image_output_max_height.setter
    def image_output_max_height(self, image_output_max_height):
        """Sets the image_output_max_height of this ProcessParams.

        This parameter allows setting maximum height in pixels of output images and thus reducing image size to desired. Does not change the aspect ratio. Changes disabled if equals to 0. Default 0.  # noqa: E501

        :param image_output_max_height: The image_output_max_height of this ProcessParams.  # noqa: E501
        :type image_output_max_height: int
        """

        self._image_output_max_height = image_output_max_height

    @property
    def image_output_max_width(self):
        """Gets the image_output_max_width of this ProcessParams.  # noqa: E501

        This parameter allows setting maximum width in pixels of output images and thus reducing image size to desired. Does not change the aspect ratio. Changes disabled if equals to 0. Default 0.  # noqa: E501

        :return: The image_output_max_width of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._image_output_max_width

    @image_output_max_width.setter
    def image_output_max_width(self, image_output_max_width):
        """Sets the image_output_max_width of this ProcessParams.

        This parameter allows setting maximum width in pixels of output images and thus reducing image size to desired. Does not change the aspect ratio. Changes disabled if equals to 0. Default 0.  # noqa: E501

        :param image_output_max_width: The image_output_max_width of this ProcessParams.  # noqa: E501
        :type image_output_max_width: int
        """

        self._image_output_max_width = image_output_max_width

    @property
    def scenario(self):
        """Gets the scenario of this ProcessParams.  # noqa: E501


        :return: The scenario of this ProcessParams.  # noqa: E501
        :rtype: Scenario
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this ProcessParams.


        :param scenario: The scenario of this ProcessParams.  # noqa: E501
        :type scenario: Scenario
        """
        if self.local_vars_configuration.client_side_validation and scenario is None:  # noqa: E501
            raise ValueError("Invalid value for `scenario`, must not be `None`")  # noqa: E501

        self._scenario = scenario

    @property
    def result_type_output(self):
        """Gets the result_type_output of this ProcessParams.  # noqa: E501

        Types of results to return in response. See 'Result' enum for available options  # noqa: E501

        :return: The result_type_output of this ProcessParams.  # noqa: E501
        :rtype: list[Result]
        """
        return self._result_type_output

    @result_type_output.setter
    def result_type_output(self, result_type_output):
        """Sets the result_type_output of this ProcessParams.

        Types of results to return in response. See 'Result' enum for available options  # noqa: E501

        :param result_type_output: The result_type_output of this ProcessParams.  # noqa: E501
        :type result_type_output: list[Result]
        """

        self._result_type_output = result_type_output

    @property
    def double_page_spread(self):
        """Gets the double_page_spread of this ProcessParams.  # noqa: E501

        Enable this option if the image you provide contains double page spread of the passport and you want to process both pages in one go. It makes sense to use it for documents that have meaningful information on both pages, like Russian domestic passport, or some others. Disabled by default.  # noqa: E501

        :return: The double_page_spread of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._double_page_spread

    @double_page_spread.setter
    def double_page_spread(self, double_page_spread):
        """Sets the double_page_spread of this ProcessParams.

        Enable this option if the image you provide contains double page spread of the passport and you want to process both pages in one go. It makes sense to use it for documents that have meaningful information on both pages, like Russian domestic passport, or some others. Disabled by default.  # noqa: E501

        :param double_page_spread: The double_page_spread of this ProcessParams.  # noqa: E501
        :type double_page_spread: bool
        """

        self._double_page_spread = double_page_spread

    @property
    def generate_double_page_spread_image(self):
        """Gets the generate_double_page_spread_image of this ProcessParams.  # noqa: E501

        When enabled together with \"doublePageSpread\" and there is a passport with two pages spread in the image, pages will be cropped, straightened and aligned together, as if the document was captured on a flatbed scanner. Disabled by default.  # noqa: E501

        :return: The generate_double_page_spread_image of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._generate_double_page_spread_image

    @generate_double_page_spread_image.setter
    def generate_double_page_spread_image(self, generate_double_page_spread_image):
        """Sets the generate_double_page_spread_image of this ProcessParams.

        When enabled together with \"doublePageSpread\" and there is a passport with two pages spread in the image, pages will be cropped, straightened and aligned together, as if the document was captured on a flatbed scanner. Disabled by default.  # noqa: E501

        :param generate_double_page_spread_image: The generate_double_page_spread_image of this ProcessParams.  # noqa: E501
        :type generate_double_page_spread_image: bool
        """

        self._generate_double_page_spread_image = generate_double_page_spread_image

    @property
    def field_types_filter(self):
        """Gets the field_types_filter of this ProcessParams.  # noqa: E501

        List of text field types to extract. If empty, all text fields from template will be extracted. Narrowing the list can shorten processing time. Empty by default.  # noqa: E501

        :return: The field_types_filter of this ProcessParams.  # noqa: E501
        :rtype: list[TextFieldType]
        """
        return self._field_types_filter

    @field_types_filter.setter
    def field_types_filter(self, field_types_filter):
        """Sets the field_types_filter of this ProcessParams.

        List of text field types to extract. If empty, all text fields from template will be extracted. Narrowing the list can shorten processing time. Empty by default.  # noqa: E501

        :param field_types_filter: The field_types_filter of this ProcessParams.  # noqa: E501
        :type field_types_filter: list[TextFieldType]
        """

        self._field_types_filter = field_types_filter

    @property
    def date_format(self):
        """Gets the date_format of this ProcessParams.  # noqa: E501

        This option allows you to set dates format so that solution will return dates in this format. For example, if you supply 'MM/dd/yyyy', and document have printed date '09 JUL 2020' for the date os issue, you will get '07/09/2020' as a result. By default it is set to system locale default (where the service is running).  # noqa: E501

        :return: The date_format of this ProcessParams.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this ProcessParams.

        This option allows you to set dates format so that solution will return dates in this format. For example, if you supply 'MM/dd/yyyy', and document have printed date '09 JUL 2020' for the date os issue, you will get '07/09/2020' as a result. By default it is set to system locale default (where the service is running).  # noqa: E501

        :param date_format: The date_format of this ProcessParams.  # noqa: E501
        :type date_format: str
        """

        self._date_format = date_format

    @property
    def measure_system(self):
        """Gets the measure_system of this ProcessParams.  # noqa: E501


        :return: The measure_system of this ProcessParams.  # noqa: E501
        :rtype: MeasureSystem
        """
        return self._measure_system

    @measure_system.setter
    def measure_system(self, measure_system):
        """Sets the measure_system of this ProcessParams.


        :param measure_system: The measure_system of this ProcessParams.  # noqa: E501
        :type measure_system: MeasureSystem
        """

        self._measure_system = measure_system

    @property
    def image_dpi_out_max(self):
        """Gets the image_dpi_out_max of this ProcessParams.  # noqa: E501

        This parameter controls maximum resolution in dpi of output images. Resolution will remain original in case 0 is supplied. By default is set to return images in response with resolution not greater than 300 dpi for all scenarios except FullAuth. In FullAuth scenario this limit is 1000 dpi by default.  # noqa: E501

        :return: The image_dpi_out_max of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._image_dpi_out_max

    @image_dpi_out_max.setter
    def image_dpi_out_max(self, image_dpi_out_max):
        """Sets the image_dpi_out_max of this ProcessParams.

        This parameter controls maximum resolution in dpi of output images. Resolution will remain original in case 0 is supplied. By default is set to return images in response with resolution not greater than 300 dpi for all scenarios except FullAuth. In FullAuth scenario this limit is 1000 dpi by default.  # noqa: E501

        :param image_dpi_out_max: The image_dpi_out_max of this ProcessParams.  # noqa: E501
        :type image_dpi_out_max: int
        """

        self._image_dpi_out_max = image_dpi_out_max

    @property
    def already_cropped(self):
        """Gets the already_cropped of this ProcessParams.  # noqa: E501

        This option can be enabled if you know for sure that the image you provide contains already cropped document by its edges. This was designed to process on the server side images captured and cropped on mobile. Disabled by default.  # noqa: E501

        :return: The already_cropped of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._already_cropped

    @already_cropped.setter
    def already_cropped(self, already_cropped):
        """Sets the already_cropped of this ProcessParams.

        This option can be enabled if you know for sure that the image you provide contains already cropped document by its edges. This was designed to process on the server side images captured and cropped on mobile. Disabled by default.  # noqa: E501

        :param already_cropped: The already_cropped of this ProcessParams.  # noqa: E501
        :type already_cropped: bool
        """

        self._already_cropped = already_cropped

    @property
    def custom_params(self):
        """Gets the custom_params of this ProcessParams.  # noqa: E501

        This option allows passing custom processing parameters that can be implemented in future without changing API.  # noqa: E501

        :return: The custom_params of this ProcessParams.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_params

    @custom_params.setter
    def custom_params(self, custom_params):
        """Sets the custom_params of this ProcessParams.

        This option allows passing custom processing parameters that can be implemented in future without changing API.  # noqa: E501

        :param custom_params: The custom_params of this ProcessParams.  # noqa: E501
        :type custom_params: dict(str, object)
        """

        self._custom_params = custom_params

    @property
    def config(self):
        """Gets the config of this ProcessParams.  # noqa: E501

        This option allows setting additional custom configuration per document type. If recognized document has ID specified in config, processing adjusts according to designated configuration.  # noqa: E501

        :return: The config of this ProcessParams.  # noqa: E501
        :rtype: list[PerDocumentConfig]
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ProcessParams.

        This option allows setting additional custom configuration per document type. If recognized document has ID specified in config, processing adjusts according to designated configuration.  # noqa: E501

        :param config: The config of this ProcessParams.  # noqa: E501
        :type config: list[PerDocumentConfig]
        """

        self._config = config

    @property
    def log(self):
        """Gets the log of this ProcessParams.  # noqa: E501

        When enabled, results will contain transaction processing log. Disabled by default  # noqa: E501

        :return: The log of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this ProcessParams.

        When enabled, results will contain transaction processing log. Disabled by default  # noqa: E501

        :param log: The log of this ProcessParams.  # noqa: E501
        :type log: bool
        """

        self._log = log

    @property
    def log_level(self):
        """Gets the log_level of this ProcessParams.  # noqa: E501


        :return: The log_level of this ProcessParams.  # noqa: E501
        :rtype: LogLevel
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this ProcessParams.


        :param log_level: The log_level of this ProcessParams.  # noqa: E501
        :type log_level: LogLevel
        """

        self._log_level = log_level

    @property
    def force_doc_id(self):
        """Gets the force_doc_id of this ProcessParams.  # noqa: E501

        Force use of specific template ID and skip document type identification step.  # noqa: E501

        :return: The force_doc_id of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._force_doc_id

    @force_doc_id.setter
    def force_doc_id(self, force_doc_id):
        """Sets the force_doc_id of this ProcessParams.

        Force use of specific template ID and skip document type identification step.  # noqa: E501

        :param force_doc_id: The force_doc_id of this ProcessParams.  # noqa: E501
        :type force_doc_id: int
        """

        self._force_doc_id = force_doc_id

    @property
    def match_text_field_mask(self):
        """Gets the match_text_field_mask of this ProcessParams.  # noqa: E501

        When disabled, text field OCR will be done as is and then the recognized value will be matched to the field mask for validity. If enabled, we are trying to read a field value with maximum efforts to match the mask and provide a correctly formatted value, making assumptions based on the provided field mask in the template. Enabled by default.  # noqa: E501

        :return: The match_text_field_mask of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._match_text_field_mask

    @match_text_field_mask.setter
    def match_text_field_mask(self, match_text_field_mask):
        """Sets the match_text_field_mask of this ProcessParams.

        When disabled, text field OCR will be done as is and then the recognized value will be matched to the field mask for validity. If enabled, we are trying to read a field value with maximum efforts to match the mask and provide a correctly formatted value, making assumptions based on the provided field mask in the template. Enabled by default.  # noqa: E501

        :param match_text_field_mask: The match_text_field_mask of this ProcessParams.  # noqa: E501
        :type match_text_field_mask: bool
        """

        self._match_text_field_mask = match_text_field_mask

    @property
    def fast_doc_detect(self):
        """Gets the fast_doc_detect of this ProcessParams.  # noqa: E501

        When enabled, shorten the list of candidates to process during document detection in a single image process mode. Reduces processing time for specific backgrounds. Enabled by default.  # noqa: E501

        :return: The fast_doc_detect of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._fast_doc_detect

    @fast_doc_detect.setter
    def fast_doc_detect(self, fast_doc_detect):
        """Sets the fast_doc_detect of this ProcessParams.

        When enabled, shorten the list of candidates to process during document detection in a single image process mode. Reduces processing time for specific backgrounds. Enabled by default.  # noqa: E501

        :param fast_doc_detect: The fast_doc_detect of this ProcessParams.  # noqa: E501
        :type fast_doc_detect: bool
        """

        self._fast_doc_detect = fast_doc_detect

    @property
    def update_ocr_validity_by_glare(self):
        """Gets the update_ocr_validity_by_glare of this ProcessParams.  # noqa: E501

        When enabled, fail OCR field validity, if there is a glare over the text field on the image. Disabled by default.  # noqa: E501

        :return: The update_ocr_validity_by_glare of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._update_ocr_validity_by_glare

    @update_ocr_validity_by_glare.setter
    def update_ocr_validity_by_glare(self, update_ocr_validity_by_glare):
        """Sets the update_ocr_validity_by_glare of this ProcessParams.

        When enabled, fail OCR field validity, if there is a glare over the text field on the image. Disabled by default.  # noqa: E501

        :param update_ocr_validity_by_glare: The update_ocr_validity_by_glare of this ProcessParams.  # noqa: E501
        :type update_ocr_validity_by_glare: bool
        """

        self._update_ocr_validity_by_glare = update_ocr_validity_by_glare

    @property
    def check_required_text_fields(self):
        """Gets the check_required_text_fields of this ProcessParams.  # noqa: E501

        When enabled, each field in template will be checked for value presence and if the field is marked as required, but has no value, it will have 'error' in validity status. Disabled by default.  # noqa: E501

        :return: The check_required_text_fields of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._check_required_text_fields

    @check_required_text_fields.setter
    def check_required_text_fields(self, check_required_text_fields):
        """Sets the check_required_text_fields of this ProcessParams.

        When enabled, each field in template will be checked for value presence and if the field is marked as required, but has no value, it will have 'error' in validity status. Disabled by default.  # noqa: E501

        :param check_required_text_fields: The check_required_text_fields of this ProcessParams.  # noqa: E501
        :type check_required_text_fields: bool
        """

        self._check_required_text_fields = check_required_text_fields

    @property
    def return_cropped_barcode(self):
        """Gets the return_cropped_barcode of this ProcessParams.  # noqa: E501

        When enabled, returns cropped barcode images for unknown documents. Disabled by default.  # noqa: E501

        :return: The return_cropped_barcode of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._return_cropped_barcode

    @return_cropped_barcode.setter
    def return_cropped_barcode(self, return_cropped_barcode):
        """Sets the return_cropped_barcode of this ProcessParams.

        When enabled, returns cropped barcode images for unknown documents. Disabled by default.  # noqa: E501

        :param return_cropped_barcode: The return_cropped_barcode of this ProcessParams.  # noqa: E501
        :type return_cropped_barcode: bool
        """

        self._return_cropped_barcode = return_cropped_barcode

    @property
    def image_qa(self):
        """Gets the image_qa of this ProcessParams.  # noqa: E501


        :return: The image_qa of this ProcessParams.  # noqa: E501
        :rtype: ImageQA
        """
        return self._image_qa

    @image_qa.setter
    def image_qa(self, image_qa):
        """Sets the image_qa of this ProcessParams.


        :param image_qa: The image_qa of this ProcessParams.  # noqa: E501
        :type image_qa: ImageQA
        """

        self._image_qa = image_qa

    @property
    def respect_image_quality(self):
        """Gets the respect_image_quality of this ProcessParams.  # noqa: E501

        When enabled, image quality checks status affects document optical and overall status. Disabled by default.  # noqa: E501

        :return: The respect_image_quality of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._respect_image_quality

    @respect_image_quality.setter
    def respect_image_quality(self, respect_image_quality):
        """Sets the respect_image_quality of this ProcessParams.

        When enabled, image quality checks status affects document optical and overall status. Disabled by default.  # noqa: E501

        :param respect_image_quality: The respect_image_quality of this ProcessParams.  # noqa: E501
        :type respect_image_quality: bool
        """

        self._respect_image_quality = respect_image_quality

    @property
    def force_doc_format(self):
        """Gets the force_doc_format of this ProcessParams.  # noqa: E501


        :return: The force_doc_format of this ProcessParams.  # noqa: E501
        :rtype: DocumentFormat
        """
        return self._force_doc_format

    @force_doc_format.setter
    def force_doc_format(self, force_doc_format):
        """Sets the force_doc_format of this ProcessParams.


        :param force_doc_format: The force_doc_format of this ProcessParams.  # noqa: E501
        :type force_doc_format: DocumentFormat
        """

        self._force_doc_format = force_doc_format

    @property
    def no_graphics(self):
        """Gets the no_graphics of this ProcessParams.  # noqa: E501

        When enabled, no graphic fields will be cropped from document image. Disabled by default.  # noqa: E501

        :return: The no_graphics of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._no_graphics

    @no_graphics.setter
    def no_graphics(self, no_graphics):
        """Sets the no_graphics of this ProcessParams.

        When enabled, no graphic fields will be cropped from document image. Disabled by default.  # noqa: E501

        :param no_graphics: The no_graphics of this ProcessParams.  # noqa: E501
        :type no_graphics: bool
        """

        self._no_graphics = no_graphics

    @property
    def document_area_min(self):
        """Gets the document_area_min of this ProcessParams.  # noqa: E501

        Specifies minimal area of the image that document should cover to be treated as candidate when locating. Value should be in range from 0 to 1, where 1 is when document should fully cover the image.  # noqa: E501

        :return: The document_area_min of this ProcessParams.  # noqa: E501
        :rtype: float
        """
        return self._document_area_min

    @document_area_min.setter
    def document_area_min(self, document_area_min):
        """Sets the document_area_min of this ProcessParams.

        Specifies minimal area of the image that document should cover to be treated as candidate when locating. Value should be in range from 0 to 1, where 1 is when document should fully cover the image.  # noqa: E501

        :param document_area_min: The document_area_min of this ProcessParams.  # noqa: E501
        :type document_area_min: float
        """

        self._document_area_min = document_area_min

    @property
    def depersonalize_log(self):
        """Gets the depersonalize_log of this ProcessParams.  # noqa: E501

        When enabled, all personal data will be forcibly removed from the logs. Disabled by default.  # noqa: E501

        :return: The depersonalize_log of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._depersonalize_log

    @depersonalize_log.setter
    def depersonalize_log(self, depersonalize_log):
        """Sets the depersonalize_log of this ProcessParams.

        When enabled, all personal data will be forcibly removed from the logs. Disabled by default.  # noqa: E501

        :param depersonalize_log: The depersonalize_log of this ProcessParams.  # noqa: E501
        :type depersonalize_log: bool
        """

        self._depersonalize_log = depersonalize_log

    @property
    def multi_doc_on_image(self):
        """Gets the multi_doc_on_image of this ProcessParams.  # noqa: E501

        This option allows locating and cropping multiple documents from one image if enabled. Disabled by default.  # noqa: E501

        :return: The multi_doc_on_image of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._multi_doc_on_image

    @multi_doc_on_image.setter
    def multi_doc_on_image(self, multi_doc_on_image):
        """Sets the multi_doc_on_image of this ProcessParams.

        This option allows locating and cropping multiple documents from one image if enabled. Disabled by default.  # noqa: E501

        :param multi_doc_on_image: The multi_doc_on_image of this ProcessParams.  # noqa: E501
        :type multi_doc_on_image: bool
        """

        self._multi_doc_on_image = multi_doc_on_image

    @property
    def shift_expiry_date(self):
        """Gets the shift_expiry_date of this ProcessParams.  # noqa: E501

        This option allows shifting the date of expiry into the future or past for number of months specified. This is useful, for example, in some cases when document might be still valid for some period after original expiration date to prevent negative validity status for such documents. Or by shifting the date to the past will set negative validity for the documents that is about to expire in a specified number of months. 0 by default  # noqa: E501

        :return: The shift_expiry_date of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._shift_expiry_date

    @shift_expiry_date.setter
    def shift_expiry_date(self, shift_expiry_date):
        """Sets the shift_expiry_date of this ProcessParams.

        This option allows shifting the date of expiry into the future or past for number of months specified. This is useful, for example, in some cases when document might be still valid for some period after original expiration date to prevent negative validity status for such documents. Or by shifting the date to the past will set negative validity for the documents that is about to expire in a specified number of months. 0 by default  # noqa: E501

        :param shift_expiry_date: The shift_expiry_date of this ProcessParams.  # noqa: E501
        :type shift_expiry_date: int
        """

        self._shift_expiry_date = shift_expiry_date

    @property
    def minimal_holder_age(self):
        """Gets the minimal_holder_age of this ProcessParams.  # noqa: E501

        This options allows specifying the minimal age in years of the document holder for the document to be considered valid.  # noqa: E501

        :return: The minimal_holder_age of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._minimal_holder_age

    @minimal_holder_age.setter
    def minimal_holder_age(self, minimal_holder_age):
        """Sets the minimal_holder_age of this ProcessParams.

        This options allows specifying the minimal age in years of the document holder for the document to be considered valid.  # noqa: E501

        :param minimal_holder_age: The minimal_holder_age of this ProcessParams.  # noqa: E501
        :type minimal_holder_age: int
        """

        self._minimal_holder_age = minimal_holder_age

    @property
    def return_uncropped_image(self):
        """Gets the return_uncropped_image of this ProcessParams.  # noqa: E501

        When enabled, returns input images in output. Disabled by default.  # noqa: E501

        :return: The return_uncropped_image of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._return_uncropped_image

    @return_uncropped_image.setter
    def return_uncropped_image(self, return_uncropped_image):
        """Sets the return_uncropped_image of this ProcessParams.

        When enabled, returns input images in output. Disabled by default.  # noqa: E501

        :param return_uncropped_image: The return_uncropped_image of this ProcessParams.  # noqa: E501
        :type return_uncropped_image: bool
        """

        self._return_uncropped_image = return_uncropped_image

    @property
    def mrz_formats_filter(self):
        """Gets the mrz_formats_filter of this ProcessParams.  # noqa: E501

        This option allows limiting MRZ formats to be recognized by specifying them in array.  # noqa: E501

        :return: The mrz_formats_filter of this ProcessParams.  # noqa: E501
        :rtype: list[MRZFormat]
        """
        return self._mrz_formats_filter

    @mrz_formats_filter.setter
    def mrz_formats_filter(self, mrz_formats_filter):
        """Sets the mrz_formats_filter of this ProcessParams.

        This option allows limiting MRZ formats to be recognized by specifying them in array.  # noqa: E501

        :param mrz_formats_filter: The mrz_formats_filter of this ProcessParams.  # noqa: E501
        :type mrz_formats_filter: list[MRZFormat]
        """

        self._mrz_formats_filter = mrz_formats_filter

    @property
    def force_read_mrz_before_locate(self):
        """Gets the force_read_mrz_before_locate of this ProcessParams.  # noqa: E501

        When enabled, make sure that in series processing MRZ is located fully inside the result document image, if present on the document. Enabling this option may add extra processing time, by disabling optimizations, but allows more stability in output image quality. Disabled by default.  # noqa: E501

        :return: The force_read_mrz_before_locate of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._force_read_mrz_before_locate

    @force_read_mrz_before_locate.setter
    def force_read_mrz_before_locate(self, force_read_mrz_before_locate):
        """Sets the force_read_mrz_before_locate of this ProcessParams.

        When enabled, make sure that in series processing MRZ is located fully inside the result document image, if present on the document. Enabling this option may add extra processing time, by disabling optimizations, but allows more stability in output image quality. Disabled by default.  # noqa: E501

        :param force_read_mrz_before_locate: The force_read_mrz_before_locate of this ProcessParams.  # noqa: E501
        :type force_read_mrz_before_locate: bool
        """

        self._force_read_mrz_before_locate = force_read_mrz_before_locate

    @property
    def parse_barcodes(self):
        """Gets the parse_barcodes of this ProcessParams.  # noqa: E501

        This option can be disabled to stop parsing after barcode is read. Enabled by default.  # noqa: E501

        :return: The parse_barcodes of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._parse_barcodes

    @parse_barcodes.setter
    def parse_barcodes(self, parse_barcodes):
        """Sets the parse_barcodes of this ProcessParams.

        This option can be disabled to stop parsing after barcode is read. Enabled by default.  # noqa: E501

        :param parse_barcodes: The parse_barcodes of this ProcessParams.  # noqa: E501
        :type parse_barcodes: bool
        """

        self._parse_barcodes = parse_barcodes

    @property
    def convert_case(self):
        """Gets the convert_case of this ProcessParams.  # noqa: E501


        :return: The convert_case of this ProcessParams.  # noqa: E501
        :rtype: TextPostProcessing
        """
        return self._convert_case

    @convert_case.setter
    def convert_case(self, convert_case):
        """Sets the convert_case of this ProcessParams.


        :param convert_case: The convert_case of this ProcessParams.  # noqa: E501
        :type convert_case: TextPostProcessing
        """

        self._convert_case = convert_case

    @property
    def split_names(self):
        """Gets the split_names of this ProcessParams.  # noqa: E501

        When enabled, the Surname and GivenNames field will be divided into ft_First_Name, ft_Second_Name, ft_Third_Name, ft_Fourth_Name, ft_Last_Name fields. Disabled by default.  # noqa: E501

        :return: The split_names of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._split_names

    @split_names.setter
    def split_names(self, split_names):
        """Sets the split_names of this ProcessParams.

        When enabled, the Surname and GivenNames field will be divided into ft_First_Name, ft_Second_Name, ft_Third_Name, ft_Fourth_Name, ft_Last_Name fields. Disabled by default.  # noqa: E501

        :param split_names: The split_names of this ProcessParams.  # noqa: E501
        :type split_names: bool
        """

        self._split_names = split_names

    @property
    def disable_perforation_ocr(self):
        """Gets the disable_perforation_ocr of this ProcessParams.  # noqa: E501

        When enabled, OCR of perforated fields in the document template will not be performed. Disabled by default.  # noqa: E501

        :return: The disable_perforation_ocr of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._disable_perforation_ocr

    @disable_perforation_ocr.setter
    def disable_perforation_ocr(self, disable_perforation_ocr):
        """Sets the disable_perforation_ocr of this ProcessParams.

        When enabled, OCR of perforated fields in the document template will not be performed. Disabled by default.  # noqa: E501

        :param disable_perforation_ocr: The disable_perforation_ocr of this ProcessParams.  # noqa: E501
        :type disable_perforation_ocr: bool
        """

        self._disable_perforation_ocr = disable_perforation_ocr

    @property
    def document_group_filter(self):
        """Gets the document_group_filter of this ProcessParams.  # noqa: E501

        List of specific eligible document types from DocumentType enum to recognize from. You may, for example, specify only passports to be recognized by setting this property. Empty by default.  # noqa: E501

        :return: The document_group_filter of this ProcessParams.  # noqa: E501
        :rtype: list[DocumentType]
        """
        return self._document_group_filter

    @document_group_filter.setter
    def document_group_filter(self, document_group_filter):
        """Sets the document_group_filter of this ProcessParams.

        List of specific eligible document types from DocumentType enum to recognize from. You may, for example, specify only passports to be recognized by setting this property. Empty by default.  # noqa: E501

        :param document_group_filter: The document_group_filter of this ProcessParams.  # noqa: E501
        :type document_group_filter: list[DocumentType]
        """

        self._document_group_filter = document_group_filter

    @property
    def process_auth(self):
        """Gets the process_auth of this ProcessParams.  # noqa: E501

        Authenticity checks that should be performed regardless of the document type. The available checks are listed in the eRPRM_Authenticity enum. Note that only supported by your license checks can be added.   # noqa: E501

        :return: The process_auth of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._process_auth

    @process_auth.setter
    def process_auth(self, process_auth):
        """Sets the process_auth of this ProcessParams.

        Authenticity checks that should be performed regardless of the document type. The available checks are listed in the eRPRM_Authenticity enum. Note that only supported by your license checks can be added.   # noqa: E501

        :param process_auth: The process_auth of this ProcessParams.  # noqa: E501
        :type process_auth: int
        """

        self._process_auth = process_auth

    @property
    def device_id(self):
        """Gets the device_id of this ProcessParams.  # noqa: E501

        This parameter is used to specify the document reader device type from which input images were captured. Default 0.  # noqa: E501

        :return: The device_id of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ProcessParams.

        This parameter is used to specify the document reader device type from which input images were captured. Default 0.  # noqa: E501

        :param device_id: The device_id of this ProcessParams.  # noqa: E501
        :type device_id: int
        """

        self._device_id = device_id

    @property
    def device_type(self):
        """Gets the device_type of this ProcessParams.  # noqa: E501

        This parameter is used to specify the document reader device type from which input images were captured. Default 0.  # noqa: E501

        :return: The device_type of this ProcessParams.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ProcessParams.

        This parameter is used to specify the document reader device type from which input images were captured. Default 0.  # noqa: E501

        :param device_type: The device_type of this ProcessParams.  # noqa: E501
        :type device_type: int
        """

        self._device_type = device_type

    @property
    def device_type_hex(self):
        """Gets the device_type_hex of this ProcessParams.  # noqa: E501

        This parameter is used to specify the document reader device type from which input images were captured  # noqa: E501

        :return: The device_type_hex of this ProcessParams.  # noqa: E501
        :rtype: str
        """
        return self._device_type_hex

    @device_type_hex.setter
    def device_type_hex(self, device_type_hex):
        """Sets the device_type_hex of this ProcessParams.

        This parameter is used to specify the document reader device type from which input images were captured  # noqa: E501

        :param device_type_hex: The device_type_hex of this ProcessParams.  # noqa: E501
        :type device_type_hex: str
        """

        self._device_type_hex = device_type_hex

    @property
    def ignore_device_id_from_image(self):
        """Gets the ignore_device_id_from_image of this ProcessParams.  # noqa: E501

        This parameter is used to tell the processing engine to ignore any parameters saved in the image when scanned from the document reader device. Default false  # noqa: E501

        :return: The ignore_device_id_from_image of this ProcessParams.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_device_id_from_image

    @ignore_device_id_from_image.setter
    def ignore_device_id_from_image(self, ignore_device_id_from_image):
        """Sets the ignore_device_id_from_image of this ProcessParams.

        This parameter is used to tell the processing engine to ignore any parameters saved in the image when scanned from the document reader device. Default false  # noqa: E501

        :param ignore_device_id_from_image: The ignore_device_id_from_image of this ProcessParams.  # noqa: E501
        :type ignore_device_id_from_image: bool
        """

        self._ignore_device_id_from_image = ignore_device_id_from_image

    @property
    def document_id_list(self):
        """Gets the document_id_list of this ProcessParams.  # noqa: E501

        List of the document ID's to process. All documents will be processed, if empty.  # noqa: E501

        :return: The document_id_list of this ProcessParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._document_id_list

    @document_id_list.setter
    def document_id_list(self, document_id_list):
        """Sets the document_id_list of this ProcessParams.

        List of the document ID's to process. All documents will be processed, if empty.  # noqa: E501

        :param document_id_list: The document_id_list of this ProcessParams.  # noqa: E501
        :type document_id_list: list[int]
        """

        self._document_id_list = document_id_list

    @property
    def rfid(self):
        """Gets the rfid of this ProcessParams.  # noqa: E501


        :return: The rfid of this ProcessParams.  # noqa: E501
        :rtype: ProcessParamsRfid
        """
        return self._rfid

    @rfid.setter
    def rfid(self, rfid):
        """Sets the rfid of this ProcessParams.


        :param rfid: The rfid of this ProcessParams.  # noqa: E501
        :type rfid: ProcessParamsRfid
        """

        self._rfid = rfid

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
        if not isinstance(other, ProcessParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessParams):
            return True

        return self.to_dict() != other.to_dict()
