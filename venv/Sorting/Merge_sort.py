class Merge_sort:
    def merge_sort(self, A):
        first = 0
        self.merge_sort2(A, first, len(A) - 1)

    def merge_sort2(self, A, first, last):
        if first < last:
            middle = (first + last) // 2
            self.merge_sort2(A, first, middle)
            self.merge_sort2(A, middle+1, last)
            self.merge(A, first, middle, last)

    def merge(self, A, first, middle, last):
        L = A[first:middle]
        R = A[middle:last+1]
        L.append(9999999)
        R.append(9999999)
        i=j=0
        for k in range(first, last+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j +=1

a = Merge_sort()
b = [3,1,6,0,88,-1,4]
a.merge_sort(b)
print(b)
