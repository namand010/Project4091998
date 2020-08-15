str = "AABCAAADA"
lis = []
# a = iter(str) this is for making string iteratable
# print(a)
# m = list(zip(a,a,a)) combines two lists or more into list of tuples
# print(m)
# for j in range(3):
#     for k in m[0]:
#         if k not in
#
# # b= set()
# # c = []
# # for i in m:
# #     for j in i:
# #         if j not in b:
# #             b.add(j)
# #
# # print(b)
for i in range(3):
    t = str[i * 3 : (i + 1) * 3]
    lis.append(t)

temp = []
for i in range(len(list(iter(str)))-6):
    abc = "".join(str[i * 3 : (i + 1) * 3])
    temp.append(abc)
print(temp)
print(lis)








