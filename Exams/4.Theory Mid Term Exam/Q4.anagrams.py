from itertools import permutations

def anagrams(x):
        dict1 = {}
        while len(x)>0:
                x1 = x.pop()
                dict1[x1] = dict1.get(x1,[])
                dict1[x1].append(x1)

                i = 0
                while i<len(x):
                        word = x[i]
                        perm = [''.join(p) for p in permutations(x1)]
                        if word in perm:
                                x.remove(word)
                                dict1[x1].append(word)
                        else:
                                i=i+1
        return dict1.values()

print(anagrams(['tae','souep','eat','ihba','node','peuos','ate','abhi','bhia','done','tea','soupe']))
result = anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
print(result)