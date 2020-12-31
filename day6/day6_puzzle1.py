import os
from re import sub

cwd = os.getcwd()
input_txt = os.path.join(cwd, 'input.txt')


class CalcGroupQuestions():

    def __init__(self, input_txt):

        with open(input_txt, newline='\n') as input_file:
            lst_data = input_file.read().split('\n\r\n')
            lst_data = [sub('\r|\n', '', i) for i in lst_data]

        def count_unique(answers):
            unique_list = []
            for i in answers:
                if i not in unique_list:
                    unique_list += [i]
                else:
                    pass
            return len(unique_list)

        self.group_sums = [count_unique(i) for i in lst_data]

    def total_sum(self):
        return sum(self.group_sums)


if __name__ == '__main__':
    my_inst = CalcGroupQuestions(input_txt)
    print(my_inst.total_sum())
