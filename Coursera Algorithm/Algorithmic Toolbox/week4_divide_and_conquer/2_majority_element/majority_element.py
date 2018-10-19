# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1


def recursive_majority(A,len_,array,n):
    if len_ == 1:
        print(A)
        array[A[0]]+=1
        if array[A[0]]>n/2:
            return 1,array,n
        else:
            return 0,array,n
    m = len_//2
    out,array,n = recursive_majority(A[:m],m,array,n)
    out,array,n = recursive_majority(A[m:],len_ - m,array,n)
    return out,array,n    


def get_majority_advanced(a,n):
    counter={}
    for ii in a:
        if ii in counter.keys():
            counter[ii]+=1
        else:
            counter[ii] = 1
    # print(counter)
    for key,item in counter.items():
        if item>n//2:
            return 1
    return 0


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    out = get_majority_advanced(a,n)
    print(out)
