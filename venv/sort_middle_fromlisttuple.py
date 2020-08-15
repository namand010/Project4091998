

a = [(1,10,2),(2,-6,-1),(3,4,8),(1,-10,1)]
b = []



#n = len(a)

# for i in range(n):
#     for j in range(n-i-1):
#         if a[j][1] > a[j+1][1]:
#             a[j],a[j+1] = a[j+1],a[j]
#
# print(a)
#
# for i in range(n):
#     print(a[i][1], end=' ')

##### need to be fixed
def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        pivot = a.pop()
        pivot1 = pivot[1]
        d = []
        f = []
        for i in range(len(a)):
            if a[i][1] > pivot1:
                f.append(a[i])
            else:
                d.append(a[i])
    return quick_sort(d) + [pivot] + quick_sort(f)

n = quick_sort(a)
#for j in range(len(a)):
print(n, end=' ')

