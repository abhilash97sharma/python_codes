def cal(a, b):
    print('sum of the number is:', (a + b))
    print('sub of the number is:', (a - b))
    print('mul of the number is:', (a * b))
    print('div of the number is:', (a / b))
    return


cal(45, 6)


def cube(a):
    return a * a * a


num1 = int(input("Enter the no to be cube:"))
print('The cube of the ' + str(num1) + " is :", cube(num1))


def max_num(a, b, c):
    if a > b and a > c:
        print(str(a) + ' is greater')
    elif b > a and b > c:
        print(str(b) + " is greater")
    elif c > a and c > b:
        print(str(c) + " is greater")
    else:
        print("all no\'s are equal")


max_num(23, 23, 23)


# exponential function
def exp_fun(base, exp):
    a = 1;
    for index in range(exp):
        a = base * a
    return a


print(exp_fun(2, 3))
