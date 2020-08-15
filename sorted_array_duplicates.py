arr = [1, 1, 2, 3, 4, 5, 6, 6, 7]

# l = set(arr)

# print(l)

ab = set()

for i in arr:
    if i not in ab:
        ab.add(i)

print(ab)


a = [10, 5, 15]
b = [20, 3, 2, 12]

for j in range(len(b)):
    a.append(b[j])

print(a)