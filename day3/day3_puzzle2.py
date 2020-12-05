import os
from math import ceil

cwd = os.getcwd()
input_txt = os.path.join(cwd, 'input.txt')

with open(input_txt, newline='\n') as input_file:
    lst_data = input_file.read().splitlines()


class CountCollisions():
    def __init__(self, input_data, horiz_shift, vert_shift=1):

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

        def check_collisions(self):
            tree_count = 0
            for i in range(self.req_steps):
                col = i * self.horiz_shift
                row = i * self.vert_shift
                if self.working_data[row][col] == '#':
                    tree_count += 1

            return tree_count

        self.horiz_shift = horiz_shift
        self.vert_shift = vert_shift
        self.working_data = multiply_df(input_data, horiz_shift, vert_shift)
        self.tree_count = check_collisions(self)

    def __mul__(self, other):
        return self.tree_count * other

    def __rmul__(self, other):
        return self * other


if __name__ == '__main__':
    r1d1 = CountCollisions(lst_data, horiz_shift=1, vert_shift=1)
    r3d1 = CountCollisions(lst_data, horiz_shift=3, vert_shift=1)
    r5d1 = CountCollisions(lst_data, horiz_shift=5, vert_shift=1)
    r7d1 = CountCollisions(lst_data, horiz_shift=7, vert_shift=1)
    r1d2 = CountCollisions(lst_data, horiz_shift=1, vert_shift=2)

    answer = r1d1 * r3d1 * r5d1 * r7d1 * r1d2
    print(answer)
