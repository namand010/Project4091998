str = "abacdex"
X = "e"
Y = "x"
lis = list(iter(str))
for i in range(len(lis)):
    if lis[i] == X:
        # temp = lis[i]
        lis[i] = Y


print("".join(lis))

