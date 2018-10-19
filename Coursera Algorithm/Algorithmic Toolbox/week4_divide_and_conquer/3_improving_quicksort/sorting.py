# Uses python3
import sys
import random
    
# def Partition3(A,l,r):
#     pivot = A[l]
#     #print(pivot)
#     j = l
#     count_pivot = 0
#     m1 = l
#     flag = 0
#     to = False
#     for i in range(l+1,r):
#         if A[i]< pivot:
#             j+=1
#             A[j],A[i]=A[i],A[j]
#             if flag ==1:
#                 to = True
#         elif A[i]==pivot:
#             flag =1
#             count_pivot+=1
#             m1+=1
#             j+=1
#             A[j],A[i]=A[i],A[j]
            
#             A[m1],A[j] = A[j],A[m1]
#     if to:
#         A[l:l+count_pivot+1],A[j-count_pivot:j+1] = A[j-count_pivot:j+1],A[l:l+count_pivot+1]
#         return j-count_pivot,j
#     else:
#         A[l],A[j] = A[j],A[l]
#         return j-count_pivot,j

def Partition3(A,l,r):
    pivot = A[l]
#     print(pivot,A)
    j = l
    count_pivot = 0
    non_pivot_count = 0
    m1 = l
    flag = 0
    to = False
    for i in range(l+1,r):
        if A[i]< pivot:
            j+=1
            A[j],A[i]=A[i],A[j]
            non_pivot_count+=1
            if flag ==1:
                to = True
        elif A[i]==pivot:
            flag =1
            count_pivot+=1
            m1+=1
            j+=1
            A[j],A[i]=A[i],A[j]
            A[m1],A[j] = A[j],A[m1]
#     print(A,"sd",j,count_pivot,non_pivot_count,A[j])
            
    if to:
        #print("q",A, A[l:l+count_pivot+1],A[j-count_pivot:j+1])
        #A[l:l+count_pivot+1],A[j-count_pivot:j+1] = A[j-count_pivot:j+1],A[l:l+count_pivot+1]
#         print(non_pivot_count)
#         print(A[j-non_pivot_count+1:j+1],A[l:l+non_pivot_count])
        temp_index = min(non_pivot_count-1,count_pivot)
        #print(temp_index)
        #A[j-temp_index+1:j],A[l:l+temp_index] = A[l:l+non_pivot_count],A[j-temp_index+1:j]
        A[j-temp_index:j+1],A[l:l+temp_index+1] = A[l:l+temp_index+1],A[j-temp_index:j+1]
        #return A[:j-temp_index-1],A[j+1:],A[j+1-temp_index:j+1]
        #print(j+1-temp_index,j+1,"as",len(A))
#         print(A[:j-count_pivot],A[j+1:],A)
        return j-count_pivot,j
    else:
        A[l],A[j] = A[j],A[l]
#         print(A)
#         return A[:j-count_pivot],A[j+1:],A[j-count_pivot:j+1]
        return j-count_pivot,j

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    # k = random.randint(l, r-1)
    # a[l], a[k] = a[k], a[l]
    #use partition3
    m1,m2 = Partition3(a, l, r)
    #print(m1,m2,a)
    randomized_quick_sort(a, l, m1);
    randomized_quick_sort(a, m2 + 1, r);


def RandomizedQuickSort(A,l,r):
    """
    QuickSort3
    Recursive call to smaller array 
    Eliminating tail recursion
    """
    while l<r:
        k = random.randint(l, r-1)
        A[k],A[l] = A[l],A[k] ## Swapping for randomized pivot
        m1,m2 = Partition3(A,l,r)
        # print(m1,m2,A)
        if m1-l < r-m2:
            RandomizedQuickSort(A,l,m1);
            l = m1+1
        else:
            RandomizedQuickSort(A,m2+1,r);
            r = m2

def QuickSort(A,l,r):
    # k = random.randint(l, r-1)
    # A[k],A[l] = A[l],A[k] ## Swapping for randomized pivot
    while l < r:
        # k = random.randint(l, r-1)
        # A[k],A[l] = A[l],A[k]
        m1,m2 = Partition3(A,l,r)
        # print(m1,m2)
        QuickSort(A,l,m1)
        l = m2+1 ##for python indexing

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n - 1)
    n = sys.stdin.readline()
    a = list(map(int,sys.stdin.readline().split()))
    #print(a)
    QuickSort(a,0,int(n))
    print(*a)
