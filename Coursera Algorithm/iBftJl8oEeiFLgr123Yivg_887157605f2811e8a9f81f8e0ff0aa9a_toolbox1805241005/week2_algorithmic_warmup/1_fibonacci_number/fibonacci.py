# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def optimized_fib(n):
	if n == 0:
		return 0
	if n==1:
		return 1
	fib_list = [0]*(n+1)
	fib_list[0] = 0
	fib_list[1] = 1
	for i in range(2,n+1):
		fib_list[i] = fib_list[i-1]+fib_list[i-2]
	return fib_list[n]

if __name__ == '__main__':
	n = int(input())
	print(optimized_fib(n))
