def build_pyramid():
    start_position = 3
    end_position = 5
    for row in range(0, 5):
        if row != 0:
            start_position -= 1
            end_position += 1
        for column in range(0, 9):
            if column == 8:
                if row == 4:
                    print("*")
                    break
                else:
                    print(" ")
                    break
            if (column > start_position) and (column < end_position):
                print("*", end="")
            else:
                print(" ", end="")


build_pyramid()
