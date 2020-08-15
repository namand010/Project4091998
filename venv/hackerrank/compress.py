ab = "1222311"

from itertools import groupby

print(list(groupby(ab)))

for k, v in groupby(ab):
    print('({},{})'.format(*(len(list(v)), int(k))))


# counts = list(iter(ab))

# count = 0
# for i in range(len(counts)):
#     if counts[i+1] != counts[i]:
#         print("1", counts[i])
#     else:
#         print(count + 1)
#         print(count[i])
