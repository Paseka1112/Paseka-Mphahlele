import sys
import stdio
from instream import InStream

##implementing and teting from 'Algorithms' - Cormen & co

def findmaxcrossingsubarray(a, low, mid, high):
    neg_inf = float('-inf')
    left_sum = neg_inf
    sum = 0
    for i in range(mid, low, -1):
        sum = sum + a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = neg_inf
    sum = 0
    for j in range(mid+1, high):
        sum = sum + a[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def main():
    a = [13, -3, -25, 20,-3 ,-16, -23, 18, 20, -7, 12, -5 ,-22, 15, -4,7]
    result = findmaxcrossingsubarray(a, 0, len(a)//2, len(a))
    stdio.writeln(result)
if __name__ == '__main__': main()


