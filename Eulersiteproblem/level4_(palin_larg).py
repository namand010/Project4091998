n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)

#include<iostream.h>    ----------------->>>>>>>its for scanf and printf
#include<stdio.h>
#include<Math.h>

#for (i=0; i>=10; i--)
 #   printf("%d" && "%d", i++, ++i)