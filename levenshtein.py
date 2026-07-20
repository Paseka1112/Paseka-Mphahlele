import sys
import stdio

def levenshtein(x, y):
    """Given two strings x,y, we wish to know how many operations (insertion, deletion, or
    substitution) are required to transform x into y"""

    n = len(x)
    m = len(y)
    A = [[i+j for j in range(m+1)] for i in range(n+1)]

    for i in range(n):
        for j in range(m):
            A[i+1][j+1] = min(A[i][j+1] + 1, A[i+1][j] + 1, 
                            A[i][j] + int(x[i]) != y[j])
            
    return A[n][m]