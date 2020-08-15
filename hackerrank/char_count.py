S = "aaabbbccccd"

# dic = dict.fromkeys(S, 0)
# print(dic)
temp = {}
for i in S:
    if temp.get(i) is None:
        temp[i] = 1
    else:
        temp[i] = temp[i] + 1

print(temp)
#
# print(max(temp.values()))
# # maxx = None
# # for k, v in temp.items():
# #     if v is max(temp.values()):
# #         maxx = k
#
# print('{} {}'.format(max(temp, key=temp.get), max(temp.values())))
#
from collections import Counter

#
# counts = Counter(S)
# print(counts)
#
# print(counts.most_common(3))
#
# # for k, v in counts.most_common(3):
# #     if v < max(counts.values()):
# #         print('{} {}'.format(k, v))
# lis = []
# i = 0
# most = counts.most_common(3)
# while most:
#     min = most[0][1]
#     if most[i][1] < min:
#         min = most[i][1]
#     lis.append(min)
#     most.remove(min)
#     i = i + 1
#
# print(lis)

# s = sorted(input().strip())
s_counter = Counter(S).most_common()

# key = lambda x: (x[1] * -1, x[0])


s_counter = sorted(s_counter, key=lambda x: x[1], reverse=True)
print(s_counter)
for i in range(0, 3):
    print(s_counter[i][0], s_counter[i][1])

a = [2,31,-1,2,0]
print(a)
