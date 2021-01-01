list1 = [5,7,10,12,16,11,19,20,21,25,28,30]

def binarySearch(target):
	low = 0
	high = len(list1)

	while(low <= high):
		middle = int((low + high) / 2)

		if(target == list1[middle]):
			return middle
	
		elif(target > list1[middle]):
			low = middle + 1
		else :
			high = middle - 1


print(binarySearch(16))
