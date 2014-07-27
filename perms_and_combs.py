def permuations(pstring, keys, endIndex):
	if endIndex == 1:
		print pstring + str(keys[0])

	else:
		for i in range(0, endIndex):
			swap(keys, i, endIndex - 1) 
			permuations(pstring + str(keys[endIndex -1]), keys, endIndex -1)
			swap(keys, i, endIndex - 1) 


def combinations(pstring, size, counter):
	pass

def swap(array, i1, i2):
	temp = array[i1]
	array[i1] = array[i2]
	array[i2] = temp


test = [1,2,3,4]
permuations('', test, len(test) )