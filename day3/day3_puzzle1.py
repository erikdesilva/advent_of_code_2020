import os
from math import ceil

cwd = os.getcwd()
input_txt = os.path.join(cwd, 'input.txt')

with open(input_txt, newline='\n') as input_file:
    lst_data = input_file.read().splitlines()


class CountCollisions():
    def __init__(self, input_data, horiz_shift, vert_shift=1, start_pos=[0, 0]):

        def multiply_df(input_data, horiz_shift, vert_shift):
            output_data = input_data
            height = len(input_data)
            width = len(input_data[1])
            self.req_steps = ceil(height / vert_shift)
            while self.req_steps > (width / horiz_shift):
                add_zip = zip(output_data, input_data)
                output_data = [i[0] + i[1] for i in add_zip]
                height = len(output_data)
                width = len(output_data[1])

            self.df_height = len(output_data)
            return output_data

        self.horiz_shift = horiz_shift
        self.vert_shift = vert_shift
        self.start_pos = start_pos
        self.working_data = multiply_df(input_data, horiz_shift, vert_shift)
        self.tree_count = 0

    def check_collisions(self):
        start_pos = self.start_pos
        for i in range(self.req_steps):
            col = i * self.horiz_shift + start_pos[0]
            row = i * self.vert_shift + start_pos[1]
            if self.working_data[row][col] == '#':
                self.tree_count += 1


if __name__ == '__main__':
    instance = CountCollisions(lst_data, 3)
    instance.check_collisions()
    print(instance.tree_count)
