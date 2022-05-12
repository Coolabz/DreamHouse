x = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print("---------")
print(f"| {x[0]} {x[1]} {x[2]} |")
print(f"| {x[3]} {x[4]} {x[5]} |")
print(f"| {x[6]} {x[7]} {x[8]} |")
print("---------")
c = [x[d:d+3] for d in range(0, len(x) - 2, 3)]
counter_22 = 0
counter = 0

while counter == 0:
    a = input("Enter the coordinates:")
    d = a.replace(" ", "")
    if d.isdigit():
        True
    else:
        print("You should enter numbers!")
        continue
    first_cor = int(a[0]) - 1
    second_cor = int(a[2]) - 1
    if first_cor > 2 or second_cor > 2:
        print("Coordinates should be from 1 to 3!")
        continue
    if c[first_cor][second_cor] == " ":
        if counter_22 % 2 == 0:
            c[first_cor][second_cor] = "X"
            counter_22 = counter_22 + 1
        else:
            c[first_cor][second_cor] = "O"
            counter_22 = counter_22 + 1
    else:
        print("This cell is occupied! Choose another one!")
        continue

    print("---------")
    print(f"| {c[0][0]} {c[0][1]} {c[0][2]} |")
    print(f"| {c[1][0]} {c[1][1]} {c[1][2]} |")
    print(f"| {c[2][0]} {c[2][1]} {c[2][2]} |")
    print("---------")

    if c[0][0] == c[0][1] == c[0][2] and c[0][0] != " ":
        print(f"{c[0][0]} wins")
        break
    elif c[1][0] == c[1][1] == c[1][2] and c[1][0] != " ":
        print(f"{c[1][0]} wins")
        break
    elif c[2][0] == c[2][1] == c[2][2] and c[2][0] != " ":
        print(f"{c[2][0]} wins")
        break
    elif c[0][0] == c[1][0] == c[2][0] and c[0][0] != " ":
        print(f"{c[0][0]} wins")
        break
    elif c[0][1] == c[1][1] == c[2][1] and c[0][1] != " ":
        print(f"{c[[0][1]]} wins")
        break
    elif c[0][2] == c[1][2] == c[2][2] and c[0][2] != " ":
        print(f"{c[0][2]} wins")
        break
    elif c[0][0] == c[1][1] == c[2][2] and c[0][0] != " ":
        print(f"{c[0][0]} wins")
        break
    elif c[0][2] == c[1][1] == c[2][0] and c[0][2] != " ":
        print(f"{c[0][2]} wins")
        break
    else:
        if c[0].count(" ") + c[1].count(" ") + c[2].count(" ") == 0:
            print("Draw")
        else:
            continue
    if c.count(" ") == 0:
        counter = counter +1

