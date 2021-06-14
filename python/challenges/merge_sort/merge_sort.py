def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
    return arr
def merge(left, right, arr):

    i=  0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        for item in right[j:]:
            arr[k] = item
            k += 1
    else:
        for item in left[i:]:
            arr[k] = item
            k += 1

# liste = [3,2,4,1]
# print(merge_sort(liste))
# print(liste)
