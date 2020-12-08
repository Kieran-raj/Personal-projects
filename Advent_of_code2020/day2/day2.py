with open('input.txt', 'r') as f:
    lines = f.readlines()

dic = {}

for line in lines:
    element = line.strip().split()
    ranges = element[0].split('-')
    dic[element[2]] = [element[1][-2], ranges[0], ranges[1]] 

count = 0

for i in dic:
    num_letter = i.count(dic[i][0])
    if num_letter in range(int(dic[i][1]), (1 + int(dic[i][2]))):
        count += 1

print(count)
print(dic)
