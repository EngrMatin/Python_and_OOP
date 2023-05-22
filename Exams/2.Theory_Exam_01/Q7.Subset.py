class getSubset:
    def func1(self, list1):
        set1= set(list1)
        return self.func2([], sorted(set1))

    def func2(self, current, set1):
        if set1:
            set2 = self.func2(current, set1[1: ]) + self.func2(current + [set1[0]], set1[1: ])
            return set2

        return [current]

list1 = [4, 5, 6]
subsets = getSubset().func1(list1)
print(subsets)
