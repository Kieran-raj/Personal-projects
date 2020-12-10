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
    num_open = 0
    num_trees = 0
    lines2 = read_input()
    if start_position == 0:
        num = 0
    else:
        num = d
    for i in range(len(lines2)):
        random = i + num
        if random < len(lines2):
            if lines2[random][start_position] == '.':
                num_open += 1
                start_position += r
            else:
                num_trees += 1
                start_position += r
    return num_trees

print(get_ans(1, 1) * get_ans(3, 1) * get_ans(5, 1) * get_ans(7, 1) * get_ans(1, 2))





