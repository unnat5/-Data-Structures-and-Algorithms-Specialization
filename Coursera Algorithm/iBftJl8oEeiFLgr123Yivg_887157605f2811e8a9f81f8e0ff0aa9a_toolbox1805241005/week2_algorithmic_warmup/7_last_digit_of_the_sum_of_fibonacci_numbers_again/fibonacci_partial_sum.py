# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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

def get_fibonacci_huge_optimized(n, m, from_):
    length,fib_series = find_period_length(m)
    out = n%length
    out2 = from_%length
    return fib_series[out],fib_series[out2]


def fibonacci_partial_sum_optimized(from_,n):
    out,temp= get_fibonacci_huge_optimized(n+2,10,from_+1)
    if temp > out:
        out += 10
    return (out-temp)


if __name__ == '__main__':
    input = sys.stdin.readline();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_optimized(from_, to))