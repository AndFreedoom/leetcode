# solution 1:
def twosum( nums,target):
    for i, onenum in enumerate(nums):
        another = target - onenum
        if another in nums and i != nums.index(another):
            return [i, nums.index(another)]
# solution 2 :
def twosum(nums,target):
    dictn = {}
    for i, num in enumerate(nums):
        another = target - num
        if another in dictn:
            return [dictn[another], i]
        dictn[num] = i