#Ref: https://en.wikipedia.org/wiki/Maximum_subarray_problem

def maxsubarray(arr):
    result = arr[0]
    maxEnding = arr[0]

    for i in range(len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        result = max(result, maxEnding)
    
    return result