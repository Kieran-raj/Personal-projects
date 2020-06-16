import random
while True:
    words = ["python", "java", "kotlin", "javascript"]
    print("H A N G M A N")
    to_play = input("Type 'play' to play the game, 'exit' to quit:")
    tries = 8
    ran_word = random.choice(words)
    display = "-"*(len(ran_word))
    dashes = display
    not_in = []
    if to_play == "play":
        while True:
            ans = (''.join(display))
            print("Lives: " + str(tries))
            if ans == ran_word:
                print("You guessed the word " + ran_word + "!")
                print("You survived!\n")
                break
            else:
                print("\n" + ans)
            letter = input("Input a letter:")
            if letter == ran_word:
                print("You guess the word " + ran_word + "!")
                print("You survived \n")
                break
            if len(letter) != 1:
                print("You should input a single letter")
            else:
                if not letter.islower() or not letter.isascii():
                    print("It is not an ASCII lowercase letter")
                else:
                    if letter in ran_word:
                        if letter in display:
                            print("You already typed this letter")
                        else:
                            position = ran_word.index(letter)
                            position2 = ran_word.rindex(letter)
                            display = list(display)
                            display[position] = letter
                            display[position2] = letter
                    else:
                        if letter not in not_in:
                            print("No such letter in the word")
                            not_in.append(letter)
                            tries -= 1
                        else:
                            print("You already typed this letter")
            if tries == 0:
                print("You are hanged!\n")
                break
    else:
        break













