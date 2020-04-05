def build_pyramid_with_given_height_and_direction(height, direction="up"):
    direction = direction.lower()
    if validate_height(height) == False:
        print("Error: Need to enter a positive integer.")
    elif validate_direction(direction) == False:
        print("Error: Direction can only be 'up' or 'down'.")
    else:
        total_number_of_rows = height
        total_number_of_columns = total_number_of_rows * 2
        if direction == "up":
            start_position = total_number_of_rows - 1
            end_position = total_number_of_rows + 1
        else:
            start_position = 0;
            end_position = total_number_of_columns;
        for row in range(1, total_number_of_rows):
            if direction == "up":
                if row != 1:
                    start_position -= 1
                    end_position += 1
            else:
                if row != 1:
                    start_position += 1
                    end_position -= 1
            for column in range(1, total_number_of_columns):
                if column == total_number_of_columns - 1:
                    if row == total_number_of_rows:
                        print("*")
                        break
                    else:
                        print(" ")
                        break
                if (column > start_position) and (column < end_position):
                    print("*", end="")
                else:
                    print(" ", end="")


def validate_height(height):
    try:
        int(height)
        if height < 1 or type(height) == float:
            return False
        else:
            return True
    except:
        return False

def validate_direction(direction):
    try:
        direction.isalnum()
        if (direction == "up" or direction == "down"):
            return True
        else:
            return False
    except:
        return False


build_pyramid_with_given_height_and_direction(8, "down")
