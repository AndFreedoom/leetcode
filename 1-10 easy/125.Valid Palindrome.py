
# 一、将所有字母都转成小写，过滤掉其他字符得到新字符串；再按照“回文”的定义，判断处理后的字符串正序反序是否一致。
def isvalidpalindrome(s):
    cleanlist = [c for c in s.lower() if c.isalnum()]
    length = len(cleanlist)
    for i in range(0, length//2):
        if cleanlist[i] != cleanlist[length-i-1]:
            return False
    return True
# 二、直接利用python切片
def isvalidpalindrome(s):
    cleanlist = [c for c in s.lower() if c.isalnum()]
    return cleanlist == cleanlist[::-1]
