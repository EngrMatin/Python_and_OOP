from itertools import permutations

def anagrams(list1):
    dict1 = {}
    while len(list1)>0:
        x = list1.pop()
        dict1[x] = dict1.get(x, [])
        dict1[x].append(x)

        i = 0
        while i<len(list1):
            word = list1[i]
            word_list = [''.join(p) for p in permutations(x)]
            if word in word_list:
                list1.remove(word)
                dict1[x].append(word)
            else:
                i += 1

    new_list = []
    for w in dict1.values():
        new_list.append(w)

    return new_list


result = anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
print(result)


