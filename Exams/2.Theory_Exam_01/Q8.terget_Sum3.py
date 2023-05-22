class targetSum(object):

    def twoSum(self, list1, target):
        dict1 = dict()
        idx = 0

        while idx < len(list1):
            if target-list1[idx] not in dict1:
                dict1[list1[idx]] = idx
                idx += 1
            else:
                return [dict1[target-list1[idx]], idx]
              

list1 = [10,20,10,40,50,60,70]
target = 50

result = targetSum().twoSum(list1, target)
# print(result)

for x in result:
    if x != result[-1]:
        print(x+1, end=', ')
    else:
        print(x+1)