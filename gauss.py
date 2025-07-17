import numpy as np
import random
def gauss(A,b):
    n = len(A)
    A = np.hstack((A,b))
# Elimination process
    for i in range(0,n-1):
        # step 2
        p = i        
        while p <= n and A[p][i] == 0:
            p = p + 1
        if p == n+1:
            raise ValueError("Matrix A is singular")
        # step 3 
        if p != i:
            A[[i,p]] = A[[p,i]]
        # step 4, do steps 5 and 6    
        for j in range(i+1,n):
            m = A[j][i]/A[i][i]
            for k in range(i,n+1):
                A[j][k] = A[j][k] - m*A[i][k]        
    # step 7                            
    if A[n-1][n-1] == 0:
        raise ValueError("Matrix A is singular")        
# back substitution process
    

