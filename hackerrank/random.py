# if __name__ == '__main__':
#    # N = int(input())
#
#     arr = []
# for i in range(10):
#     s = input().split()
#     for i in range(1, len(s)):
#         s[i] = int(s[i])
#
#     if s[0] == "append":
#         arr.append(s[1])
#     elif s[0] == "extend":
#         arr.extend(s[1:])
#     elif s[0] == "insert":
#         arr.insert(s[1], s[2])
#     elif s[0] == "remove":
#         arr.remove(s[1])
#     elif s[0] == "pop":
#         arr.pop()
#     elif s[0] == "sort":
#         arr.sort()
#     elif s[0] == "reverse":
#         arr.reverse()
#     elif s[0] == "print":
#         print(arr)

import os
hostname = "google.com" #example
response = os.system("ping -c 1" + hostname)
print(response)

#and then check the response...
if response == 0:
  print ("hostname is up{}".format(hostname))
else:
  print ("hostname is up{}".format(hostname))
