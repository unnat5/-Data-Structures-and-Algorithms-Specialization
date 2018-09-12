# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def find_period_length(m):
    """Pisano period"""
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
    out2 = (n-1)%length
    return fib_series[out],fib_series[out2]


def fibonacci_sum_square_optimized(n):
    temp,temp2= (get_fibonacci_huge_optimized(n,10))
    out = (temp+temp2)*temp
    return out%10

if __name__ == '__main__':
    n = int(stdin.readline())
    print(fibonacci_sum_square_optimized(n))
