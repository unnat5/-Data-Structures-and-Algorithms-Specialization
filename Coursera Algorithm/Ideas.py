# def recFactorial(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return recFactorial(n-1)*n

# put = recFactorial(100)
# print(put)

# NAIVE GCD
def NaiveGCD(a,b):
	best = 0
	for d in range(1,a+b):
		if a%d==0 and b%d==0:
			best = d
	return best

def EuclideanGCD(a,b):
	if b ==0:
		return a
	else :
		return EuclideanGCD(b,a%b)

if __name__ == '__main__':
	out = NaiveGCD(4,10)
	cout = EuclideanGCD(357,234)
	print(out,cout)


