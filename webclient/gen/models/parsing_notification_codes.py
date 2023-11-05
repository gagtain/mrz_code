# coding: utf-8



import pprint
import re  # noqa: F401

import six

from webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from webclient.gen.models import *


"""
The enumeration contains possible values of notification codes returned during the RFID chip processing.
"""
class ParsingNotificationCodes(object):

    ntfLDS_ASN_Certificate_IncorrectVersion = int("-1879048191")

    ntfLDS_ASN_Certificate_NonMatchingSignatureAlgorithm = int("-1879048190")

    ntfLDS_ASN_Certificate_IncorrectTimeCoding = int("-1879048189")

    ntfLDS_ASN_Certificate_IncorrectUseOfGeneralizedTime = int("-1879048188")

    ntfLDS_ASN_Certificate_EmptyIssuer = int("-1879048187")

    ntfLDS_ASN_Certificate_EmptySubject = int("-1879048186")

    ntfLDS_ASN_Certificate_UnsupportedCriticalExtension = int("-1879048184")

    ntfLDS_ASN_Certificate_ForcedDefaultCSCARole = int("-1879048178")

    ntfLDS_ASN_Certificate_ForcedDefaultDSRole = int("-1879048177")

    ntfLDS_ASN_Certificate_IncorrectIssuerSubjectDS = int("-1879048176")

    ntfLDS_ASN_Certificate_DuplicatingExtensions = int("-1879048169")

    ntfLDS_ICAO_Certificate_Version_Missed = int("-1879047680")

    ntfLDS_ICAO_Certificate_Version_Incorrect = int("-1879047679")

    ntfLDS_ICAO_Certificate_Issuer_Country_Missed = int("-1879047678")

    ntfLDS_ICAO_Certificate_Issuer_CommonName_Missed = int("-1879047677")

    ntfLDS_ICAO_Certificate_Issuer_CountryNonCompliant = int("-1879047676")

    ntfLDS_ICAO_Certificate_Subject_Country_Missed = int("-1879047675")

    ntfLDS_ICAO_Certificate_Subject_CommonName_Missed = int("-1879047674")

    ntfLDS_ICAO_Certificate_Subject_CountryNonCompliant = int("-1879047673")

    ntfLDS_ICAO_Certificate_UsingNonCompliantData = int("-1879047672")

    ntfLDS_ICAO_Certificate_UnsupportedSignatureAlgorithm = int("-1879047671")

    ntfLDS_ICAO_Certificate_UnsupportedPublicKeyAlgorithm = int("-1879047670")

    ntfLDS_ICAO_Certificate_MissedExtensions = int("-1879047669")

    ntfLDS_ICAO_Certificate_Validity = int("-1879047668")

    ntfLDS_ICAO_Certificate_Ext_UsingNonCompliantData = int("-1879047667")

    ntfLDS_ICAO_Certificate_Ext_KeyUsage_Missed = int("-1879047666")

    ntfLDS_ICAO_Certificate_Ext_KeyUsage_NotCritical = int("-1879047665")

    ntfLDS_ICAO_Certificate_Ext_KeyUsage_IncorrectData = int("-1879047664")

    ntfLDS_ICAO_Certificate_Ext_BasicC_Missed = int("-1879047663")

    ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectUsage1 = int("-1879047662")

    ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectUsage2 = int("-1879047661")

    ntfLDS_ICAO_Certificate_Ext_BasicC_NotCritical = int("-1879047660")

    ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectData = int("-1879047659")

    ntfLDS_ICAO_Certificate_Ext_BasicC_PathLenC_Missed = int("-1879047658")

    ntfLDS_ICAO_Certificate_Ext_BasicC_PathLenC_Incorrect = int("-1879047657")

    ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_NotCritical = int("-1879047656")

    ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_IncorrectUsage = int("-1879047655")

    ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_IncorrectData = int("-1879047654")

    ntfLDS_ICAO_Certificate_Ext_AuthKeyID_Missed = int("-1879047653")

    ntfLDS_ICAO_Certificate_Ext_AuthKeyID_IncorrectData = int("-1879047652")

    ntfLDS_ICAO_Certificate_Ext_AuthKeyID_KeyID_Missed = int("-1879047651")

    ntfLDS_ICAO_Certificate_Ext_SubjectKeyID_Missed = int("-1879047650")

    ntfLDS_ICAO_Certificate_Ext_SubjectKeyID_IncorrectData = int("-1879047649")

    ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_Missed = int("-1879047648")

    ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_IncorrectData = int("-1879047647")

    ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_Empty = int("-1879047646")

    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Missed = int("-1879047645")

    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_IncorrectData = int("-1879047644")

    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Empty = int("-1879047643")

    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_NonCompliant = int("-1879047642")

    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Critical = int("-1879047640")

    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_Empty = int("-1879047639")

    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_Incorrect = int("-1879047638")

    ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_NonCompliant = int("-1879047637")

    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Missed = int("-1879047636")

    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_IncorrectData = int("-1879047635")

    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Empty = int("-1879047634")

    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_NonCompliant = int("-1879047633")

    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Critical = int("-1879047631")

    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_Empty = int("-1879047630")

    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_Incorrect = int("-1879047629")

    ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_NonCompliant = int("-1879047628")

    ntfLDS_ICAO_Certificate_Ext_DocTypeList_Missed = int("-1879047627")

    ntfLDS_ICAO_Certificate_Ext_DocTypeList_IncorrectData = int("-1879047626")

    ntfLDS_ICAO_Certificate_Ext_DocTypeList_Version = int("-1879047625")

    ntfLDS_ICAO_Certificate_Ext_DocTypeList_DocTypes = int("-1879047624")

    ntfLDS_ICAO_Certificate_Ext_DocTypeList_DocTypes_Empty = int("-1879047623")

    ntfLDS_ICAO_Certificate_Ext_CertPolicies_IncorrectData = int("-1879047622")

    ntfLDS_ICAO_Certificate_Ext_CertPolicies_Empty = int("-1879047621")

    ntfLDS_ICAO_Certificate_Ext_CertPolicies_PolicyID_Missed = int("-1879047620")

    ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_Missed = int("-1879047619")

    ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_IncorrectData = int("-1879047618")

    ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_Empty = int("-1879047617")

    ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_PointMissed = int("-1879047616")

    ntfLDS_ICAO_Certificate_SN_NonCompliant = int("-1879047615")

    ntfLDS_ICAO_Certificate_Issuer_SN_NonCompliant = int("-1879047614")

    ntfLDS_ICAO_Certificate_Subject_SN_NonCompliant = int("-1879047613")

    ntfLDS_ICAO_Certificate_Issuer_AttributeNonCompliant = int("-1879047612")

    ntfLDS_ICAO_Certificate_Subject_AttributeNonCompliant = int("-1879047611")

    ntfLDS_ICAO_Certificate_IssuerSubject_Country_NonMatching = int("-1879047610")

    ntfLDS_ICAO_Certificate_Ext_CSCA_AltNames_NonMatching = int("-1879047609")

    ntfLDS_ICAO_Certificate_Ext_NameChange_IncorrectData = int("-1879047608")

    ntfLDS_ICAO_Certificate_Ext_NameChange_NonCompliant = int("-1879047607")

    ntfLDS_ICAO_Certificate_Ext_NameChange_Critical = int("-1879047606")

    ntfLDS_ICAO_Certificate_Ext_DocTypeList_NonCompliant = int("-1879047605")

    ntfLDS_ICAO_Certificate_Ext_DocTypeList_Critical = int("-1879047604")

    ntfLDS_ICAO_Certificate_Ext_Optional_Critical = int("-1879047603")

    ntfLDS_ICAO_Certificate_Subject_NonCompliant = int("-1879047602")

    ntfLDS_ICAO_Certificate_Subject_CommonNameNonCompliant = int("-1879047601")

    ntfLDS_ICAO_COM_LDS_Version_Incorrect = int("-1879048160")

    ntfLDS_ICAO_COM_LDS_Version_Missing = int("-1879048159")

    ntfLDS_ICAO_COM_Unicode_Version_Incorrect = int("-1879048158")

    ntfLDS_ICAO_COM_Unicode_Version_Missing = int("-1879048157")

    ntfLDS_ICAO_COM_DGPM_Incorrect = int("-1879048156")

    ntfLDS_ICAO_COM_DGPM_Missing = int("-1879048155")

    ntfLDS_ICAO_COM_DGPM_Unexpected = int("-1879048154")

    ntfLDS_ICAO_Application_LDSVersion_Unsupported = int("-1879048144")

    ntfLDS_ICAO_Application_UnicodeVersion_Unsupported = int("-1879048143")

    ntfLDS_ICAO_Application_LDSVersion_Inconsistent = int("-1879048142")

    ntfLDS_ICAO_Application_UnicodeVersion_Inconsistent = int("-1879048141")

    ntfLDS_ASN_SignedData_OID_Incorrect = int("-1879047936")

    ntfLDS_ASN_SignedData_Version_Incorrect = int("-1879047776")

    ntfLDS_ASN_SignedData_ContentOID_Incorrect = int("-1879047775")

    ntfLDS_ICAO_SignedData_Version_Incorrect = int("-1879047935")

    ntfLDS_ICAO_SignedData_DigestAlgorithms_Empty = int("-1879047934")

    ntfLDS_ICAO_SignedData_DigestAlgorithms_Unsupported = int("-1879047933")

    ntfLDS_ICAO_SignedData_SignerInfos_MultipleEntries = int("-1879047927")

    ntfLDS_ICAO_SignedData_Certificates_Missed = int("-1879047760")

    ntfLDS_ICAO_SignedData_Certificates_Empty = int("-1879047759")

    ntfLDS_ICAO_SignedData_CRLs_IncorrectUsage = int("-1879047758")

    ntfLDS_ICAO_LDSObject_IncorrectContentOID = int("-1879047932")

    ntfLDS_ICAO_LDSObject_DGNumber_Incorrect = int("-1879047931")

    ntfLDS_ICAO_LDSObject_DGHash_Missing = int("-1879047930")

    ntfLDS_ICAO_LDSObject_DGHash_Extra = int("-1879047929")

    ntfLDS_ICAO_LDSObject_Version_Incorrect = int("-1879047928")

    ntfLDS_ICAO_MasterList_Version_Incorrect = int("-1879047744")

    ntfLDS_ICAO_DeviationList_Version_Incorrect = int("-1879047736")

    ntfLDS_BSI_DefectList_Version_Incorrect = int("-1879047728")

    ntfLDS_BSI_BlackList_Version_Incorrect = int("-1879047720")

    ntfLDS_ASN_SignerInfo_Version_Incorrect = int("-1879047926")

    ntfLDS_ASN_SignerInfo_SID_IncorrectChoice = int("-1879047925")

    ntfLDS_ASN_SignerInfo_SID_DigestAlgorithmNotListed = int("-1879047924")

    ntfLDS_ASN_SignerInfo_MessageDigestAttr_Missing = int("-1879047923")

    ntfLDS_ASN_SignerInfo_MessageDigestAttr_Data = int("-1879047922")

    ntfLDS_ASN_SignerInfo_MessageDigestAttr_Value = int("-1879047921")

    ntfLDS_ASN_SignerInfo_ContentTypeAttr_Missing = int("-1879047920")

    ntfLDS_ASN_SignerInfo_ContentTypeAttr_Data = int("-1879047919")

    ntfLDS_ASN_SignerInfo_ContentTypeAttr_Value = int("-1879047918")

    ntfLDS_ASN_SignerInfo_SigningTimeAttr_Missing = int("-1879047909")

    ntfLDS_ASN_SignerInfo_SigningTimeAttr_Data = int("-1879047908")

    ntfLDS_ASN_SignerInfo_SigningTimeAttr_Value = int("-1879047907")

    ntfLDS_ASN_SignerInfo_ListContentDescriptionAttr_Missing = int("-1879047906")

    ntfLDS_ASN_SignerInfo_ListContentDescriptionAttr_Data = int("-1879047905")

    ntfLDS_Auth_SignerInfo_Certificate_Validity = int("-1879047915")

    ntfLDS_Auth_SignerInfo_Certificate_RootIsNotTrusted = int("-1879047914")

    ntfLDS_Auth_SignerInfo_Certificate_CantFindCSCA = int("-1879047913")

    ntfLDS_Auth_SignerInfo_Certificate_Revoked = int("-1879047912")

    ntfLDS_Auth_SignerInfo_Certificate_SignatureInvalid = int("-1879047911")

    ntfLDS_UnsupportedImageFormat = int("-1879047910")

    ntfLDS_MRZ_DocumentType_Unknown = int("139272")

    ntfLDS_MRZ_IssuingState_SyntaxError = int("139273")

    ntfLDS_MRZ_Name_IsVoid = int("139274")

    ntfLDS_MRZ_Number_IncorrectChecksum = int("139277")

    ntfLDS_MRZ_Nationality_SyntaxError = int("139278")

    ntfLDS_MRZ_DOB_SyntaxError = int("139279")

    ntfLDS_MRZ_DOB_Error = int("139280")

    ntfLDS_MRZ_DOB_IncorrectChecksum = int("139281")

    ntfLDS_MRZ_Sex_Incorrect = int("139282")

    ntfLDS_MRZ_DOE_SyntaxError = int("139283")

    ntfLDS_MRZ_DOE_Error = int("139284")

    ntfLDS_MRZ_DOE_IncorrectChecksum = int("139285")

    ntfLDS_MRZ_OptionalData_IncorrectChecksum = int("139286")

    ntfLDS_MRZ_IncorrectChecksum = int("139287")

    ntfLDS_MRZ_Incorrect = int("139288")

    ntfLDS_Biometrics_FormatOwner_Missing = int("-1878982656")

    ntfLDS_Biometrics_FormatOwner_Incorrect = int("-1878917120")

    ntfLDS_Biometrics_FormatType_Missing = int("-1878851584")

    ntfLDS_Biometrics_FormatType_Incorrect = int("-1878786048")

    ntfLDS_Biometrics_Type_Incorrect = int("-1878720512")

    ntfLDS_Biometrics_SubType_Missing = int("-1878654976")

    ntfLDS_Biometrics_SubType_Incorrect = int("-1878589440")

    ntfLDS_Biometrics_BDB_Image_Missing = int("-1878523904")

    ntfLDS_Biometrics_BDB_FormatID_Incorrect = int("-1878458368")

    ntfLDS_Biometrics_BDB_Version_Incorrect = int("-1878392832")

    ntfLDS_Biometrics_BDB_DataLength_Incorrect = int("-1878327296")

    ntfLDS_Biometrics_BDB_Data_Gender = int("-1877999616")

    ntfLDS_Biometrics_BDB_Data_EyeColor = int("-1877934080")

    ntfLDS_Biometrics_BDB_Data_HairColor = int("-1877868544")

    ntfLDS_Biometrics_BDB_Data_PoseAngle_Yaw = int("-1877803008")

    ntfLDS_Biometrics_BDB_Data_PoseAngle_Pitch = int("-1877737472")

    ntfLDS_Biometrics_BDB_Data_PoseAngle_Roll = int("-1877671936")

    ntfLDS_Biometrics_BDB_Data_PoseAngleU_Yaw = int("-1877606400")

    ntfLDS_Biometrics_BDB_Data_PoseAngleU_Pitch = int("-1877540864")

    ntfLDS_Biometrics_BDB_Data_PoseAngleU_Roll = int("-1877475328")

    ntfLDS_Biometrics_BDB_Data_FaceImageType = int("-1877409792")

    ntfLDS_Biometrics_BDB_Data_ImageDataType = int("-1877344256")

    ntfLDS_SI_PACE_Info_UnsupportedStdParameters = int("-1862270976")

    ntfLDS_SI_PACE_Info_DeprecatedVersion = int("-1862270975")

    ntfLDS_SI_PACE_DomainParams_UsingStdRef = int("-1862270974")

    ntfLDS_SI_PACE_DomainParams_UnsupportedAlgorithm = int("-1862270973")

    ntfLDS_SI_CA_Info_IncorrectVersion = int("-1862270972")

    ntfLDS_SI_CA_PublicKey_UnsupportedAlgorithm = int("-1862270971")

    ntfLDS_SI_CA_DomainParams_UnsupportedAlgorithm = int("-1862270970")

    ntfLDS_SI_TA_Info_IncorrectVersion = int("-1862270969")

    ntfLDS_SI_TA_Info_FileIDForVersion2 = int("-1862270968")

    ntfLDS_SI_eIDSecurity_UnsupportedDigestAlgorithm = int("-1862270967")

    ntfLDS_SI_RI_Info_IncorrectVersion = int("-1862270966")

    ntfLDS_SI_RI_DomainParams_UnsupportedAlgorithm = int("-1862270965")

    ntfLDS_SI_AA_Info_IncorrectVersion = int("-1862270964")

    ntfLDS_SI_AA_Info_UnsupportedAlgorithm = int("-1862270963")

    ntfLDS_SI_AA_Info_InconsistentAlgorithmReference = int("-1862270962")

    ntfLDS_SI_Storage_PACE_Info_NotAvailable = int("-1862270720")

    ntfLDS_SI_Storage_PACE_Info_NoStdParameters = int("-1862270719")

    ntfLDS_SI_Storage_PACE_Info_NoMatchingDomainParams = int("-1862270718")

    ntfLDS_SI_Storage_CA_Info_NotAvailable = int("-1862270717")

    ntfLDS_SI_Storage_CA_DomainParams_NoRequiredOption = int("-1862270716")

    ntfLDS_SI_Storage_CA_DomainParams_NotAvailable = int("-1862270715")

    ntfLDS_SI_Storage_CA_AnonymousInfos = int("-1862270714")

    ntfLDS_SI_Storage_CA_Info_NoMatchingDomainParams = int("-1862270713")

    ntfLDS_SI_Storage_CA_Info_NoMatchingPublicKey = int("-1862270712")

    ntfLDS_SI_Storage_CA_IncorrectInfosQuantity = int("-1862270711")

    ntfLDS_SI_Storage_TA_Info_NotAvailable = int("-1862270710")

    ntfLDS_SI_Storage_CardInfoLocator_MultipleEntries = int("-1862270709")

    ntfLDS_SI_Storage_eIDSecurityInfo_MultipleEntries = int("-1862270708")

    ntfLDS_SI_Storage_PrivilegedTI_MultipleEntries = int("-1862270707")

    ntfLDS_SI_Storage_PrivilegedTI_IncorrectUsage = int("-1862270706")

    ntfLDS_SI_Storage_RI_DomainParams_MultipleEntries = int("-1862270705")

    ntfLDS_SI_Storage_PACEInfos_NonConsistant = int("-1862270704")

    ntfLDS_CVCertificate_Profile_IncorrectVersion = int("-1862270463")

    ntfLDS_CVCertificate_Validity = int("-1862270462")

    ntfLDS_CVCertificate_NonCVCADomainParameters = int("-1862270461")

    ntfLDS_CV_Certificate_PrivateKey_IncorrectVersion = int("-1862270460")

    ntfLDS_TA_PACEStaticBindingUsed = int("-1862270208")

    ntfLDS_Auth_MLSignerInfo_Certificate_Validity = int("-1845493483")

    ntfLDS_Auth_MLSignerInfo_Certificate_RootIsNotTrusted = int("-1845493482")

    ntfLDS_Auth_MLSignerInfo_Certificate_CantFindCSCA = int("-1845493481")

    ntfLDS_Auth_MLSignerInfo_Certificate_Revoked = int("-1845493480")

    ntfLDS_Auth_MLSignerInfo_Certificate_SignatureInvalid = int("-1845493479")

    allowable_values = [ntfLDS_ASN_Certificate_IncorrectVersion, ntfLDS_ASN_Certificate_NonMatchingSignatureAlgorithm, ntfLDS_ASN_Certificate_IncorrectTimeCoding, ntfLDS_ASN_Certificate_IncorrectUseOfGeneralizedTime, ntfLDS_ASN_Certificate_EmptyIssuer, ntfLDS_ASN_Certificate_EmptySubject, ntfLDS_ASN_Certificate_UnsupportedCriticalExtension, ntfLDS_ASN_Certificate_ForcedDefaultCSCARole, ntfLDS_ASN_Certificate_ForcedDefaultDSRole, ntfLDS_ASN_Certificate_IncorrectIssuerSubjectDS, ntfLDS_ASN_Certificate_DuplicatingExtensions, ntfLDS_ICAO_Certificate_Version_Missed, ntfLDS_ICAO_Certificate_Version_Incorrect, ntfLDS_ICAO_Certificate_Issuer_Country_Missed, ntfLDS_ICAO_Certificate_Issuer_CommonName_Missed, ntfLDS_ICAO_Certificate_Issuer_CountryNonCompliant, ntfLDS_ICAO_Certificate_Subject_Country_Missed, ntfLDS_ICAO_Certificate_Subject_CommonName_Missed, ntfLDS_ICAO_Certificate_Subject_CountryNonCompliant, ntfLDS_ICAO_Certificate_UsingNonCompliantData, ntfLDS_ICAO_Certificate_UnsupportedSignatureAlgorithm, ntfLDS_ICAO_Certificate_UnsupportedPublicKeyAlgorithm, ntfLDS_ICAO_Certificate_MissedExtensions, ntfLDS_ICAO_Certificate_Validity, ntfLDS_ICAO_Certificate_Ext_UsingNonCompliantData, ntfLDS_ICAO_Certificate_Ext_KeyUsage_Missed, ntfLDS_ICAO_Certificate_Ext_KeyUsage_NotCritical, ntfLDS_ICAO_Certificate_Ext_KeyUsage_IncorrectData, ntfLDS_ICAO_Certificate_Ext_BasicC_Missed, ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectUsage1, ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectUsage2, ntfLDS_ICAO_Certificate_Ext_BasicC_NotCritical, ntfLDS_ICAO_Certificate_Ext_BasicC_IncorrectData, ntfLDS_ICAO_Certificate_Ext_BasicC_PathLenC_Missed, ntfLDS_ICAO_Certificate_Ext_BasicC_PathLenC_Incorrect, ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_NotCritical, ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_IncorrectUsage, ntfLDS_ICAO_Certificate_Ext_ExtKeyUsage_IncorrectData, ntfLDS_ICAO_Certificate_Ext_AuthKeyID_Missed, ntfLDS_ICAO_Certificate_Ext_AuthKeyID_IncorrectData, ntfLDS_ICAO_Certificate_Ext_AuthKeyID_KeyID_Missed, ntfLDS_ICAO_Certificate_Ext_SubjectKeyID_Missed, ntfLDS_ICAO_Certificate_Ext_SubjectKeyID_IncorrectData, ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_Missed, ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_IncorrectData, ntfLDS_ICAO_Certificate_Ext_PrivateKeyUP_Empty, ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Missed, ntfLDS_ICAO_Certificate_Ext_SubjectAltName_IncorrectData, ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Empty, ntfLDS_ICAO_Certificate_Ext_SubjectAltName_NonCompliant, ntfLDS_ICAO_Certificate_Ext_SubjectAltName_Critical, ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_Empty, ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_Incorrect, ntfLDS_ICAO_Certificate_Ext_SubjectAltName_DN_NonCompliant, ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Missed, ntfLDS_ICAO_Certificate_Ext_IssuerAltName_IncorrectData, ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Empty, ntfLDS_ICAO_Certificate_Ext_IssuerAltName_NonCompliant, ntfLDS_ICAO_Certificate_Ext_IssuerAltName_Critical, ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_Empty, ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_Incorrect, ntfLDS_ICAO_Certificate_Ext_IssuerAltName_DN_NonCompliant, ntfLDS_ICAO_Certificate_Ext_DocTypeList_Missed, ntfLDS_ICAO_Certificate_Ext_DocTypeList_IncorrectData, ntfLDS_ICAO_Certificate_Ext_DocTypeList_Version, ntfLDS_ICAO_Certificate_Ext_DocTypeList_DocTypes, ntfLDS_ICAO_Certificate_Ext_DocTypeList_DocTypes_Empty, ntfLDS_ICAO_Certificate_Ext_CertPolicies_IncorrectData, ntfLDS_ICAO_Certificate_Ext_CertPolicies_Empty, ntfLDS_ICAO_Certificate_Ext_CertPolicies_PolicyID_Missed, ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_Missed, ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_IncorrectData, ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_Empty, ntfLDS_ICAO_Certificate_Ext_CRLDistPoint_PointMissed, ntfLDS_ICAO_Certificate_SN_NonCompliant, ntfLDS_ICAO_Certificate_Issuer_SN_NonCompliant, ntfLDS_ICAO_Certificate_Subject_SN_NonCompliant, ntfLDS_ICAO_Certificate_Issuer_AttributeNonCompliant, ntfLDS_ICAO_Certificate_Subject_AttributeNonCompliant, ntfLDS_ICAO_Certificate_IssuerSubject_Country_NonMatching, ntfLDS_ICAO_Certificate_Ext_CSCA_AltNames_NonMatching, ntfLDS_ICAO_Certificate_Ext_NameChange_IncorrectData, ntfLDS_ICAO_Certificate_Ext_NameChange_NonCompliant, ntfLDS_ICAO_Certificate_Ext_NameChange_Critical, ntfLDS_ICAO_Certificate_Ext_DocTypeList_NonCompliant, ntfLDS_ICAO_Certificate_Ext_DocTypeList_Critical, ntfLDS_ICAO_Certificate_Ext_Optional_Critical, ntfLDS_ICAO_Certificate_Subject_NonCompliant, ntfLDS_ICAO_Certificate_Subject_CommonNameNonCompliant, ntfLDS_ICAO_COM_LDS_Version_Incorrect, ntfLDS_ICAO_COM_LDS_Version_Missing, ntfLDS_ICAO_COM_Unicode_Version_Incorrect, ntfLDS_ICAO_COM_Unicode_Version_Missing, ntfLDS_ICAO_COM_DGPM_Incorrect, ntfLDS_ICAO_COM_DGPM_Missing, ntfLDS_ICAO_COM_DGPM_Unexpected, ntfLDS_ICAO_Application_LDSVersion_Unsupported, ntfLDS_ICAO_Application_UnicodeVersion_Unsupported, ntfLDS_ICAO_Application_LDSVersion_Inconsistent, ntfLDS_ICAO_Application_UnicodeVersion_Inconsistent, ntfLDS_ASN_SignedData_OID_Incorrect, ntfLDS_ASN_SignedData_Version_Incorrect, ntfLDS_ASN_SignedData_ContentOID_Incorrect, ntfLDS_ICAO_SignedData_Version_Incorrect, ntfLDS_ICAO_SignedData_DigestAlgorithms_Empty, ntfLDS_ICAO_SignedData_DigestAlgorithms_Unsupported, ntfLDS_ICAO_SignedData_SignerInfos_MultipleEntries, ntfLDS_ICAO_SignedData_Certificates_Missed, ntfLDS_ICAO_SignedData_Certificates_Empty, ntfLDS_ICAO_SignedData_CRLs_IncorrectUsage, ntfLDS_ICAO_LDSObject_IncorrectContentOID, ntfLDS_ICAO_LDSObject_DGNumber_Incorrect, ntfLDS_ICAO_LDSObject_DGHash_Missing, ntfLDS_ICAO_LDSObject_DGHash_Extra, ntfLDS_ICAO_LDSObject_Version_Incorrect, ntfLDS_ICAO_MasterList_Version_Incorrect, ntfLDS_ICAO_DeviationList_Version_Incorrect, ntfLDS_BSI_DefectList_Version_Incorrect, ntfLDS_BSI_BlackList_Version_Incorrect, ntfLDS_ASN_SignerInfo_Version_Incorrect, ntfLDS_ASN_SignerInfo_SID_IncorrectChoice, ntfLDS_ASN_SignerInfo_SID_DigestAlgorithmNotListed, ntfLDS_ASN_SignerInfo_MessageDigestAttr_Missing, ntfLDS_ASN_SignerInfo_MessageDigestAttr_Data, ntfLDS_ASN_SignerInfo_MessageDigestAttr_Value, ntfLDS_ASN_SignerInfo_ContentTypeAttr_Missing, ntfLDS_ASN_SignerInfo_ContentTypeAttr_Data, ntfLDS_ASN_SignerInfo_ContentTypeAttr_Value, ntfLDS_ASN_SignerInfo_SigningTimeAttr_Missing, ntfLDS_ASN_SignerInfo_SigningTimeAttr_Data, ntfLDS_ASN_SignerInfo_SigningTimeAttr_Value, ntfLDS_ASN_SignerInfo_ListContentDescriptionAttr_Missing, ntfLDS_ASN_SignerInfo_ListContentDescriptionAttr_Data, ntfLDS_Auth_SignerInfo_Certificate_Validity, ntfLDS_Auth_SignerInfo_Certificate_RootIsNotTrusted, ntfLDS_Auth_SignerInfo_Certificate_CantFindCSCA, ntfLDS_Auth_SignerInfo_Certificate_Revoked, ntfLDS_Auth_SignerInfo_Certificate_SignatureInvalid, ntfLDS_UnsupportedImageFormat, ntfLDS_MRZ_DocumentType_Unknown, ntfLDS_MRZ_IssuingState_SyntaxError, ntfLDS_MRZ_Name_IsVoid, ntfLDS_MRZ_Number_IncorrectChecksum, ntfLDS_MRZ_Nationality_SyntaxError, ntfLDS_MRZ_DOB_SyntaxError, ntfLDS_MRZ_DOB_Error, ntfLDS_MRZ_DOB_IncorrectChecksum, ntfLDS_MRZ_Sex_Incorrect, ntfLDS_MRZ_DOE_SyntaxError, ntfLDS_MRZ_DOE_Error, ntfLDS_MRZ_DOE_IncorrectChecksum, ntfLDS_MRZ_OptionalData_IncorrectChecksum, ntfLDS_MRZ_IncorrectChecksum, ntfLDS_MRZ_Incorrect, ntfLDS_Biometrics_FormatOwner_Missing, ntfLDS_Biometrics_FormatOwner_Incorrect, ntfLDS_Biometrics_FormatType_Missing, ntfLDS_Biometrics_FormatType_Incorrect, ntfLDS_Biometrics_Type_Incorrect, ntfLDS_Biometrics_SubType_Missing, ntfLDS_Biometrics_SubType_Incorrect, ntfLDS_Biometrics_BDB_Image_Missing, ntfLDS_Biometrics_BDB_FormatID_Incorrect, ntfLDS_Biometrics_BDB_Version_Incorrect, ntfLDS_Biometrics_BDB_DataLength_Incorrect, ntfLDS_Biometrics_BDB_Data_Gender, ntfLDS_Biometrics_BDB_Data_EyeColor, ntfLDS_Biometrics_BDB_Data_HairColor, ntfLDS_Biometrics_BDB_Data_PoseAngle_Yaw, ntfLDS_Biometrics_BDB_Data_PoseAngle_Pitch, ntfLDS_Biometrics_BDB_Data_PoseAngle_Roll, ntfLDS_Biometrics_BDB_Data_PoseAngleU_Yaw, ntfLDS_Biometrics_BDB_Data_PoseAngleU_Pitch, ntfLDS_Biometrics_BDB_Data_PoseAngleU_Roll, ntfLDS_Biometrics_BDB_Data_FaceImageType, ntfLDS_Biometrics_BDB_Data_ImageDataType, ntfLDS_SI_PACE_Info_UnsupportedStdParameters, ntfLDS_SI_PACE_Info_DeprecatedVersion, ntfLDS_SI_PACE_DomainParams_UsingStdRef, ntfLDS_SI_PACE_DomainParams_UnsupportedAlgorithm, ntfLDS_SI_CA_Info_IncorrectVersion, ntfLDS_SI_CA_PublicKey_UnsupportedAlgorithm, ntfLDS_SI_CA_DomainParams_UnsupportedAlgorithm, ntfLDS_SI_TA_Info_IncorrectVersion, ntfLDS_SI_TA_Info_FileIDForVersion2, ntfLDS_SI_eIDSecurity_UnsupportedDigestAlgorithm, ntfLDS_SI_RI_Info_IncorrectVersion, ntfLDS_SI_RI_DomainParams_UnsupportedAlgorithm, ntfLDS_SI_AA_Info_IncorrectVersion, ntfLDS_SI_AA_Info_UnsupportedAlgorithm, ntfLDS_SI_AA_Info_InconsistentAlgorithmReference, ntfLDS_SI_Storage_PACE_Info_NotAvailable, ntfLDS_SI_Storage_PACE_Info_NoStdParameters, ntfLDS_SI_Storage_PACE_Info_NoMatchingDomainParams, ntfLDS_SI_Storage_CA_Info_NotAvailable, ntfLDS_SI_Storage_CA_DomainParams_NoRequiredOption, ntfLDS_SI_Storage_CA_DomainParams_NotAvailable, ntfLDS_SI_Storage_CA_AnonymousInfos, ntfLDS_SI_Storage_CA_Info_NoMatchingDomainParams, ntfLDS_SI_Storage_CA_Info_NoMatchingPublicKey, ntfLDS_SI_Storage_CA_IncorrectInfosQuantity, ntfLDS_SI_Storage_TA_Info_NotAvailable, ntfLDS_SI_Storage_CardInfoLocator_MultipleEntries, ntfLDS_SI_Storage_eIDSecurityInfo_MultipleEntries, ntfLDS_SI_Storage_PrivilegedTI_MultipleEntries, ntfLDS_SI_Storage_PrivilegedTI_IncorrectUsage, ntfLDS_SI_Storage_RI_DomainParams_MultipleEntries, ntfLDS_SI_Storage_PACEInfos_NonConsistant, ntfLDS_CVCertificate_Profile_IncorrectVersion, ntfLDS_CVCertificate_Validity, ntfLDS_CVCertificate_NonCVCADomainParameters, ntfLDS_CV_Certificate_PrivateKey_IncorrectVersion, ntfLDS_TA_PACEStaticBindingUsed, ntfLDS_Auth_MLSignerInfo_Certificate_Validity, ntfLDS_Auth_MLSignerInfo_Certificate_RootIsNotTrusted, ntfLDS_Auth_MLSignerInfo_Certificate_CantFindCSCA, ntfLDS_Auth_MLSignerInfo_Certificate_Revoked, ntfLDS_Auth_MLSignerInfo_Certificate_SignatureInvalid]  # noqa: E501

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
        """ParsingNotificationCodes - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, ParsingNotificationCodes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParsingNotificationCodes):
            return True

        return self.to_dict() != other.to_dict()
