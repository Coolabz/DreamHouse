sup_counter = 0
winner = 0
looser = 0
print(f"H A N G M A N  # 8 attempts")
while sup_counter < 2:
    import random

    def chosing(lst):
        return random.choice(lst)

    b = ["python", "java", "swift", "javascript", "telescope", "communication"]
    c = list(chosing(b))
    o = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >')
    if o == "play":
        pass
    elif o == "results":
        print(f"You won: {winner} times.")
        print(f"You lost: {looser} times.")
        continue
    else:
        break
    b = list(len(c) * "-")
    print(" ")
    print("".join(b))
    counter = 0
    attemps = 8
    x =[]
    while counter <= 200:
        b = list(b)
        g = input("Input a letter: > ")
        if len(g) > 1 or len(g) == 0:
            print("Please, input a single letter.")
            print(" ")
            print("".join(b))
            continue
        if g in "QWERTYUIOPASDFGHJKLZXCVBNM0123456789-!@#$%^&*()_+-=":
            print("Please, enter a lowercase letter from the English alphabet.")
            print(" ")
            print("".join(b))
            continue
        if g not in "qwertyuiopasdfghjklzxcvbnm":
            print("Please, input a single letter.")
            print(" ")
            print("".join(b))
            continue
        if x.count(g) > 0:
            print("You've already guessed this letter.")
            print(" ")
            print("".join(b))
            continue
        x.append(g)
        cou = 0
        q = 0
        w = 0
        for i in c:
            if g in c:
                if i == g:
                    b[cou] = g
                    cou = cou + 1
                    w = w + 1
                else:
                    cou = cou + 1
            else:
                if attemps - 1 ==0:
                    print(f"That letter doesn't appear in the word.  # {attemps - 1} attempts")
                    break
                else:
                    print(f"That letter doesn't appear in the word.  # {attemps - 1} attempts")
                    print(" ")
                    print("".join(b))
                    cou = cou + 1
                    q = q+1
                    break
        if q == 0:
            if attemps - 1 ==0:
                if g in c:
                    #print(f"{g}  # {attemps - 1} attempts")
                    print(" ")
                    print("".join(b))
                else:
                    print(f"{g}  # {attemps - 1} attempts")
            else:
                print(" ")
                print("".join(b))
        q = 0
        counter = counter + 1
        if b == c:
            b = "".join(b)
            print(f"You guessed the word {b}!")
            print("You survived!")
            winner = winner + 1
            break
        if attemps == 0:
            print(" ")
            print("You lost!")
            looser = looser + 1
            break
        if w > 0:
            continue
        attemps = attemps - 1
        if attemps == 0:
            print(" ")
            print("You lost!")
            looser = looser + 1
            break
