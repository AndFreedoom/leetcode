# solution 1 :
def reverseint(x):
    if x < 0:
        new_x = -1 * int(str(-x)[::-1])
    else :
        new_x = int(str(x)[::-1])
    if new_x > 2**31-1 or new_x < -(2**31):
        new_x = 0
    return new_x






# solution 2 :
def reverseint(x):
    if x < 0:
        flag = -1
    else :
        flag = 1
    new_x = 0
    x = abs(x)
    while x :
        new_x = 10 * new_x + x % 10
        x = x // 10
    new_x = flag * new_x
    if new_x > (2**31-1) or new_x < -(2**31):
        new_x = 0
    return new_x

print(reverseint(287878787878978676778578))

