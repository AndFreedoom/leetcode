'''统计一篇英文文档中，某些单词出现的次数。单词存放在一个列表中'''
import re
import operator

def wordfre(wordlist,filename):
    with open(filename) as fr:
        file = fr.read()            # read返回的是字符串
        fulltxt = [word for word in re.split(r'\W*',file) if len(word) > 3]   # 对字符串切分，返回列表

    wordcount = {}
    for word in wordlist:
        # wordcount[word] = fulltxt.count(word)
        # wordcount[word] = wordcount.get(word, 0) + 1     #这三种写法一个效果
        if word not in fulltxt:
            wordcount[word] = 0
        wordcount[word] += 1

    sortedwordcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedwordcount
# 修改一下，即可变成统计一篇文档中所有单词出现的次数，


