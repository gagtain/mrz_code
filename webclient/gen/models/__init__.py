# coding: utf-8

# flake8: noqa


from __future__ import absolute_import

# import models into model package
from webclient.gen.models.area_array import AreaArray
from webclient.gen.models.area_container import AreaContainer
from webclient.gen.models.authenticity_check_list import AuthenticityCheckList
from webclient.gen.models.authenticity_check_result import AuthenticityCheckResult
from webclient.gen.models.authenticity_check_result_item import AuthenticityCheckResultItem
from webclient.gen.models.authenticity_result import AuthenticityResult
from webclient.gen.models.authenticity_result_all_of import AuthenticityResultAllOf
from webclient.gen.models.authenticity_result_type import AuthenticityResultType
from webclient.gen.models.bc_pdf417_info import BcPDF417INFO
from webclient.gen.models.bc_roidetect import BcROIDETECT
from webclient.gen.models.check_diagnose import CheckDiagnose
from webclient.gen.models.check_result import CheckResult
from webclient.gen.models.chosen_document_type import ChosenDocumentType
from webclient.gen.models.chosen_document_type_result import ChosenDocumentTypeResult
from webclient.gen.models.chosen_document_type_result_all_of import ChosenDocumentTypeResultAllOf
from webclient.gen.models.container_list import ContainerList
from webclient.gen.models.critical import Critical
from webclient.gen.models.cross_source_value_comparison import CrossSourceValueComparison
from webclient.gen.models.data_module import DataModule
from webclient.gen.models.details_optical import DetailsOptical
from webclient.gen.models.details_rfid import DetailsRFID
from webclient.gen.models.device_info import DeviceInfo
from webclient.gen.models.doc_bar_code_info import DocBarCodeInfo
from webclient.gen.models.doc_bar_code_info_all_of import DocBarCodeInfoAllOf
from webclient.gen.models.doc_bar_code_info_fields_list import DocBarCodeInfoFieldsList
from webclient.gen.models.doc_visual_extended_field import DocVisualExtendedField
from webclient.gen.models.doc_visual_extended_info import DocVisualExtendedInfo
from webclient.gen.models.document_format import DocumentFormat
from webclient.gen.models.document_image import DocumentImage
from webclient.gen.models.document_image_result import DocumentImageResult
from webclient.gen.models.document_image_result_all_of import DocumentImageResultAllOf
from webclient.gen.models.document_position import DocumentPosition
from webclient.gen.models.document_position_result import DocumentPositionResult
from webclient.gen.models.document_position_result_all_of import DocumentPositionResultAllOf
from webclient.gen.models.document_type import DocumentType
from webclient.gen.models.document_type_recognition_result import DocumentTypeRecognitionResult
from webclient.gen.models.document_types_candidates import DocumentTypesCandidates
from webclient.gen.models.document_types_candidates_list import DocumentTypesCandidatesList
from webclient.gen.models.document_types_candidates_result import DocumentTypesCandidatesResult
from webclient.gen.models.document_types_candidates_result_all_of import DocumentTypesCandidatesResultAllOf
from webclient.gen.models.encrypted_rcl_result import EncryptedRCLResult
from webclient.gen.models.encrypted_rcl_result_all_of import EncryptedRCLResultAllOf
from webclient.gen.models.fdsid_list import FDSIDList
from webclient.gen.models.face_api import FaceApi
from webclient.gen.models.face_api_search import FaceApiSearch
from webclient.gen.models.fiber_result import FiberResult
from webclient.gen.models.fiber_result_all_of import FiberResultAllOf
from webclient.gen.models.graphic_field import GraphicField
from webclient.gen.models.graphic_field_type import GraphicFieldType
from webclient.gen.models.graphic_fields_list import GraphicFieldsList
from webclient.gen.models.graphics_result import GraphicsResult
from webclient.gen.models.graphics_result_all_of import GraphicsResultAllOf
from webclient.gen.models.ident_result import IdentResult
from webclient.gen.models.ident_result_all_of import IdentResultAllOf
from webclient.gen.models.image_data import ImageData
from webclient.gen.models.image_qa import ImageQA
from webclient.gen.models.image_quality_check import ImageQualityCheck
from webclient.gen.models.image_quality_check_list import ImageQualityCheckList
from webclient.gen.models.image_quality_check_type import ImageQualityCheckType
from webclient.gen.models.image_quality_result import ImageQualityResult
from webclient.gen.models.image_quality_result_all_of import ImageQualityResultAllOf
from webclient.gen.models.images import Images
from webclient.gen.models.images_available_source import ImagesAvailableSource
from webclient.gen.models.images_field import ImagesField
from webclient.gen.models.images_field_value import ImagesFieldValue
from webclient.gen.models.images_result import ImagesResult
from webclient.gen.models.images_result_all_of import ImagesResultAllOf
from webclient.gen.models.lcid import LCID
from webclient.gen.models.lexical_analysis_result import LexicalAnalysisResult
from webclient.gen.models.lexical_analysis_result_all_of import LexicalAnalysisResultAllOf
from webclient.gen.models.license_result import LicenseResult
from webclient.gen.models.license_result_all_of import LicenseResultAllOf
from webclient.gen.models.light import Light
from webclient.gen.models.list_verified_fields import ListVerifiedFields
from webclient.gen.models.log_level import LogLevel
from webclient.gen.models.mrz_format import MRZFormat
from webclient.gen.models.measure_system import MeasureSystem
from webclient.gen.models.ocr_security_text_result import OCRSecurityTextResult
from webclient.gen.models.ocr_security_text_result_all_of import OCRSecurityTextResultAllOf
from webclient.gen.models.one_candidate import OneCandidate
from webclient.gen.models.original_symbol import OriginalSymbol
from webclient.gen.models.p_array_field import PArrayField
from webclient.gen.models.parsing_notification_codes import ParsingNotificationCodes
from webclient.gen.models.per_document_config import PerDocumentConfig
from webclient.gen.models.photo_ident_result import PhotoIdentResult
from webclient.gen.models.photo_ident_result_all_of import PhotoIdentResultAllOf
from webclient.gen.models.point import Point
from webclient.gen.models.point_array import PointArray
from webclient.gen.models.points_container import PointsContainer
from webclient.gen.models.process_params import ProcessParams
from webclient.gen.models.process_params_rfid import ProcessParamsRfid
from webclient.gen.models.process_request import ProcessRequest
from webclient.gen.models.process_request_image import ProcessRequestImage
from webclient.gen.models.process_response import ProcessResponse
from webclient.gen.models.process_system_info import ProcessSystemInfo
from webclient.gen.models.processing_status import ProcessingStatus
from webclient.gen.models.raw_image_container_list import RawImageContainerList
from webclient.gen.models.rectangle_coordinates import RectangleCoordinates
from webclient.gen.models.result import Result
from webclient.gen.models.result_item import ResultItem
from webclient.gen.models.rfid_location import RfidLocation
from webclient.gen.models.rfid_origin import RfidOrigin
from webclient.gen.models.scenario import Scenario
from webclient.gen.models.security_feature_result import SecurityFeatureResult
from webclient.gen.models.security_feature_result_all_of import SecurityFeatureResultAllOf
from webclient.gen.models.security_feature_type import SecurityFeatureType
from webclient.gen.models.source import Source
from webclient.gen.models.source_validity import SourceValidity
from webclient.gen.models.status import Status
from webclient.gen.models.status_result import StatusResult
from webclient.gen.models.status_result_all_of import StatusResultAllOf
from webclient.gen.models.string_recognition_result import StringRecognitionResult
from webclient.gen.models.symbol_candidate import SymbolCandidate
from webclient.gen.models.symbol_recognition_result import SymbolRecognitionResult
from webclient.gen.models.text import Text
from webclient.gen.models.text_available_source import TextAvailableSource
from webclient.gen.models.text_data_result import TextDataResult
from webclient.gen.models.text_data_result_all_of import TextDataResultAllOf
from webclient.gen.models.text_field import TextField
from webclient.gen.models.text_field_type import TextFieldType
from webclient.gen.models.text_field_value import TextFieldValue
from webclient.gen.models.text_post_processing import TextPostProcessing
from webclient.gen.models.text_result import TextResult
from webclient.gen.models.text_result_all_of import TextResultAllOf
from webclient.gen.models.transaction_info import TransactionInfo
from webclient.gen.models.verification_result import VerificationResult
from webclient.gen.models.verified_field_map import VerifiedFieldMap
from webclient.gen.models.visibility import Visibility
