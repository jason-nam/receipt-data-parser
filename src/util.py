# util functions

import csv

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        data = list(csv.reader(csvfile))
    return data