from sys import stdin
from random import randint

#Tests the Frievalds algorithm

def readint():
    return int(stdin.readline())

def readarray(arr):
    return list(map(arr, stdin.readline().split()))

def readmatrix(n):
    matrix = []
    for i in range(n):
        row = readarray(int)
        assert len(row) == n
        matrix.append(row)
    return matrix

def matrix_vector(matrix, vector):
    n = len(matrix)
    result = []
    result += [matrix[i][j]*vector[j] for j in range(n) for i in range(n)]

def freivalds_alg(A, B, C):
    n = len(A)
    vector = [randint(0, 100000) for j in range(n)]
    return matrix_vector(A, matrix_vector(B, vector)) == matrix_vector(C, vector)

def main():
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(freivalds_alg(A, B, C))

if __name__ == '__main__': main()



