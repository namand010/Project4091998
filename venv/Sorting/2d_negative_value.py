
a = [[-4, -3, -1, 1],
     [-2, -2,  1, 2],
     [-1,  1,  2, 3],
     [1,   2,  4, 5]]

def negative_count(a):
    count = 0
    row = 0 #####to find the lenth of row - len(a)
    col = len(a[0]) - 1  #####last column to start with
##########O(n) instead of O(n2)
    while col >= 0 and row < len(a):
        if a[row][col] < 0:
            count += (col + 1)
            row += 1
        else:
            col -= 1
    return count

print(negative_count(a))


