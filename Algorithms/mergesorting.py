#This version is from L10 in mit ocw. 
#I found it simple and easier to follow

def mergesort(L):
    """Returns a sorted list containing the same elements as L"""
    
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergesort(L[:middle])
        right = mergesort(L[middle:])
        together = merge(left, right)
        print('merged',  together)
        return together

def merge(left, right):
    """Assume left and right are sorted lists. Returns a new sorted 
    list containing the elements in left and right would contain """

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while ( i < len(left)):
        result.append(left[i])
        i = i + 1
    while (j < len(right)):
        result.append(right[j])
        j = j + 1
    return result

def main():

    L = [1, 10, 20, 5, 6, 7, 8, 100]
    result = mergesort(L)
    print(result)
if __name__ == '__main__': main()

