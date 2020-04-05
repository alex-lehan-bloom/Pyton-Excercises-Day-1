

def is_parsable(user_input):
    if is_num(user_input) or is_string(user_input):
        return True
    else:
        return False


def is_num(user_input):
    try:
        int(user_input)
        if type(user_input) == float:
            return False
        else:
            return True
    except:
        return False


def is_string(user_input):
    try:
        user_input.isalnum()
        return True
    except:
        return False


print(is_parsable(10))
print(is_parsable("test string"))
print(is_parsable(10.5))


