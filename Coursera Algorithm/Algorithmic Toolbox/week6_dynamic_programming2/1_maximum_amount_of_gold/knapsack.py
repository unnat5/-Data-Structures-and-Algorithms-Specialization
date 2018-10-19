# Uses python3
import sys
from collections import defaultdict

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def knapsack_norepetition(W=10,items=[3,5,3,3,5]):
    value_table = [0]*(W+1)
    dict_ = defaultdict(list)
    dict_[0] = [0]
    final_temp = 0
    for w in range(1,W+1):
        for ii,item in enumerate(items):
            if item<= w:
                temp_val = value_table[w-item]+item
                if temp_val > value_table[w]:
                    #print(dict_[w-item],item,"s")
                    if (item,ii) not in dict_[w-item]:
                        #print("s2",item)
                        value_table[w]=temp_val
                        final_temp  = (item,ii)
        if final_temp != 0:
            dict_[w] = dict_[w-final_temp[0]]+[final_temp]
            final_temp=0
        if value_table[w] < value_table[w-1]:
            dict_[w] = dict_[w-1]
            value_table[w] = value_table[w-1]
    return value_table[-1]

if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    # print(optimal_weight(W, w))
    W,len_ = list(map(int,sys.stdin.readline().split()))
    gold = list(map(int,sys.stdin.readline().split()))
    out = knapsack_norepetition(W,gold)
    print(out)

