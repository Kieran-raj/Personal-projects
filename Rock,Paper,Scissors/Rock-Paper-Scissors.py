import random


def get_scoreboard():
    with open('rating.txt', 'r') as scores:
        current_score = "Current Scoreboard:"
        print(current_score)
        print(len(current_score)*"-")
        for score in scores.readlines():
            print(score.strip())


name = input("Enter you name:")
out_tofile = []
d = {}
file = open('rating.txt', 'r')
for line in file:
    (key, val) = line.split()
    d[key] = int(val)
    if not key == name:
        out_tofile.append(line)
file.close()
while True:  # number 1
    print("Hello, " + name)
    if name in d:
        score = d[name]
    else:
        score = 0
    mode = input("""Input an odd number of unusual objects
or press 'Enter' to play classic Rock, Paper, Scissors: """)
    print("Okay, let's start")
    while True:  # random items with unusual rules (normal rules not included)
        if mode == '':
            mode = 'rock,paper,scissors'
        ans = input().lower()
        if ans == "scoreboard":
            get_scoreboard()
        elif ans == "rating":
            print(f"Your rating: {score}")
        elif ans == "exit":
            file = open('rating.txt', 'w')
            file.writelines(out_tofile)
            file.close()
            profile = f"{name} {score}"
            file = open('rating.txt', 'a')
            print(profile, file=file, sep="\n")
            file.close()
            print("Bye")
            break
        elif ans not in mode:
            print("Invalid input")
        else:
            options = mode.split(',')
            computer_choice = random.choice(options)
            index = options.index(ans)
            positions = options[0:index]
            rpositions = options[index + 1::]
            final_list = rpositions + positions
            elements = len(final_list)
            slice_index = int(elements/2)
            beaten_by = final_list[0:slice_index]
            if computer_choice in beaten_by:
                print(f"Sorry, but the computer chose {computer_choice}")
            elif ans == computer_choice:
                score += 50
                print(f"There is a draw {ans}")
            else:
                score += 100
                print(f"Well done. Computer chose {computer_choice} and failed")
    break

