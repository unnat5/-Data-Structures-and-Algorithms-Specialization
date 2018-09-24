#Uses python3

import sys
import math
# from functools import cmp_to_key 

# def comparator(a,b):
#     a_str = str(a)
#     b_str = str(b)
#     if a_str[0]==b_str[0] and abs(len(a_str)-len(b_str))<=1:
#     	return 1 if a%10 < b%10 else -1
#     return int(b_str[0])-int(a_str[0])

# def largest_number(n):
# 	n.sort(key=cmp_to_key(comparator))
# 	return "".join(map(str,n))
# def largest_number(n):
#     comparator = 0
#     out  = ""
#     n_len = len(n)
#     while True:
#         for ii in n:
#             #logic,comparator,out = complex_logic(ii,comparator,out)
#             if int(str(ii)[0])>int(str(comparator)[0]) and not ii == comparator:
#                 comparator= ii
                
#             elif str(ii)[0]==str(comparator)[0] and len(str(comparator))!=len(str(ii)):
#                 if int(str(comparator)+str(ii))>int(str(ii)+str(comparator)):
#                     out += str(comparator)
#                     n.remove(comparator)
#                     comparator = ii
#                 else:
#                     out += str(ii)
#                     n.remove(ii)
                    
#         out += str(comparator)
#         n.remove(comparator)
#         if len(n)==0:
#             break
#         comparator = 0
        
#     return out
# def largest_number(n):
#     comparator = 0
#     out  = ""
#     n_len = len(n)
#     while True:
#         for ii in n:
#             #logic,comparator,out = complex_logic(ii,comparator,out)
#             # if ii>=comparator or str(ii)[0] == str(comparator)[0]:
#             if ii>=comparator or (str(ii)[0] == str(comparator)[0] and len(str(comparator)) > 1):
#                 if int(str(ii)+str(comparator))>=int(str(comparator)+str(ii)):
#                     comparator = ii
                                
#         out += str(comparator)
#         n.remove(comparator);
#         if len(n)==0:
#             break
#         comparator = 0
#     return int(out)
# def largest_number(n):
#     comparator = 0
#     out  = ""
#     n_len = len(n)
#     count = 0
#     while True:
#         for index,ii in enumerate(n):
#         	if index == 0:
#         		comparator = ii
#         	else:
#             #logic,comparator,out = complex_logic(ii,comparator,out)
# 	            if ii>=comparator or (str(ii)[0] == str(comparator)[0] and len(str(comparator)) > 1):
# 	                if int(out + str(ii)+str(comparator)) >= int(out + str(comparator)+str(ii)):
# 	                    comparator = ii
                                
#         out += str(comparator)
#         count +=1
#         n.remove(comparator);
#         if count == n_len:
#             return int(out)  
#         comparator = 0



# def largest_number(n):
#     comparator = -math.inf
#     out  = ""
#     n_len = len(n)
#     count = 0
#     while True:
#         for index,ii in enumerate(n):
#         	if index == 0:
#         		comparator = ii
#         	else:
#             #logic,comparator,out = complex_logic(ii,comparator,out)
# 	            if ii>=comparator or (str(ii)[0] == str(comparator)[0] and len(str(comparator)) > 1):
# 	                if int(out + str(ii)+str(comparator)) > int(out + str(comparator)+str(ii)):
# 	                    comparator = ii
                                
#         out += str(comparator)
#         count +=1
#         n.remove(comparator);
#         if count == n_len:
#             return int(out)  
#         comparator = -math.inf



def complex_logical(maxDigit,digit):
    return int(str(maxDigit)+str(digit))<int(str(digit)+str(maxDigit))
    
    
    
def largest_number(n):
    answer = ""
    while len(n)!=0:
        maxDigit = 0
        for digit in n:
            if complex_logical(maxDigit,digit):
                maxDigit = digit
        n.remove(maxDigit)
        answer += str(maxDigit)
    return answer

if __name__ == '__main__':
    #input = sys.stdin.readline()
    n = input()
    a = list(map(int,input().split()))
    # print(a)
    print(largest_number(a))
    
