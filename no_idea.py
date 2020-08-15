# a, b = input().split()
# val = input().split()
#
# for i in range(a):
#     c = input().split()
#
# for j in range(b):
#     d = input().split()
#
# for k in val:
#     if k in c:

a, b = input().split()
arr = list(input().split())
A = set(input().split())
B = set(input().split())

total_happiness = 0
for i in arr:
    if i in A:
        total_happiness += 1
    elif i in B:
        total_happiness -= 1
    else:
        total_happiness = total_happiness

print(total_happiness)
