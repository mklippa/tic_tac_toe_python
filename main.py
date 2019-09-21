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

# steps = [("X", points[1]), ("O", points[5]), ("X", points[9])]
# steps = {5: 1, 6: 2}


def print_field():
    for row in range(0, 13):
        if row % 4 == 0:
            print(line)
        else:
            positions = list(
                filter(lambda position: points[position][0] == row, steps.keys())
            )
            if len(positions) != 0:
                answer = division
                for position in positions:
                    point = points[position]
                    letter = players[steps[position]]
                    answer = answer[: point[1]] + letter + answer[point[1] + 1 :]
                print(answer)
            else:
                print(division)


def check():
    return True


steps = {}
curPlayer = 1
while check():
    turn = 0
    while turn not in range(1, 10) or turn in steps.keys():
        turn = int(
            input("Player #{}, please, endter a num from 1 to 9 ".format(curPlayer))
        )
    steps[turn] = curPlayer
    print_field()
    if curPlayer == 1:
        curPlayer = 2
    else:
        curPlayer = 1
else:
    pass

print_field()
