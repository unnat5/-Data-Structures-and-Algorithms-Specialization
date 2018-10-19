# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions


# def MergeSort(A,len_,counter):
#     if len_ == 1:
#         counter+=1
#         return A,counter
#     m = len_//2
#     B,counter = MergeSort(A[:m],m,counter)
#     C,counter = MergeSort(A[m:],len_ - m,counter)
#     A_out,counter = Merge(B,C,counter)
#     return A_out,counter 

# def Merge(B,C,counter):
#     D = []
#     len_b = len(B)
#     len_c = len(C)
#     flag_T = 0
#     while len_b and len_c :
#         flag_T =1
#         if B[0]>C[0]:
#             #print(B,C)
#             D.append(C[0])
#             C = C[1:]
#             len_c-=1
#             flag =1
#             counter +=1
#         else:
#             D.append(B[0])
#             B = B[1:]
#             len_b-=1
#             flag = 0
#     if flag_T ==0:
#         return B+C,counter
#     elif flag == 0:
#         out = D+C
#     else:
#         out = D+B
#     return out,counter
def MergeSort(A,len_,counter):
    if len_ == 1:
        return A,counter
    m = len_//2
    B,counter = MergeSort(A[:m],m,counter)
    C,counter = MergeSort(A[m:],len_ - m,counter)
    A_out,counter = Merge(B,C,counter)
    return A_out,counter 

def Merge(B,C,counter):
    D = []
    len_b = len(B)
    len_c = len(C)
    while len_b and len_c :
        if B[0]>C[0]:
            D.append(C[0])
            C = C[1:]
            len_c-=1
            flag =1
            counter +=len(B)
        else:
            D.append(B[0])
            B = B[1:]
            len_b-=1
            flag = 0
   # print(B,C,counter)
    if flag == 0:
        out = D+C
    else:
        out = D+B
    return out,counter

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    n = int(sys.stdin.readline())
    array = list(map(int,sys.stdin.readline().split()))
    counter = 0
    sorted_array,number_of_inversions = MergeSort(array,n,counter)
    print(number_of_inversions)

