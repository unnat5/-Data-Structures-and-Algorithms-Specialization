# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [10,5,1]
    index = 0
    cout = 0
    while m>0:
    	if not m-coins[index]>=0:
    		index+=1
    	else: 
    		m-=coins[index]
    		cout+=1





    return cout

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
