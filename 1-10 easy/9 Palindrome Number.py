#  一、这种写法最简单，但是有作弊之嫌。。。。
def ispalindromenumber(x):
    if x < 0 :
        return False
    return str(x) == str(x)[::-1]

# 二、将整数翻转，然后进行判断。python语言不需要考虑溢出，其他语言需要考虑溢出，另外其他语言如果溢出说明不是回文数。
def ispalindromenumber(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    temp = x
    new_x = 0
    while temp:
        new_x = 10 * new_x + temp % 10
        temp = temp//10
        print(1)
    return new_x == x

# 三、承接方法二,只需要翻转一半比较即可，
def ispalindromenumber(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    new_x = 0
    while x > new_x:
        new_x = new_x * 10 + x % 10
        x = x//10
    return new_x == x or new_x//10 == x
# 四、逐个比较收尾数字
def ispalindromenumber(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    digits = 1
    while x // digits >= 10:
        digits *= 10

    while digits > 1:
        right = x % 10
        left = x // digits
        if right != left:
            return False
        x = (x % digits)//10
        digits = digits//100
    return True



