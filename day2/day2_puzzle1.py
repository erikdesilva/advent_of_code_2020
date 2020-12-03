import os

cwd = os.getcwd()
input_txt = os.path.join(cwd, 'input.txt')


class findAcceptedPasswords():

    def __init__(self, input_txt):

        def parse_data(input_txt):
            with open(input_txt, newline='\n') as input_file:
                lst_data = input_file.read().splitlines()
                dct_passwords = {}
                pass_id = 0
                for i in lst_data:
                    params = i.split(': ')[0]
                    char_range = [int(i)
                                  for i in params.split(' ')[0].split('-')]
                    target = params.split(' ')[1]
                    password = i.split(': ')[1]
                    dct_passwords[pass_id] = {'password': password,
                                              'target': target,
                                              'char_range': char_range}
                    pass_id += 1
                return dct_passwords

        self.input_data = parse_data(input_txt)
        self.accepted_passwords = {}
        self.num_accepted = None

    def append_valid(self):
        for pass_id, values in self.input_data.items():
            letter_count = 0
            for char in range(len(values['password'])):
                if values['password'][char] == values['target']:
                    letter_count += 1
                else:
                    pass

            if letter_count >= values['char_range'][0] and letter_count <= values['char_range'][1]:
                self.input_data[pass_id]['accepted'] = True
                self.accepted_passwords[pass_id] = self.input_data[pass_id]
            else:
                self.input_data[pass_id]['accepted'] = False

        self.num_accepted = len(self.accepted_passwords)


if __name__ == '__main__':
    instance = findAcceptedPasswords(input_txt=input_txt)
    instance.append_valid()
    print(instance.num_accepted)
