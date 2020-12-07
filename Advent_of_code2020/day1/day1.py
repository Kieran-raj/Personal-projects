from itertools import permutations 

with open('input.txt') as f:
    lines = f.readlines()

lst = []

for i in lines:
    lst.append(int(i.strip()))

perm = permutations(lst, 2)

ans = []
for i in set((perm)):
    if sum(list(i)) == 2020:
        for l in i:
            ans.append(l)


final_ans = 1
for i in set(ans):
    final_ans *= i

print(final_ans)