import csv
from pathlib import Path
from itertools import permutations
from functools import reduce

pth_input_dir = Path(r'C:\Users\EDeSilva\Documents\AoC\1')
pth_input_txt = pth_input_dir / 'input.txt'

def multiply_entries(input_txt_path, num_permutations=2, year=2020):
    with open(input_txt_path, newline='') as f:
        reader = csv.reader(f)
        lst_data = [int(i[0]) for i in reader]

    lst_perms = permutations(lst_data, num_permutations)

    for perm in lst_perms:
        if sum(perm) == year:
            print(reduce((lambda x, y: x * y), perm))
            break

multiply_entries(pth_input_txt, 4)