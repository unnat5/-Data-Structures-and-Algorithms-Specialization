#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    a_sorted = sorted(a,reverse=True)
    b_sorted = sorted(b,reverse=True)
    for i in range(len(b_sorted)):
        res += a_sorted[i] * b_sorted[i]
    return res

if __name__ == '__main__':
    n = sys.stdin.readline()
    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))
    print(max_dot_product(a, b))
    
