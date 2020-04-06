import math


def list_square_even_power_odd(max_num):
    try:
        validate_argument(max_num)
        unmodified_list = [num for num in range(0, max_num)]
        modified_list = [float(format(math.sqrt(num), ".2f")) if num % 2 == 0 else math.pow(num, 2) for num in
                         range(0, max_num)]
        print("Unmodified list: " + str(unmodified_list))
        print("Modified list: " + str(modified_list))
    except Exception as e:
        print(e.args[0])


def validate_argument(argument):
    if str(argument).isdigit():
        return True
    else:
        raise ValueError("Error: Enter a positive integer.")


list_square_even_power_odd(10)
