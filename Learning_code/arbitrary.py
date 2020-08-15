def circularArray(arr, elem):
    begin_index = 0
    last_index = len(arr) - 1
    # i = 0
    # (begin_index, last_index) = (0, len(A) - 1)
    while begin_index <= last_index:
        mid = (begin_index + last_index) // 2
        if elem == arr[mid]:
            return mid

        if arr[mid] <= arr[last_index]:
            if arr[mid] < elem <= arr[last_index]:
                begin_index = mid + 1
            else:
                last_index = mid - 1
        else:
            if arr[begin_index] <= elem < arr[mid]:
                last_index = mid - 1
            else:
                begin_index = mid + 1
    return -1


A = [9, 10, 2, 5, 6, 8]
key = 6
index = circularArray(A, key)
if index != -1:
    print("The index is", index)
else:
    print("Element not found")
