class targetSum:

    def twoSum(self, list1, target):
        dict1 = {}
        for i, x in enumerate(list1):
            if target-x in dict1:
                return (dict1[target-x], i)
            dict1[x] = i
              

list1 = [10,20,35,40,50,60,70]
target = 50

# print(targetSum().twoSum(list1, target))
result = targetSum().twoSum(list1, target)

for x in result:
    print(x, end=', ')