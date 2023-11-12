# parsing csv file

import csv

from group_item import group_item_receipt
from regex_util import extract_data_with_regex
from llm_util import extract_data_with_llm
from constants import CSV_FILE_PATH

def parse_receipt_data(file_path):
    with open(file_path, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            text = row[4]
            extracted_data = extract_data_with_regex(text)

            # if not extracted_data:
            #     extracted_data = extracted_data_with_llm(text)
                
            #TODO

if __name__ == "__main__":
    path = CSV_FILE_PATH + "PXL_20231106_204751723.csv"
    parse_receipt_data(path)