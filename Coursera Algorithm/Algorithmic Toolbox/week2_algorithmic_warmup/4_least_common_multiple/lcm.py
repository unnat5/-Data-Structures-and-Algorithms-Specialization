# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_better(a, b):
	counter=2
	out = 1
	while True:
		a_rem = a%counter==0
		b_rem = b%counter==0
		if a_rem or b_rem:
			if a_rem:
				a/=counter
			if b_rem:
				b/=counter
			out*=counter
		else:
			counter+=1
		if a==1 and b==1:
			return out

def gcd_w(a,b):
	while b>0:
		a,b = b,a%b
	return a



def lcm_optimize(a, b):
	out = a*b//gcd_w(a,b)
	return out



if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_optimize(a, b))

