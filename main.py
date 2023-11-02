from mrz.checker.td3 import TD3CodeChecker
from mrz.checker.td1 import TD1CodeChecker
from mrz.checker.td2 import TD2CodeChecker
import json

from MrzClass import MrzClass


def load_data(filename):
    with open(filename) as f:
        data = f.read()
    return json.loads(data)


def get_mrz_in_json(json: dict):
    return json['result'][0].get('value').replace('^', '\n')



def mrz_checker_from_mrz(mrz: str):
    list_mrz = [TD1CodeChecker, TD3CodeChecker, TD2CodeChecker]
    for mrz_checker in list_mrz:
        try:
            print(mrz_checker)
            return mrz_checker(mrz)
        except:
            ...
    raise ValueError

def main(mrz_coder):
    checker_passport = mrz_checker_from_mrz(mrz_coder)
    print(checker_passport.document_type)
    fields_passport = checker_passport.fields()
    print(checker_passport)
    print("fields")
    for key, value in fields_passport._asdict().items():
        print(f"{key} : {value}")
    print(len(fields_passport._asdict()))



if __name__ == '__main__':

    json_mrz_data = load_data('MRZ/2x36/1.json')
    mrz = get_mrz_in_json(json=json_mrz_data)
    mrz_class = MrzClass(mrz)
    mrz_class.print_table()