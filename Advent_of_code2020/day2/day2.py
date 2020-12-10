count = 0 
with open('input.txt','r') as f:
    for l in f.readlines():
        rules_str, letter_str, password_str = l.split(" ")
        rule_min, rule_max = [int(m) for m in rules_str.split("-")]
        letter = letter_str[0]
        password = password_str.strip()

        #letter_count = password.count(letter)

        #if letter_count in range(rule_min, rule_max + 1):
         #   count += 1
        
        if letter == password[rule_min - 1] and letter == password[rule_max - 1]:
            count += 0
        elif letter != password[rule_min-1] and letter != password[rule_max-1]:
            count += 0
        else:
            count += 1
print(count)










