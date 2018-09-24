# Uses python3
import sys
import math


# def optimal_points(segments,lens):
#     sorted_seg = sorted(segments)
#     value = sorted_seg[0][0]-1
#     to  = math.inf
#     ls = []
#     counter = 0
#     while True:
#         value+=1
#         counter = 0
#         for ss in sorted_seg:
#             start = ss[0];stop=ss[1]
#             if value < start or to<start:
#                 break
#             if value >= start and value <= stop:
#                 to = min(stop,to)
#                 counter +=1
#         if value > to :
#             temp = sorted_seg[prev_counter-1]
#             sorted_seg = sorted_seg[prev_counter:]
#             lens-=prev_counter
#             value -= 1
#             ls.append(value)
#             value = temp[1]
#             to = math.inf
#             if lens<=0:
#                 return ls
#         prev_counter = counter

def optimal_points(segments,lens):
    segments.sort(key = lambda x:x[1])
    sorted_segment = segments
    value = sorted_segment[0][1]
    ls = [value]
    for ss in sorted_segment:
        if value<ss[0]:
            value = ss[1]
            ls.append(value)
            
    return ls
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    segment = []
    for ii in range(n):
        temp = list(map(int,sys.stdin.readline().split()))
        segment.append(temp)
    out = optimal_points(segment,n)
    print(len(out))
    print(*out)
