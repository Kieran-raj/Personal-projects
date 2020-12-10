import os

with open('input2.txt' , 'r') as f:
    lines = f.readlines()


len_slope = len(lines)
#min_row_length = len_slope * 3
#for i in lines:
#    with open('input3.txt', 'a') as f2:
#       f2.write(i.strip() + (min_row_length * i.strip()) + i)


def input3(move):
    os.remove('input3.txt')
    min_row_length = len_slope * move
    for i in lines:
        with open('input3.txt', 'a') as f2:
            f2.write(i.strip() + (min_row_length * i.strip()) + i)


def read_input():
    with open('input3.txt', 'r') as f3:
        return f3.readlines()


right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]


ans = []
for r, d in zip(right, down):
    input3(r)
    start_position = 0
    num_open = 0
    num_trees = 0
    lines2 = read_input()
    for i in range(len(lines2)):
        random = i + (d - 1)

        if random < len(lines2):
            if lines2[random][start_position] == '.':
                num_open += 1
                start_position += r
            else:
                num_trees += 1
                start_position += r
    ans.append(num_trees)



final_ans = 1
for i in ans:
    final_ans *= i


print(ans)
print(final_ans)        

