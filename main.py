# first_sign = ""
# while first_sign not in ["X", "O"]:
#     first_sign = input("X or O? ")
# print("Congrats!")

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

steps = [("X", points[1]), ("O", points[5]), ("X", points[9])]


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

print_field()