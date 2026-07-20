import sys
import stdio
import stdarray
#https://www.cs.cornell.edu/courses/JavaAndDS/files/sort5pigeonHole.pdf
#https://en.wikipedia.org/wiki/Pigeonhole_sort

def pigeonhole_sort(arr):
    arr_min = min(arr)
    arr_max = max(arr)
    arr_range = arr_max - arr_min + 1

    phole = stdarray.create1D(arr_range, None)
    for i in range(arr_range):
        phole[i] = []

    for x in arr:
        phole[x - arr_min].append(x)

    i = 0
    for count in range(arr_range):
        for item in phole[count]:
            arr[i] = item
            i += 1

    return arr
def main():
    a = [9, 7, 8, 6, 12]
    result = pigeonhole_sort(a)
    stdio.writeln(result)
if __name__ == '__main__': main()





