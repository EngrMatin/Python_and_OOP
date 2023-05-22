import mutate

def nearly_equal(a,b):
	return a in mutate.mutate(b)


if __name__ == '__main__':
	print (nearly_equal('helo','hello'))
	print (nearly_equal('hello','hel'))