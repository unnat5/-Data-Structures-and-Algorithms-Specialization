# Uses python3
import sys
import itertools
from collections import defaultdict

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

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
    return value_table[-1],dict_[W]

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *A = list(map(int, input.split()))
    # print(partition3(A))
    dummy = sys.stdin.readline()
    ls = list(map(int,sys.stdin.readline().split()))
    ls = sorted(ls,reverse=True)
    absum= sum(ls)
    if absum%3 == 0:
        value,dicts = knapsack_norepetition(W=absum//3,items=ls)
        dvalue = [i[0] for i in dicts if i != 0]
        #print(dvalue)
        if value == absum/3 and sum(dvalue)==absum/3:
            [ls.remove(i) for i in dvalue];
            value,dicts = knapsack_norepetition(W=absum//3,items=ls)
            dvalue = [i[0] for i in dicts if i != 0]
            if value == absum/3 and sum(dvalue)==absum/3:
                [ls.remove(i) for i in dvalue];
                value,dicts = knapsack_norepetition(W=absum//3,items=ls)
                dvalue = [i[0] for i in dicts if i != 0]
                if value == absum/3 and sum(dvalue)==absum/3:
                    print(1)
                else:
                    print(0)
            else : 
                print(0)
        else:
            print(0)
    else:
        print(0)

