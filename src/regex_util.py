# functions for regex based data parsing

import re
from constants import REGULAR_EXPRESSION

def extract_data_with_regex(text):
    pattern = re.compile(r"some_pattern")
    match = pattern.search(text)
    if match:
        return match.group()
        
    return None
