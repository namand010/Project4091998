# arr = [1,2,3,4,6,8]
# temp = []
# for i in range(arr[0], arr[-1] + 1):
#     temp.append(i)
#
# a = set(temp)
# b = set(arr)
#
# print("The Missing Value", list(a^b))


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         l = []
#         r = []
#         pivotal = arr.pop()
#         for i in range(len(arr)):
#             if arr[i] < pivotal:
#                 l.append(arr[i])
#             else:
#                 r.append(arr[i])
#     return quick_sort(l) + [pivotal] + quick_sort(r)
#
# arr = [23,24,25,26,20,21,22]
# print(quick_sort(arr))


# import re
#
#
# def ip_address(pattern, str):
#     if re.search(pattern, str):
#         return True
#     else:
#         return False
#
#
# pattern = "^([0-9]{0,255})\.([0-9]{0,255})\.([0-9]{0,255})\.([0-9]{0,255})"
# print(ip_address(pattern, str="10.0.0.0"))


def binary_search(arr, elem):
    begin_index = 0
    last_index = len(arr) - 1

    while begin_index <= last_index:
        mid = (last_index + begin_index) // 2
        midvalue = arr[mid]

        if midvalue == elem:
            return mid
        elif elem > midvalue:
            begin_index = mid + 1
        else:
            last_index = mid - 1
    return -1


print(binary_search(arr=[2,5,6,8], elem=5))
