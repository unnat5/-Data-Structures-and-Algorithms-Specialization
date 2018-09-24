# Uses python3
import sys

# def get_prime():
#     num=0
#     ls =[]
#     while True:
#         flag=0
#         num+=1
#         for ii in range(2,num//2+1):
#             if num%ii == 0:
#                 flag =1
#         if flag != 1:
#             yield num
# def optimal_summands(tar):
#     ls = []
#     if tar==2:
#         return [2]
#     get_primes = get_prime()
#     while tar!=0:
#         #print(tar,ls)
#         num = next(get_primes)
#         temp = tar-num
#         if not temp%2==0 or temp==0:
#             tar-=num
#             ls.append(num)
#     return ls

# def optimal_summands(n):
# 	count = 0
# 	ls =[]
# 	while True:
# 		count += 1
# 		temp = n-count 
#     	if temp>count:
#         	ls.append(count)
#         	n-=count
#     	else :
#         	ls.append(n)
#         	return ls

def optimal_summands(n):
	count =0
	ls = []
	while True:
		count +=1
		temp = n-count
		if temp > count:
			ls.append(count)
			n-=count
		else:
			ls.append(n)
			return ls




if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
