# Uses python3
import sys

def binary_search(a, x,high,low):
    #left, right = 0, len(a)-1
    # write your code here
    if high<low:
        return -1
    mid = low + (high-low)//2
    if a[mid]==x:
        return mid
    elif a[mid] < x:
        return binary_search(a,x,high,mid+1)
    else :
        return binary_search(a,x,mid-1,low)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def binary_search_iterative(array,item,high,low):
    while True:
        if low>high:
            return -1
        mid = low + (high-low)//2
        if array[mid]==item:
            return mid
        elif array[mid] < item:
            low = mid+1
        else:
            high = mid-1

if __name__ == '__main__':
    sequence = list(map(int,sys.stdin.readline().split()))[1:]
    items = list(map(int,sys.stdin.readline().split()))[1:]
    for item in items:
        print(binary_search_iterative(sequence,item,len(sequence)-1,0), end = ' ')


    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[n + 1]
    # a = data[1 : n + 1]
    # for x in data[n + 2:]:
    #     # replace with the call to binary_search when implemented
    #     print(linear_search(a, x), end = ' ')
