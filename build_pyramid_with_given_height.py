def build_pyramid_with_given_height(height):
    if validate_height(height) == False:
        print("Error: Need to enter a positive integer.")
    else:
        space = " "
        star = "*"
        times = height
        for i in range(0, height):
            print(space * times + star)
            times -= 1
            star += "**"


def validate_height(height):
    try:
        int(height)
        if height < 1 or type(height) == float:
            return False
        else:
            return True
    except:
        return False


build_pyramid_with_given_height(10)
