

######## taking pivot as last element from the list and cgecking all values which is greater or leseer and appening it with recirsion as followed up
######## Big O - n log n, worst is n2 
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = arr.pop()

        item_greater = []
        items_lesser = []

        for i in range(len(arr)):
            if arr[i] > pivot:
                item_greater.append(arr[i])
            else:
                items_lesser.append(arr[i])
    return quick_sort(items_lesser) + [pivot] + quick_sort(item_greater)

arr = [10, 7, 8, 9, 1, 5]
n = quick_sort(arr)
for j in n:
    print(j, end=' ')


