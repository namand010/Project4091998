lis = []
input_c = int(input())
for i in range(input_c):
    lis.append(input())

print(lis)
from collections import Counter
counts = Counter(lis) ######----> creats dict with how many occurences are the values
print(counts)
print(len(counts))
print(*counts.values())

for i in counts.elements():
    print ( i, end = " ")

print(counts.most_common(2))
dic = dict.fromkeys(lis,0)
# print(len(dic.keys()))
# for i in lis:
#     if dic[i] is 0:
#         dic[i] = 1
#     else:
#         dic[i] = dic[i] + 1
# 
# print(len(dic))
# print(*dic.values())



