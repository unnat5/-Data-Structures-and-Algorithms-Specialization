# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def optimized_fib_last_digit(n):
    if n == 0:
        return 0
    # if n==1:
    #     return 1
    fib_list = [0]*(n+1)
    fib_list[0] = 0
    fib_list[1] = 1
    for i in range(2,n+1):
        fib_list[i] = (fib_list[i-1]+fib_list[i-2])%10
    return fib_list[n]

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(optimized_fib_last_digit(n))
