from math import ceil
import os

cwd = os.getcwd()
input_txt = os.path.join(cwd, 'input.txt')


class Seat():

    def __init__(self, seat_string, num_rows=128, num_cols=8):
        self.input_string = seat_string
        self.num_rows = num_rows
        self.num_cols = num_cols

        def parse_index(self, index_type):

            if index_type == 'row':
                id_string = self.input_string[:-3]
                rear_char = 'B'
                front_char = 'F'
                valid_index = [i for i in range(self.num_rows)]
            elif index_type == 'col':
                id_string = self.input_string[-3:]
                rear_char = 'R'
                front_char = 'L'
                valid_index = [i for i in range(self.num_cols)]

            for char in id_string:
                halfway = ceil(len(valid_index) / 2)
                if char == rear_char:
                    valid_index = valid_index[halfway:]
                else:
                    valid_index = valid_index[:halfway]

            return valid_index[0]

        self.row = parse_index(self, 'row')
        self.col = parse_index(self, 'col')
        self.seat_id = self.row * 8 + self.col


def calc_my_seat(input_txt):
    with open(input_txt, newline='\n') as input_file:
        lst_data = input_file.read().splitlines()
    taken_seats = [Seat(i).seat_id for i in lst_data]
    poss_seats = [i for i in range(max(taken_seats)) if i not in taken_seats]

    def valid_untaken(seat):
        prev_seat = seat - 1
        next_seat = seat + 1
        if (prev_seat in taken_seats) and (next_seat in taken_seats):
            print(seat)
        else:
            pass

    [valid_untaken(i) for i in poss_seats]


if __name__ == '__main__':
    calc_my_seat(input_txt)
