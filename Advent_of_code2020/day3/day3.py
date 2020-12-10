### Needed a little help with part 2 unfortunately :(((( ###

import os

with open('input.txt' , 'r') as f:
    lines = f.readlines()

len_slope = len(lines)


def input3(move):
    os.remove('input3.txt')
    min_row_length = len_slope * move
    for i in lines:
        with open('input3.txt', 'a') as f2:
            f2.write(i.strip() + (min_row_length * i.strip()) + i)


def read_input():
    with open('input3.txt', 'r') as f3:
        return f3.readlines()


def get_ans(r, d):
    ans = []
    input3(r)
    start_position = 0
    down_position = 0
    num_open = 0
    num_trees = 0
    lines2 = read_input()
    while down_position < len(lines2):
        if lines2[down_position][start_position] == '.':
            num_open += 1
            start_position += r
            down_position += d
        else:
            num_trees += 1
            start_position += r
            down_position += d
    return num_trees


print(get_ans(1, 1) * get_ans(3, 1) * get_ans(5, 1) * get_ans(7, 1) * get_ans(1, 2))




