file1 = '../source/atest.txt'
content_list = open(file1, 'r').readlines()

print(content_list[0:5])

for line in content_list:
    print(line)


file2 = open('../destination/copy.txt', 'w').writelines(content_list[0:5])

