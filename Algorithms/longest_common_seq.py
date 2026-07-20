# ref: https://www.cse.cuhk.edu.hk/~taoyf/course/3160/24-fall/lec/0k_lcs.pdf

import stdio
import sys

def longest_common_seq(x, y):
    """Given two strings x and y, find the length of the 
        longest subsequence"""
    
    n = len(x)
    m = len(y)

    A = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                A[i+1][j+1] = A[i][j] + 1
            else:
                A[i+1][j+1] = max(A[i][j+1], A[i+1][j])
    
    sol = []
    i, j = n, m
    while A[i][j] > 0:
        if A[i][j] == A[i - 1][j]:
            i -= 1
        elif A[i][j] == A[i][j-1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            sol.append(x[i])
    return ''.join(sol[::-1])

def main():
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    result = longest_common_seq(s1, s2)
    stdio.writeln(result)

if __name__ == '__main__':main()
