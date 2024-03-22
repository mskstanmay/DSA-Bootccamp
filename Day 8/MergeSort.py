def merge(list1,list2):
    newlist= []
    i = 0
    j = 0

    while (i < len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            newlist.append(list1[i])
            i+=1
        else:
            newlist.append(list2[j])
            j+=1
    while i < len(list1):
        newlist.append(list1[i])
        i+=1
    while j < len(list2):
        newlist.append(list2[j])
        j+=1

def merge_Sort(mylist):
    if len(mylist) ==1:
        return mylist
    mid_index = len(mylist) // 2
    
    left= merge_Sort(mylist[:mid_index])
    right = merge_Sort(mylist[mid_index:])

    return merge(left,right)

ol =[3,1,4,2]
print(merge_Sort(ol))
