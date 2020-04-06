

def solve_math(equation, *nums):
    for num in nums:
        try:
            int(num)
        except:
            print("Error: You can only numbers for the '*nums' argument.")
            exit()
    new_equation = ""
    index_of_nums = 0
    for char in equation:
        if index_of_nums == len(nums):
            print("Error: You didn't enter enough numbers.")
            exit()
        if char == "X" or char == "x":
            char = nums[index_of_nums]
            index_of_nums +=1
            new_equation += str(char)
        else:
            new_equation += str(char)
    print(new_equation)
    print(eval(new_equation))


solve_math("X*X+X*X*X",1,2,3,4,5)