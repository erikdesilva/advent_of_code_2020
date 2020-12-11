import os
from re import sub

cwd = os.getcwd()
input_txt = os.path.join(cwd, 'input.txt')


class CalcGroupQuestions():

    def __init__(self, input_txt):

        with open(input_txt, newline='\n') as input_file:
            lst_data = input_file.read().split('\n\n')
            lst_data = [sub('\r', '', i) for i in lst_data]
            lst_data = [i.split('\n') for i in lst_data]

        def count_duplicates(answer):
            joined_answer = ''.join(answer)
            unique_list = []
            for i in joined_answer:
                if i not in unique_list:
                    unique_list += [i]
                else:
                    pass

            answer_dict = {}
            for i in unique_list:
                answer_dict[i] = joined_answer.count(i)
            answer_dict = {i: j for i, j in answer_dict.items()
                           if j == len(answer)}
            return len(answer_dict)

        self.group_sums = [count_duplicates(i) for i in lst_data]

    def total_sum(self):
        return sum(self.group_sums)


if __name__ == '__main__':
    my_inst = CalcGroupQuestions(input_txt)
    print(my_inst.total_sum())
