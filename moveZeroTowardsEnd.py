arr = [2,3,4,5,65,0,65,9,0,0,0,4,0,0,5,23]

def moveZeroTowarsRight(arr):
    n = len(arr)
    index = 0
    for i in range (0, n):
        if (arr[i] != 0):
            arr[index] = arr[i]
            index = index + 1
    
    while (index < n):
        arr[index] = 0
        index = index + 1
    
    return arr

arr = moveZeroTowarsRight(arr)
print(arr)