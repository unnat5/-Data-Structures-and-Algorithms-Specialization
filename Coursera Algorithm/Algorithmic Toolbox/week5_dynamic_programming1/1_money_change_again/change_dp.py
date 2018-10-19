# Uses python3
import sys
import math


def get_change(money,coins=[1,3,4]):
	change_table = [0]*(money+1)
	for value in range(1,money+1):
	    minCoin = math.inf
	    for coin in coins:
	        if coin<=value:
	            temp_minCoin = change_table[value-coin]+1
	            if temp_minCoin<minCoin:
	                minCoin=temp_minCoin
	                change_table[value]=minCoin
	return change_table[money]

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
