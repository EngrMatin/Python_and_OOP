def center_align(filename):
	lines = open(filename, 'r').readlines()
	x = len(min(lines))
	
	# print(max(lines))                            # will print the smallest line
	# print('len(max(lines)): ', len(max(lines)))  # outpuy: len(max(lines)):  42
	
	# print(min(lines))                            # will print the largest line
	# print('len(min(lines)): ', len(min(lines)))  # outpuy: len(min(lines)):  47

	for line in lines:
		p = int((x-len(line))/2)
		print(' ' * p + line) 
        

center_align('poem.txt')