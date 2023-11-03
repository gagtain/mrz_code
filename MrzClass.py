from custom_mrz.t3 import TD3CodeCheckerIdictAll, T3CodeGeneratorUpdate
from custom_mrz.t2 import TD2CodeCheckerID_2
from mrz.checker.td1 import TD1CodeChecker
from mrz.checker.td2 import TD2CodeChecker
from mrz.checker.td1 import TD1CodeChecker
from mrz.generator.td1 import TD1CodeGenerator
from mrz.generator.td3 import TD3CodeGenerator


class MrzClass:
    """ 
    Класс необходимый для генерации/проверки/получения результатов по данным mrz
    """

    mrz_class_list = (TD1CodeChecker, TD3CodeCheckerIdictAll, TD2CodeChecker, TD2CodeCheckerID_2)
    select_code_checker = None
    mrz_code = None

    valid = False
    mrz_generate_and_validate = None
    fields = []


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
        self.set_code_checker()
        if self.select_code_checker == TD1CodeChecker:
            generator = TD1CodeGenerator(document_type,
                 country_code,
                 document_number,
                 birth_date,
                 sex,
                 expiry_date,
                 nationality,
                 surname,
                 given_names,
                 optional_data1,
                 optional_data2)
        elif self.select_code_checker.__class__ == TD3CodeCheckerIdictAll:

            generator = T3CodeGeneratorUpdate(document_type=document_type,
                 country_code=country_code,
                 document_number=document_number,
                 birth_date=birth_date,
                 sex=sex,
                 expiry_date=expiry_date,
                 nationality=nationality,
                 surname=surname,
                 given_names=given_names,
                 optional_data=optional_data1)
        self.mrz_generate_and_validate.append({
            'mrz_code': mrz_code,
            'generated_mrz_code': str(generator),
            'status': str(generator) == mrz_code
        }
        )


    def set_code_checker(self):
        for mrz_checker in self.mrz_class_list:
            try:
                self.select_code_checker = mrz_checker
                self.validate_mrz_code()
                print(mrz_checker)
                return
            except Exception as e:
                print(e)
        print(str(self))
        raise ValueError
        
    def validate_mrz_code(self):
        self.select_code_checker = self.select_code_checker(self.mrz_code)
        self.valid = bool(self.select_code_checker)
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


