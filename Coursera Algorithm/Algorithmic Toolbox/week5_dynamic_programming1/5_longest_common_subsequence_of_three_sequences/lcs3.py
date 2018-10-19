#Uses python3

import sys
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
                D[i,j] = min(insertion,deletion,match)
            else:
                 D[i,j] = min(insertion,deletion)
    return D

def OutputAlignment_list(n,m,A,B,D):
    longest_subseq = []
    while n!=0 and m!=0:
        if n>0 and D[n,m] == D[n-1,m]+1:
            # n_list.append(A[n-1])
            # m_list.append("-")
            n -= 1
        elif m>0 and D[n,m] == D[n,m-1]+1:
            # n_list.append("-")
            # m_list.append(B[m-1])
            m-=1
        else:
            # n_list.append(A[n-1])
            # m_list.append(B[m-1])
            if A[n-1]==B[m-1]:
                longest_subseq.append(A[n-1])
            n-=1;m-=1;
    return longest_subseq

def OutputAlignment(n,m,seq1,seq2,D):
    counter = 0
    while n!=0 and m!=0:
        if n>0 and D[n,m] == D[n-1,m]+1:
            # n_list.append(A[n-1])
            # m_list.append("-")
            n -= 1
        elif m>0 and D[n,m] == D[n,m-1]+1:
            # n_list.append("-")
            # m_list.append(B[m-1])
            m-=1
        else:
            # n_list.append(A[n-1])
            # m_list.append(B[m-1])
            if seq1[n-1]==seq2[m-1]:
                # longest_subseq.append(A[n-1])
                counter +=1
            n-=1;m-=1;
    return counter

if __name__ == '__main__':
    n = sys.stdin.readline()
    seq1 = sys.stdin.readline().split()
    m = sys.stdin.readline()
    seq2 = sys.stdin.readline().split()
    q = sys.stdin.readline()
    seq3 = sys.stdin.readline().split()
    D12 = EditDistance(seq1,seq2)
    common12 = OutputAlignment_list(int(n),int(m),seq1,seq2,D12)
    # D23 = EditDistance(seq2,seq3)
    # common23 = OutputAlignment_list(int(m),int(q),seq2,seq3,D23)
    common12 = common12[::-1]
    D = EditDistance(common12,seq3)
    out = OutputAlignment(len(common12),int(q),common12,seq3,D)
    D23 = EditDistance(seq2,seq3)
    common23 = OutputAlignment_list(int(m),int(q),seq2,seq3,D23)
    common23 = common23[::-1]
    D = EditDistance(common23,seq1)
    out1 = OutputAlignment(len(common23),int(n),common23,seq1,D)



    print(max(out,out1))



