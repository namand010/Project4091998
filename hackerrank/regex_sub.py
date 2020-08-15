
import re

N = int(input())
strr = ""
for i in range(N):
    strr = strr + "\n" + input()

change_str = re.sub('(?<= )&&(?= )' ,"and", strr)
fully_changed = re.sub("(?<= )\|\|(?= ) ", "or", change_str)

print(fully_changed)
