import copy

from custom_mrz.t3 import TD3CodeCheckerIdictAll, T3CodeGeneratorUpdate
from custom_mrz.t2 import TD2CodeCheckerID_2, TD2CodeGenerator_ID2
from mrz.checker.td1 import TD1CodeChecker
from mrz.checker.td2 import TD2CodeChecker
from mrz.generator.td1 import TD1CodeGenerator
from mrz.generator.td2 import TD2CodeGenerator


class MrzClassGenerator:
    select_code_checker = None

    checker_to_generator = {
        TD1CodeChecker: TD1CodeGenerator,
        TD3CodeCheckerIdictAll: T3CodeGeneratorUpdate,
        TD2CodeCheckerID_2: TD2CodeGenerator_ID2,
        TD2CodeChecker: TD2CodeGenerator

    }

    def __init__(self, mrz_code: str,
                 document_type: str,
                 country_code: str,
                 document_number: str,
                 birth_date: str,
                 sex: str,
                 expiry_date: str,
                 nationality: str,
                 surname: str,
                 given_names: str,
                 optional_data1="",
                 optional_data2=""):

        self.mrz_generate_and_validate = []
        self.mrz_code = mrz_code
        self.document_type = document_type,
        self.country_code = country_code,
        self.document_number = document_number,
        self.birth_date = birth_date,
        self.sex = sex,
        self.expiry_date = expiry_date,
        self.nationality = nationality,
        self.surname = surname,
        self.given_names = given_names,
        self.optional_data1 = optional_data1
        self.optional_data2 = optional_data2

    def get_data(self):
        data = dict(document_type=self.document_type[0],
                    country_code=self.country_code[0],
                    document_number=self.document_number[0],
                    birth_date=self.birth_date[0],
                    sex=self.sex[0],
                    expiry_date=self.expiry_date[0],
                    nationality=self.nationality[0],
                    surname=self.surname[0],
                    given_names=self.given_names[0],
                    optional_data=self.optional_data1)

        if self.select_code_checker.__class__ == TD1CodeChecker:
            data['optional_data1'] = data.pop('optional_data')
            data['optional_data2'] = self.optional_data2

        return data

    def set_generator(self):
        data = self.get_data()
        generator = self.checker_to_generator[self.select_code_checker.__class__](**data)

        self.mrz_generate_and_validate.append({
            'mrz_code': self.mrz_code,
            'generated_mrz_code': str(generator),
            'status': str(generator) == self.mrz_code
        }
        )


class MrzCodeChecker(MrzClassGenerator):
    mrz_class_list = (TD1CodeChecker, TD3CodeCheckerIdictAll,
                      TD2CodeCheckerID_2, TD2CodeChecker)
    select_code_checker = None
    mrz_code = None

    valid = False
    mrz_generate_and_validate = None
    fields = {}

    def __init__(self, mrz_code: str, *args, **kwargs):
        self.mrz_generate_and_validate = []
        self.mrz_code = mrz_code
        super().__init__(mrz_code, *args, **kwargs)

    def set_code_checker(self):
        raw_select = None

        for mrz_checker in self.mrz_class_list:
            try:
                self.select_code_checker = mrz_checker

                self.validate_mrz_code()
                if self.valid:
                    return
                else:
                    raw_select = self.select_code_checker
            except Exception as e:
                ...
        if raw_select is not None:
            raise ValueError

    def validate_mrz_code(self):
        self.select_code_checker = self.select_code_checker(self.mrz_code)
        self.valid = bool(self.select_code_checker)
        print(self.valid)
        self.fields = self.select_code_checker.fields()._asdict()

    def __str__(self) -> str:
        return f"fields: {self.fields}, validate: {self.valid}"

    def print_table(self):
        for key, val in self.fields.items():
            print(f"{key} | {val}")
        try:
            data = self.select_code_checker.get_dict_all_fields()
            for key, val in data.items():
                print(f"{key} | {val}")
            print("validate_data")
            data = self.select_code_checker.get_dict_all_fields_validate()
            for key, val in data.items():
                print(f"{key} | {val}")
        except Exception as e:
            print(e)
        print(f"total_validate: {self.valid}")
        print(f"mrz {self.mrz_generate_and_validate}")

    def total_data(self):
        if self.select_code_checker is not None:
            return (self.fields.items() | self.select_code_checker.get_dict_all_fields() |
                    self.select_code_checker.get_dict_all_fields_validate() | {'valid': self.valid} |
                    {'mrz': self.mrz_generate_and_validate})


class MrzClass(MrzCodeChecker):
    """ 
    Класс необходимый для генерации/проверки/получения результатов по данным mrz
    """

    null_to_O = ["document_type", "country_code", "sex", "nationality", "surname", "given_names"]

    def __init__(self, mrz_code: str, document_type: str, country_code: str, document_number: str, birth_date: str,
                 sex: str, expiry_date: str, nationality: str, surname: str, given_names: str, optional_data1="",
                 optional_data2=""):
        data = self.base_replacement(mrz_code=mrz_code, document_type=document_type, country_code=country_code,
                                     document_number=document_number, birth_date=birth_date, sex=sex,
                                     expiry_date=expiry_date,
                                     nationality=nationality, surname=surname, given_names=given_names,
                                     optional_data1=optional_data1, optional_data2=optional_data2)

        super().__init__(**data)

    def base_replacement(self, **kwargs):
        """ Метод заменяет 0 на O и наоборот в зависимости от контекста """

        mrz_code = kwargs.pop('mrz_code')
        for key, value in kwargs.items():
            raw_value = copy.copy(value)
            if key in self.null_to_O:
                kwargs[key] = value.replace('0', 'O')
                print(raw_value)
                mrz_code = mrz_code.replace(raw_value, kwargs[key])
            else:
                kwargs[key] = value.replace('O', '0')
                mrz_code = mrz_code.replace(raw_value, kwargs[key])
        kwargs['mrz_code'] = mrz_code
        return kwargs
