from webclient import *
import json
from dotenv import load_dotenv
import os

class MrzReader:
    """ is a high-level class for obtaining and saving data with api """


    def __init__(self) -> None:

        load_dotenv()

        self.response: RecognitionResponse = None
        self.data = {}
        self.input_image = None


    def send(self):
        self.get_image()
        with DocumentReaderApi(host='https://api.regulaforensics.com/') as api:
            params = ProcessParams(
                scenario=Scenario.FULL_PROCESS,
                result_type_output=[Result.DOCUMENT_IMAGE, Result.STATUS, Result.TEXT, Result.IMAGES]
            )
            request = RecognitionRequest(process_params=params, images=[self.input_image])
            self.response = api.process(request)


    def get_image(self):
        with open(os.getenv("FILE"), "rb") as f:
            self.input_image = f.read()


    def init_data(self):

        for i in TextFieldType.allowable_values:
            field = self.response.text.get_field(i)
            if field is not None:
                self.data[field.field_name] = {
                    "value": field.get_value(),
                    "valid_mrz": field.source_validity(Source.MRZ),
                    "valid_vis": field.source_validity(Source.VISUAL)
                }


    def write_data(self):
        with open(os.getenv("input_file"), "w") as f:
            f.write(json.dumps(self.data))
    
if __name__ == "__main__":
    mrz_reader = MrzReader()
    mrz_reader.send()
    mrz_reader.init_data()
    mrz_reader.write_data()