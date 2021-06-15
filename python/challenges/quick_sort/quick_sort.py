def quick_sort(myList, i, j):
    if i < j:
        pivot = partition(myList, i, j)
        quick_sort(myList, i, pivot-1)
        quick_sort(myList, pivot+1, j)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right



test_list = [ 6,7,2,47,37,30 ]
print(quick_sort(test_list, 0, len(test_list) - 1))

