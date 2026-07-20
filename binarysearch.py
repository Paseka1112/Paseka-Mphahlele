import sys
import stdio
from instream import InStream

def _search(key, a, lo, hi):
    if hi <= lo: return -1 #not found
    mid = (lo + hi) // 2
    if a[mid] > key:
        return _search(key, a, lo, mid)
    elif a[mid] < key:
        return _search(key, a, mid + 1, hi)
    else:
        return mid
def search(key, a):
    return _search(key, a, 0, len(a))

def main():
    instream = InStream(sys.argv[1])
    a = instream.readAllStrings()
    while not stdio.isEmpty():
        key = stdio.readString()
        if search(key, a) < 0: stdio.writeln(key)
if __name__ == '__main__': main()