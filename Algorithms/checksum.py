#this is 2.1.12 from RS book
#how is this concept applied to credit cards?
import sys

def f(d):
    doubled = str(2*d)
    return sum(int(char) for char in doubled)

def checksum(digits):
    """d[i] are the decimal digits of the account number and f(d)
        is the sum of the decimal digits of 2d. Takes in 10 digits"""

    total = 0
    for i in range(len(digits)):
        if i % 2 == 0:
            total += digits[i]
        else:
            total += f(digits[i])

    d10 = (-total) % 10
    return d10

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Please enter a valid account number")
        sys.exit(1)

    digits = [int(char) for char in sys.argv[1]]
    check = checksum(digits)

    result = " ".join(str(d) for d in digits) + str(check)
    print(result)

if __name__ == '__main__':main()

## use 1234567890