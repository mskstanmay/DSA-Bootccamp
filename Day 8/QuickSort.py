def swap(mylist, index1, index2):
    mylist[index1], mylist[index2] = mylist[index2], mylist[index1]

def pivot(mylist, pivotIndex, endIndex):
    swapIndex = pivotIndex

    for i in range(pivotIndex + 1, endIndex + 1):
        if mylist[i] < mylist[pivotIndex]:
            swapIndex += 1
            swap(mylist, i, swapIndex)
    swap(mylist, pivotIndex, swapIndex)
    return swapIndex

def quicksort(mylist, left, right):
    if left < right:
        pivotindex = pivot(mylist, left, right)
        quicksort(mylist, left, pivotindex - 1)
        quicksort(mylist, pivotindex + 1, right)
    return mylist

def qs(mylist):
    return quicksort(mylist, 0, len(mylist) - 1)

print(qs([4, 6, 1, 7, 3, 2, 5]))
