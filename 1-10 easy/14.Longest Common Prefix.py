# 一、从任意一个字符串开始，依次检查其他字符串的同一位置是否是一样的字符，当遇到不一样时则返回当前得到的前缀。
# def longestcommonprefix(strs):
#     if not strs:
#         return ''
#     res = ''
#     for i in range(len(strs[0])):
#         for j in range(1,len(strs)):
#             if strs[j][i] != strs[0][i] or i >= len(strs[j]):
#                 return res
#         res += strs[0][i]
#     return res
# 二、先对字符串数组排序，比较第一个与最后一个即可.实际上由于排序，效率并没有提高很多
def longestcommonprefix(strs):
    if not strs:
        return ''
    res = ''
    strs.sort()
    for i in range(len(strs[0])):
        if strs[-1][i] != strs[0][i] or i >= len(strs[-1]):
            return res
        res += strs[0][i]
    return res

print(longestcommonprefix(['asas','asd''asasaww']))