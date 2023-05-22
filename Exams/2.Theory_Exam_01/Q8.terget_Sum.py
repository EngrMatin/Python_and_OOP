class targetSum:
    def __init__(self, list1, target):
        self.list1 = list1
        self.target = target

    def twoSum(self):
        for i in range(len(list1)-1):
            for j in range(i+1, len(list1)):
                if list1[i]+list1[j] == self.target:
                    index = i, j

                    return index

        return -1

list1 = [10,20,10,40,50,60,70]
target = 50

obj = targetSum(list1, target)
result = obj.twoSum()

for x in result:
    print(x, end=' ')

                