dic = {}
input_c = int(input())
for i in range(input_c):
    value = input()
    if dic.get(value) is None:
        dic[value] = 1
    else:
        dic[value] = dic[value] + 1

print(len(dic))
print(*dic.values())


