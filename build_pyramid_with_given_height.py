def build_pyramid_with_given_height(height):
    if validate_height(height) == False:
        print("Error: Need to enter a positive integer.")
    else:
        total_number_of_rows = height
        num_of_columns = total_number_of_rows * 2
        start_position = total_number_of_rows - 1
        end_position = total_number_of_rows + 1
        for row in range(1, total_number_of_rows):
            if row != 1:
                start_position -= 1
                end_position += 1
            for column in range(1, num_of_columns):
                if column == num_of_columns - 1:
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


build_pyramid_with_given_height(15)
