def bubble_sort(mylist):
    for i in range(len(mylist) - 1 , 0 ,-1):
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1], mylist[j]
    return mylist


print(bubble_sort([234,23,1,23,2,321,12]))

def selection_sort(mylist):
    for i in range(len(mylist) - 1):
        min_index = i
        for j in range(i + 1, len(mylist)):
            if mylist[j] < mylist[min_index]:
                min_index = j
        if i != min_index:
            mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
    return mylist


print(selection_sort([1,34,52,2,12,41,32]))

def insertion_sort(mylist):
    for i in range(1,len(mylist)):
        temp = mylist[i]
        j = i-1
        while j > -1 and temp < mylist[j]:
        # j < -1 is important to prevent backflow
            mylist[j+1] = mylist[j]
            mylist[j] = temp
            j -=1
    return mylist

print(insertion_sort([2,1,3]))
print(insertion_sort([1,432,32,24,45,3,44,6,8,6,2]))