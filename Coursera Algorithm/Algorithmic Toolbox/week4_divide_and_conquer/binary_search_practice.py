def binary_search_recursive(array,item,high,low):
	if low > high:
		return "ELEMENT NOT FOUND"
	mid = low + (high-low)//2
	if array[mid]==item:
		 print("array[{}] = {}".format(mid,array[mid]))
		 return mid
	elif array[mid]<item:
		return binary_search_recursive(array,item,high,mid+1)
	else:
		return binary_search_recursive(array,item,mid-1,low)

def binary_search_iterative(array,item,high,low):
	while True:
		if low>high:
			return "ELEMENT NOT FOUND"
		mid = low + (high-low)//2
		if array[mid]==item:
			return mid
		elif array[mid] < item:
			low = mid+1
		else:
			high = mid-1





if __name__=='__main__':
	out = binary_search_recursive([1,4,7,8,20,34,35,40],60,7,0)
	out_it = binary_search_iterative([1,4,7,8,20,34,35,40],1,7,0)
	print(out)
	print(out_it)