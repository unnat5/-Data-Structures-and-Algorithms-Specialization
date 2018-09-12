# Python 3
import sys
def addtwo(a,b):
	return a+b

if __name__ == '__main__':
	token = sys.stdin.readline().split()
	out = addtwo(int(token[0]),int(token[1]))
	print(out)
