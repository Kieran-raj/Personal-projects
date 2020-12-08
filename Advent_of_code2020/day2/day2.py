with open('input2.txt', 'r') as f:
    lines = f.readlines()
    count = 0

    dic = {}

    for line in lines:
        element = line.strip().split()
        ranges = element[0].split('-')
        dic[element[2]] = [element[1][-2], ranges[0], ranges[1]] 

    for i in dic:
        print(i)
        min_ = int(dic[i][1])
        max_ = 1 + int(dic[i][2])
        print(dic[i][0])
        num_letter = i.count(dic[i][0])
        ranges = range(min_, (max_))
        if num_letter in ranges:
            #count += 1
            print('yes', num_letter)
        else:
            print('no', num_letter)

#print(count)


#count = 0 
#with open('input.txt','r') as f:
#    for l in f.readlines():
#        rules_str, letter_str, password_str = l.split(" ")
#        rule_min, rule_max = [int(m) for m in rules_str.split("-")]
#        letter = letter_str[0]
#        password = password_str.strip()
#
#
#        letter_count = password.count(letter)
#        if letter_count in range(rule_min, rule_max + 1):
#            #count += 1
#            print('yes')
#        else:
#            print('no')

#print(count)









