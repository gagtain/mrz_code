from mrz.checker.td3 import TD3CodeChecker
from mrz.checker.td1 import TD1CodeChecker
from mrz.checker.td2 import TD2CodeChecker, _TD2HashChecker
from mrz.checker._fields import _FieldsChecker
import mrz.base.string_checkers as check
from mrz.base.countries_ops import *
from mrz.base.functions import hash_is_ok, namedtuple_maker
from mrz.base.functions import anset
from mrz.base.string_checkers import is_empty
from mrz.checker._hash_fields import _HashChecker
from mrz.checker._fields import _FieldsChecker
from mrz.checker._report import _Report, Kind
from mrz.checker._honorifics import titles
from mrz.generator.td2 import TD2CodeGenerator
from mrz.base.string_checkers import field, date


class TD2CodeCheckerID_2(TD2CodeChecker):
    def __init__(self, mrz_code: str, check_expiry=False, compute_warnings=False):
        check.precheck("TD2", mrz_code, 73)
        lines = mrz_code.splitlines()
        self._document_type = lines[0][0: 2]
        self._country = lines[0][2: 5]
        self._identifier = lines[0][5: 30]
        self._document_number = lines[1][0: 12]
        self._document_number_hash = lines[1][12]
        self._nationality = lines[1][10: 13]
        self._birth_date = lines[1][-9:-3]
        self._birth_date_hash = lines[1][-3]
        self._date_of_issue = lines[1][0:4]
        self._sex = lines[1][-2]
        print(lines[1][5: 30])
        self._expiry_date = lines[1][21: 27]
        self._expiry_date_hash = lines[1][27]
        self._optional_data = lines[0][20: 44]
        print('optional', self._optional_data)
        self._final_hash = lines[1][35]
        _TD2HashChecker.__init__(self,
                                 self._document_number,
                                 self._document_number_hash,
                                 self._birth_date,
                                 self._birth_date_hash,
                                 self._expiry_date,
                                 self._expiry_date_hash,
                                 self._optional_data,
                                 self._final_hash)
        _FieldsChecker.__init__(self,
                                self._document_type,
                                self._country,
                                self._identifier,
                                self._document_number,
                                self._nationality,
                                self._birth_date,
                                self._sex,
                                self._expiry_date,
                                self._optional_data,
                                "",
                                check_expiry,
                                compute_warnings,
                                mrz_code)
        self.result = self._all_hashes() & self._all_fields()


    def _str_common_fields(self, zfill: bool):
        fields = (self._id_primary.replace("<", " "),
                  self.mrz_code[-23:-9].replace("<", " "),
                  self._country.rstrip("<"),
                  self._birth_date,
                  self._sex,
                  self._document_type.rstrip("<"),
                  anset(self._document_number, zfill),
                  anset(self._optional_data, zfill))
        names = ("surname name country birth_date sex "
                 "document_type document_number optional_data ")
        print(fields)
        return fields, names

    def _all_hashes(self) -> bool:
        return (self.final_hash &
                self.document_number_hash &
                self.birth_date_hash &
                self.optional_data)
    
    @property
    def final_hash(self) -> bool:
        """Returns True if final hash is True, False otherwise"""
        from mrz.base.functions import hash_is_ok, namedtuple_maker
        ok = hash_is_ok(self._document_number +
                        self._document_number_hash +
                        self._birth_date +
                        self._birth_date_hash, self._final_hash)
        return self.report.add("final hash", ok)

    def _all_fields(self) -> bool:
        return (self.document_type &
                self.country &
                self.birth_date &
                self.sex &
                self.identifier &
                self.document_number &
                self.date_of_issue)
    
    @property
    def date_of_issue(self):
        int(self._date_of_issue)
        return True

    def get_dict_all_fields(self):

        return {"document_type":self.document_type,
                "country":self.country,
                "birth_date":self.birth_date,
                "sex":self.sex,
                "identifier":self.identifier,
                "document_number":self.document_number,
                "date_of_issuse": self.date_of_issue,
                "date_of_issuse_val": self._date_of_issue}
    
    def get_dict_all_fields_validate(self):
        return {"document_type":self.document_type,
                "nationality": self.nationality,
                "country":self.country,
                "birth_date":self.birth_date,
                "sex":self.sex,
                "identifier":self.identifier,
                "document_number":self.document_number,
                "optional_data": self.optional_data,
                "optional_data_2": self.optional_data_2,
                "final_hash":self.final_hash,
                "document_number_hash": self.document_number_hash,
                "birth_date_hash": self.birth_date_hash
                }


class TD2CodeGenerator_ID2(TD2CodeGenerator):
    
    @property
    def document_number(self) -> str:
        """Return document number string

        Document number given by the issuing State or organization, to uniquely identify the document
        from all other MRTDs

        """
        return self._document_number
    

    @document_number.setter
    def document_number(self, value: str):
        """Set document number

        Document number given by the issuing State or organization, to uniquely identify the document
        from all other MRTDs

        Case insensitive.

        """
        self._document_number = field(value, 12, "document number")