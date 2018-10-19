# Uses python3
# def edit_distance(s, t):
#     #write your code here
#     return 0
import numpy as np 
def EditDistance(A,B):
    n = len(A)
    m = len(B)
    D = np.zeros((n+1,m+1))
    if n>m:
        large = n+1
    else:
        large = m+1    
    for ii in range(large):
        if ii<n+1:
            D[ii,0]=ii
        if ii<m+1:
            D[0,ii] = ii        
    for j in range(1,m+1):
        for i in range(1,n+1):
            insertion = D[i,j-1]+1
            deletion = D[i-1,j]+1
            match = D[i-1,j-1]
            mismatch = D[i-1,j-1]+1
            if A[i-1]==B[j-1]:
                D[i,j] = match
            else:
                 D[i,j] = min(insertion,deletion,mismatch)
    return int(D[n,m])

if __name__ == "__main__":
    print(EditDistance(input(), input()))
