# Uses python3
import sys
import math as m
from collections import deque

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10
def binet_formula(n):
    return ((((1.0+m.sqrt(5.0))**n) - ((1.0-m.sqrt(5.0))**n))/(2**n * m.sqrt(5.0)))

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
    return fib_series[out] if fib_series[out] != 0 else 10


def fibonacci_sum_optimized(n):
    return (get_fibonacci_huge_optimized(n+2,10)-1)


if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_optimized(n))
