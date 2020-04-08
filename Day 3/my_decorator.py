

def my_decorator(function):
    print("---------------------------------------")
    print(function)
    print("---------------------------------------")


def hello():
    return "hello ITC"


my_decorator(hello())