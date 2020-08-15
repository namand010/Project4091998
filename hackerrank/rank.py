arr = [100, 2, 70, 2]
temp = arr
sorted_arr = sorted(arr)
print(sorted_arr)

count = 1
dict = {}
dict2 = {}

for i in sorted_arr:
    if i not in dict:
        dict[i] = count
        count = count+1
    else:
        count = count + 1
lis = []
for j in temp:
    if j in dict:
        lis.append(dict.get(j))

print(lis)


print(dict)