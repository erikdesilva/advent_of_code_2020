import os
from re import findall, match
import pandas as pd

cwd = os.getcwd()
input_txt = os.path.join(cwd, 'input.txt')


class VerifyPassports():

    def __init__(self, input_text):

        with open(input_txt, newline='\n') as input_file:
            lst_data = ''.join(input_file.read()).split('\n\n')
            self.lst_data = [i.replace('\n', ' ') for i in lst_data]

        self.passport_params = {
            'byr': [1920, 2002],
            'iyr': [2010, 2020],
            'eyr': [2020, 2030],
            'hgt': {'cm': [150, 193],
                    'in': [59, 76]},
            'hcl': '\#[0-9a-f]{6}',
            'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            'pid': '^[0-9]{9}$'
        }

        self.range_params = ['byr', 'iyr', 'eyr']
        self.regex_params = ['pid', 'hcl']

    def check_params(self, pass_dict):
        fields_valid = {}
        for field in self.passport_params.keys():
            try:
                field_val = pass_dict[field]
                field_params = self.passport_params[field]

                if field in self.range_params:
                    min_val = field_params[0]
                    max_val = field_params[1]
                    value = int(field_val)
                    fields_valid[field] = (
                        value >= min_val) and (value <= max_val)
                elif field in self.regex_params:
                    fields_valid[field] = bool(match(field_params, field_val))
                elif field == 'ecl':
                    fields_valid[field] = bool(field_val in field_params)
                elif field == 'hgt':
                    try:
                        hgt_tup = findall('([0-9]{2,3})(cm|in)', field_val)[0]
                        units = hgt_tup[1]
                        height = int(hgt_tup[0])
                        min_hgt = field_params[units][0]
                        max_hgt = field_params[units][1]
                        fields_valid[field] = (
                            height >= min_hgt) and (height <= max_hgt)
                    except IndexError:
                        fields_valid[field] = False

            except KeyError:
                fields_valid[field] = False

        result = (all(fields_valid.values()) == True)
        if result == True:
            return 1
        else:
            return 0

    def string_to_dict(self, string):
        tuples = findall('([a-z]{3}):(\#?[a-z0-9]+)', string)
        passport_dict = {}
        for item in tuples:
            passport_dict[item[0]] = item[1]

        return passport_dict

    def iterate_passports(self):
        self.valid_count = 0
        for row in self.lst_data:
            row_dict = self.string_to_dict(row)
            self.valid_count += self.check_params(row_dict)
        return self.valid_count


if __name__ == '__main__':
    instance = VerifyPassports(input_txt)
    print(instance.iterate_passports())
