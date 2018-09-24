# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    """ Initially I haven't consider what if loot available is 
    less then capacity"""
    value = 0.
    # write your code here
    unit_value = [[values[i]/weights[i],weights[i]] for i in range(len(weights))]
    s_unit_value=sorted(unit_value,reverse=True)
    index = 0
    n1 = len(s_unit_value)
    while capacity>0 and index<n1:
    	if s_unit_value[index][1]:
    		capacity-= 1
    		s_unit_value[index][1] -= 1
    		value += s_unit_value[index][0]
    	else:
    		index+=1	





    return value


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.readline().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    n,capacity=list(map(int,sys.stdin.readline().split()))
    values=[];weights=[]
    for ii in range(n):
    	value,weight = list(map(int,sys.stdin.readline().split()))
    	values.append(value);weights.append(weight)

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
