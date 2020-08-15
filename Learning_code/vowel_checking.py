print ("Naman is here")

string1 = "aieou dubey"
a = {}
for st in string1:
    if st not in a:
        a[st] = None

print(a)

#Rev

b = string1[::-1]
print(b)

for i in range(len(string1)-1, -1, -1):
    print(string1[i], end="")

#sort

d = [10,2,-1,0,11,5,6]

for i in range(len(d)):
    for j in range(len(d)-i-1):
        if d[j] > d[j+1]:
            temp = d[j+1]
            d[j+1] = d[j]
            d[j] = temp
print(d)


# file iterating
import re
#file = r"C:\Users\namand\Documents\test.txt"
file = " This is a great name.....is@dk.....and the ##%!@#@!@#!naman@gmail.comvik@fan.co"
count = {}
pattern = '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
#with open(file) as f:
#    f = f.readlines()

#for line in file:
 #   if line not in count:
  #      count[line] = None

lsi = []
for line in file:
    for pat in re.finditer(pattern, file, re.S):
        mat = pat.group()
        lsi.append(mat)
print(lsi)


#Email REgex
email = '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.])\.([a-zA-Z]{2,5})$'
website = 'http[s]?://?:[a-zA-z]|[0-9]|[$-@,$+]|[!*\(\).]|(?:%[0-9a-fA-F][0-9a-fA-F]))'

text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Original string: ",text)
print("Urls: ",urls)
