players = {1: "", 2: ""}
while players[1] not in ["X", "O"]:
    players[1] = input("X or O? ")

if players[1] == "X":
    players[2] = "O"
else:
    players[2] = "X"

line = "*************"
division = "*   *   *   *"

points = {
    1: (10, 2),
    2: (10, 6),
    3: (10, 10),
    4: (6, 2),
    5: (6, 6),
    6: (6, 10),
    7: (2, 2),
    8: (2, 6),
    9: (2, 10),
}


def print_field():
    for row in range(0, 13):
        if row % 4 == 0:
            print(line)
        else:
            row_steps = list(filter(lambda step: step[1][0] == row, steps))
            if len(row_steps) != 0:
                answer = division
                for row_step in row_steps:
                    answer = (
                        answer[: row_step[1][1]]
                        + row_step[0]
                        + answer[row_step[1][1] + 1 :]
                    )
                print(answer)
            else:
                print(division)


def check():
    return True


# steps = [("X", points[1]), ("O", points[5]), ("X", points[9])]
# steps = {1:"X",2:"O"}
steps = []
curPlayer = 1
while check():
    turn = 0
    while turn not in range(1, 10) and steps:
        turn = int(input("Player #{}, please, endter a num from 1 to 9 ".format(curPlayer)))
    steps.append((players[curPlayer], points[turn]))
    print_field()
    if curPlayer == 1:
        curPlayer = 2
    else:
        curPlayer = 1
else:
    pass

print_field()
