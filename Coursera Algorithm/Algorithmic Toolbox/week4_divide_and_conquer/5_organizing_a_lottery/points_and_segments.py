# Uses python3
import sys
from collections import deque,Counter, OrderedDict

# def fast_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     #write your code here
#     return cnt

# def naive_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     for i in range(len(points)):
#         for j in range(len(starts)):
#             if starts[j] <= points[i] <= ends[j]:
#                 cnt[i] += 1
#     return cnt

# def organizing_lottery(segments,points):
#     segments = sorted(segments,key=lambda x: x[0])
#     #sorted_points= sorted(points)
#     index = 0
#     out = [0]*len(points)
#     for i,p in enumerate(points):
#         index = 0
#         #print(segments[])
#         while p >= segments[index][0]:
#             #print(p)
#             if p<=segments[index][1]:
#                 out[i]+=1
#             index +=1
#             if index>len(segments)-1:
#                 break
#     return out

## Organizing lottery MergeSort way (taking advantage of Divide and Conquer)
## Time complexity of breaking the list log_{2} n
# def MergeSort(A,len_,cnt,points):
#     ##printing recursive call
#    # print("Recursive call Array :{},m:{}".format(A,len_))
#     ## Base case
#     if len_== 1:
#         for i,p in enumerate(points):
#             if p>=A[0][0] and p<=A[0][1]:
#                 cnt[i]+=1
#         return A
#     m = len_//2
# #     print("m:",m,len_)
#     B = MergeSort(A[:m],m,cnt,points)
# #     print("B completed!! value : {}".format(B))
#     C = MergeSort(A[m:],len_-m,cnt,points)
#     #print(sorted(B+C))
#     #print("out B : {}, C:{}".format(B,C))
#     A_out = B
#     #print("m:",m,A_out)
#     #print(A_out)
#     return A_out## understanding
# def MergeSort(A,len_,cnt,points):
#     # print(1)
#     while len_ != 1:
#         m = len_//2
#         #print(A[:m],m)
#         MergeSort(A[:m],m,cnt,points)
#         A = A[m:]
#         m = len_ -m
#         len_ = m
#     #print(A)
#     for i,p in enumerate(points):
#         if p>=A[0][0] and p<=A[0][1]:
#             cnt[i]+=1
#     return 
# def MergeSort(A,len_,cnt,points):
#     ls = deque([A])
#     while ls:
#         A = ls.popleft()
#         len_ = len(A)
#         while len_ != 1:
#             m = len_//2
#             ls.append(A[:m])
#             A = A[m:]
#             m = len_ -m
#             len_ = m
#         for i,p in enumerate(points):
#             if p>=A[0][0] and p<=A[0][1]:
#                 cnt[i]+=1
#             elif p>A[0][1]:
#                 break
#     return

# def MergeSort1(A,len_,points):
#     ls = deque([A])
#     counter_dict = Counter()
#     while ls:
#         A = ls.popleft()
#         len_ = len(A)
#         while len_ != 1:
#             m = len_//2
#             ls.append(A[:m])
#             A = A[m:]
#             m = len_ -m
#             len_ = m
#         for i,p in enumerate(points):
#             if p[0]>=A[0][0] and p[0]<=A[0][1]:
#                 counter_dict.update([p])
#             elif p[0]>A[0][1]:
#                 break                
#     return counter_dict

# def organizing_lottery(ls,counter_dict):
#     counter = 0
#     start = 0
#     end = 0 
#     for condition,item in ls:
#         if condition == 's':
#             start +=1
#         elif condition == 'e' :
#             end +=1
#         else :
#             counter_dict[condition] = abs(start - end)
#     # print(counter_dict)
            
#     return counter_dict.values()

def organizing_lottery(ls,n_points):
    counter = 0
    start = 0
    end = 0 
    # dict_ = {}
    out = n_points
    for ii,temp in enumerate(ls):
        if temp[0] == 1:
            start +=1
        elif temp[0] == 3 :
            end +=1
        else :
            out[temp[2]] = start-end
            
    return out

if __name__ == '__main__':
    #input = sys.stdin.read()
    # data = list(map(int, sys.stdin.read().split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends   = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    # mod_start = [0]*n
    # for i,d in enumerate(starts):
    #     mod_start[i] = ('s',d)
    # mod_end = [0]*n
    # for i,d in enumerate(ends):
    #     mod_end[i] = ('e',d)
    # # mod_start = [(str(i),d)for i,d in enumerate(starts)]
    # # mod_end = [(str(i),d)for i,d in enumerate(ends)]
    # mod_start+= mod_end

    # #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
    n_segments,n_points= list(map(int,sys.stdin.readline().split()))
    # list_segments = [0]*(n_segments*2)
    list_segments = [0]*(n_segments*2)
    index = -1
    for ii in range(0,n_segments):
        temp=tuple(map(int,sys.stdin.readline().split()))
        index+=1
        list_segments[index] = (1,temp[0])
        list_segments[index+1] = (3,temp[1])
        index+=1
    #print(list_segments)
    # points = list(map(int,sys.stdin.readline().split()))
    points = sys.stdin.readline().split()
    #print(list_segments)
    # counter_dict = OrderedDict()
    # modified_points = [('p',int(p)) for i,p in enumerate(points)]
    modified_points = [0]*n_points
    for i,p in enumerate(points):
        modified_points[i] = (2,int(p),i)
    list_segments += modified_points
    # print(modified_points)
    ls = sorted(list_segments,key=lambda x:(x[1],x[0]))
    # print(counter_dict)
    # print(ls)
    out = organizing_lottery(ls,modified_points)
    #for ii,p in enumerate(points):
        #print(out[p],end=' ')
    print(*out)

    # list_segments.sort(key=lambda x:x[1])
    #out = organizing_lottery(list_segments,points) 
    #print(points,list_segments)

