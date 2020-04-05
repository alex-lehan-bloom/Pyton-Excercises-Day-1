
error_message = "Need to enter an integer."
def is_even(num):
    try:
        int(num)
        if type(num) == float:
            print(error_message)
            exit()
        if num % 2 == 0:
            return True
        else:
            return False
    except Exception:
        print(error_message)
        exit()



print(is_even(10.5))
