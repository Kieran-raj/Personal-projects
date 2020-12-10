import os
os.remove('input3.txt')

right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

with open('input.txt' , 'r') as f:
    lines = f.readlines()


len_slope = len(lines)
min_row_length = len_slope * 3
os.remove('input3.txt')
for i in lines:
    with open('input3.txt', 'a') as f2:
        f2.write(i.strip() + (min_row_length * i.strip()) + i)


with open('input3.txt', 'r') as f3:
    lines2 = f3.readlines()
    ans = []
    num_open = 0
    num_trees = 0
    right = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]
    # for r, d in zip(right, down):
    start_position = 0
    num_open = 0
    num_trees = 0
    for i in range(len(lines2)):
        random = i + (d - 1)
        if random <= len(lines2):
            if lines2[random][start_position] == '.':
                num_open += 0
                start_position += r
            else:
                num_trees += 1
                start_position += r
    ans.append(num_trees)

count_trees = 1
for i in ans:
    count_trees *= i


print(count_trees)



        
