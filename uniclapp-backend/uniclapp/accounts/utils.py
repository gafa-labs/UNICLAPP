import re


def validateHesCode(hes_code):
    return len(re.findall("[A-Q][0-9][A-Q][0-9]-[0-9]{4}-[0-9]{2}", hes_code)) == 1
