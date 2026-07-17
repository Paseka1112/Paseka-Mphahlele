import sys
import stdio

def min_scalar(u, v):
    """This function returns the minimum scalar product of two vectors u and v"""
    x = sorted(u)
    y = sorted(v, reverse= True)

    result = 0
    for i in range(len(x)):
        result += x[i]*y[i]
    return abs(result)

def main():
    u = [1, 3, -5]
    v = [-2, 4, 1, 7]
    result = min_scalar(u, v)
    stdio.writeln(result)
if __name__ == '__main__': main()
