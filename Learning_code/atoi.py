import re
class Solution:
    def myAtoi(self, str: str) -> int:
        temp = []
        if str == "":
            return 0

        for i in list(iter(str)):
            if i == " ":
                continue
            else:
                if i != " " and not i.isalpha():
                    if i == "-" or i.isdigit() or i == "+":
                        temp.append(i)




