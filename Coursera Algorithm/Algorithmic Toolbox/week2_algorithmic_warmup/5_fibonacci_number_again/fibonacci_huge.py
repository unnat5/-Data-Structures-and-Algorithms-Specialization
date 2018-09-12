# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def find_period_length(m):
    fb = [0]*2
    fb[0] = 0%m 
    fb[1] = 1%m 
    c = 1
    counter=0
    prev = -1
    while True:
        c+=1
        counter +=1
        temp = (fb[c-1]+fb[c-2])%m
        fb.append(temp)
        if temp==1 and prev==0:
            return counter,fb

        prev = temp

def get_fibonacci_huge_optimized(n, m):
    length,fib_series = find_period_length(m)
    out = n%length
    return fib_series[out]


if __name__ == '__main__':
    #input = sys.stdin.read();
    n, m = map(int, input().split())
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_optimized(n,m))
