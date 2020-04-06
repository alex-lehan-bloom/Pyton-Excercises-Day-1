
def build_pyramid():
    space = " "
    star = "*"
    times = 4
    for i in range(0, 5):
        print(space*times + star)
        times -= 1
        star += "**"

build_pyramid()
