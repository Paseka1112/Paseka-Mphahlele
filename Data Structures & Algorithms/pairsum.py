import sys
import stdio
from instream import InStream

def pairsum(x, target):
    """Tests id there is a pair of elements in x[] which is equal to target"""
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if (x[i] + x[j] == target):
                print(x[i], x[j])
                return
    print('No pair found')

def main():
    x = [int(i) for i in input("Enter items separated by space: ").split()]
    target = int(input("Enter target: "))
    pairsum(x, target)

if __name__ == '__main__':
    main()
