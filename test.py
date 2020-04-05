def is_parsable(input):
    if isinstance(input, int) or input.isdigit() == True:
        print("True")
    else:
        raise ValueError("cant be parsed")


def second(input1):
    try:
        is_parsable(input1)
    except Exception as e:
        print(e.args[0])


second("1a23")