
def build_pyramid_with_given_height_and_direction(height, direction="up"):
    if validate_height(height) == False:
        print("Error: Need to enter a positive integer.")
        exit()
    if validate_direction(direction) == False:
        print("Error: Direction can only be 'up' or 'down'.")
        exit()
    else:
        direction = direction.lower()
        if direction == "up":
            space = " "
            star = "*"
            times = height - 1
            for i in range(0, height):
                print(space * times + star)
                times -= 1
                star += "**"
        if direction == "down":
            space = " "
            star = "*" * (height * 2 - 1)
            times = 0
            for i in range(0, height):
                print(space * times + star)
                times += 1
                star = star[:-2]


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
        direction.lower()
        if (direction == "up" or direction == "down"):
            return True
        else:
            return False
    except:
        return False

build_pyramid_with_given_height_and_direction(6, "up")
build_pyramid_with_given_height_and_direction(6, "down")
