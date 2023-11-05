from mrz.checker.td3 import TD3CodeChecker
from mrz.checker.td1 import TD1CodeChecker
from mrz.checker.td2 import TD2CodeChecker, _TD2HashChecker
from mrz.checker._fields import _FieldsChecker
import mrz.base.string_checkers as check
from mrz.base.countries_ops import *
from mrz.base.functions import hash_is_ok, namedtuple_maker
from mrz.base.string_checkers import is_empty
from mrz.checker._hash_fields import _HashChecker
from mrz.checker._fields import _FieldsChecker
from mrz.checker._report import _Report, Kind
from mrz.base.functions import hash_string
from mrz.checker._honorifics import titles
from mrz.base.string_checkers import field, date
import mrz.generator._transliterations as dictionary
from mrz.generator.td3 import TD3CodeGenerator, _TD3HolderName
from mrz.base.errors import DateError

class TD3CodeCheckerIdictAll(TD3CodeChecker):

    def get_dict_all_fields(self):
        return {"document_type":self._document_type,
                "nationality": self._nationality,
                "country":self._country,
                "birth_date":self._birth_date,
                "expiry_date":self._expiry_date,
                "sex":self._sex,
                "identifier":self._identifier,
                "document_number":self._document_number,
                "optional_data": self._optional_data,
                "optional_data_2": self._optional_data_2
                }


    def get_dict_all_fields_validate(self):
        return {"document_type":self.document_type,
                "nationality": self.nationality,
                "country":self.country,
                "birth_date":self.birth_date,
                "expiry_date":self.expiry_date,
                "sex":self.sex,
                "identifier":self.identifier,
                "document_number":self.document_number,
                "optional_data": self.optional_data,
                "optional_data_2": self.optional_data_2,
                "final_hash":self.final_hash,
                "document_number_hash": self.document_number_hash,
                "birth_date_hash": self.birth_date_hash,
                "expiry_date_hash": self.expiry_date_hash,
                "optional_data_hash": self.optional_data_hash
                }

    @property
    def identifier(self) -> bool:
        """Return True is the identifier is validated overcoming the checks, False otherwise."""
        full_id = self._identifier.rstrip("<")
        padding = self._identifier[len(full_id):]
        id2iter = full_id.split("<<")
        id_len = len(id2iter)
        primary = secondary = None
        if not check.is_printable(self._identifier):
            ok = False
        elif check.is_empty(self._identifier):
            self.report.add("empty identifier", level=Kind.ERROR)
            ok = False
        else:
            if id_len == len([i for i in id2iter if i]):
                if id_len == 2:
                    primary, secondary = id2iter
                    ok = True
                elif id_len == 1:
                    primary, secondary = id2iter[0], ""
                    self.report.add("only one identifier", level=Kind.WARNING)
                    ok = not self._compute_warnings
                else:
                    self.report.add("more than two identifiers", level=Kind.ERROR)
                    ok = False
            else:  # too many '<' in id
                self.report.add("invalid identifier format", level=Kind.ERROR)
                ok = False
        if ok:
            if not self._country == "RUS":

                if check.uses_nums(full_id):
                    self.report.add("identifier with numbers", level=Kind.ERROR)
                    ok = False

            else:
                status = False
                for c in full_id:
                    if c in "012345":
                        status = True
                if status:
                    self.report.add("identifier with numbers", level=Kind.ERROR)
                    ok = False
            if primary.startswith("<") or secondary and secondary.startswith("<"):
                self.report.add("some identifier begin by '<'", level=Kind.ERROR)
                ok = False
            if not padding:
                self.report.add("possible truncating", level=Kind.WARNING)
                ok = False if self._compute_warnings else ok
            for i in range(id_len):
                for itm in id2iter[i].split("<"):
                    if itm:
                        for tit in titles:
                            if tit == itm:
                                if i:  # secondary id
                                    self.report.add("Possible unauthorized prefix or suffix in identifier",
                                                 level=Kind.WARNING)
                                else:  # primary id
                                    self.report.add("Possible not recommended prefix or suffix in identifier",
                                                 level=Kind.WARNING)
                                ok = False if self._compute_warnings else ok
        self._id_secondary = str(secondary)
        self._id_primary = str(primary)
        return self.report.add("identifier", ok)
    @property
    def expiry_date(self) -> bool:
        """Return True if the expiry date is validated, False otherwise."""

        ok = False
        try:
            # TODO: Make comment about self._expiry_date_check (if check_periods == True)
            ok = False if not self._expiry_date_check else bool(check.date(self._expiry_date))
        except ValueError:
            pass
        finally:
            if self._expiry_date == '<<<<<<' and self._country == 'RUS':
                ok = True
            return self.report.add("expiry date", ok)
    @property
    def expiry_date_hash(self) -> bool:
        """Return True if the hash of the expiry date is validated, False otherwise."""
        if self._expiry_date == '<<<<<<' and self._country == 'RUS':
            return True
        return self.report.add("expiry date hash", hash_is_ok(self._expiry_date, self._expiry_date_hash))
    



class T3CodeGeneratorUpdate(TD3CodeGenerator):
    def __init__(self,
                    document_type: str,
                    country_code: str,
                    surname: str,
                    given_names: str,
                    document_number: str,
                    nationality: str,
                    birth_date: str,
                    sex: str,
                    expiry_date: str,
                    optional_data="",
                    transliteration=dictionary.latin_based(),
                    force=False):
            self._country_code = country_code
            _TD3HolderName.__init__(self, surname, given_names, transliteration)
            self.force = force
            self.document_type = document_type
            self.country_code = country_code
            self.document_number = document_number
            self.nationality = nationality
            self.birth_date = birth_date
            self.sex = sex
            self.expiry_date = expiry_date
            self.optional_data = optional_data
    @property
    def expiry_date(self) -> str:
        """Return date of expiry of the document

        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value: str):
        """Set date of expiry of the MRTD with 'YYMMDD' format

        """
        
        self._expiry_date = date(value)
            
    
    @property
    def document_type(self) -> str:
        """Return document type code

        """
        return self._document_type

    @document_type.setter
    def document_type(self, value: str):
        """Set document type code

        For TD1 and TD2, the first letter must be 'I', 'A' or 'C'. Optionally, can be used a
        second character. The second character shall be at discretion of issuing state.
        Note: 'V' shall not be used as 2nd char and 'C' shall not be used after 'A'. (TD1 and TD2)

        First letter of passports and other TD3 must be 'P'. Optionally, can be used a second
        character. The second character shall be at discretion of issuing state

        For visas (MRV-A and MRV-B), the first letter must be 'V'. Optionally, can be used a
        second character. The second character shall be at discretion of issuing state

        Case insensitive.

        """
        try:
            self._document_type = check.document_type(value, self) if not self.force \
                else check.field(value, 2, "document type")
        except Exception as e:
            "<<<<<<<<<<<<<<<<"
            if value.upper() == 'PN' or value.upper() == 'PA' or value.upper() == 'P':
                self._document_type = value if len(value) == 2 else f"{value}<"
            else:
                raise e
        
    @property
    def expiry_date_hash(self) -> str:
        """Return hash digit of expiry date

        """
        return hash_string(self.expiry_date) if self._expiry_date != '<<<<<<' else '<'