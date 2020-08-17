# import re
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         temp = []
#         signal = 0
#         if str == "":
#             return 0
#
#         for i in list(iter(str)):
#             if i == " ":
#                 continue
#             elif i.isalpha():
#                 return 0
#             else:
#                 if i == "-":
#                     signal += 1
#                 elif i.isdigit():
#                     signal += 1
#
#
#
#
#
#
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        num = '1234567890'
        signal = 0
        answer = ''  # Number storage
        num_exisit = 0  # There is a number in the record string
        for i in range(0, length):
            if str[i] == ' ':
                continue
            if str[i] in alpha and num_exisit == 0:  # The first non-space character is the letter
                return 0
            if str[i] in alpha and num_exisit == 1:
                return int(answer)
            if str[i] == '-' and i < length - 1 and str[i + 1] in num:
                signal = 1  # record negative number
                continue
            if str[i] in num:
                answer = answer + str[i]
                num_exisit = 1

        if num_exisit == 1 and signal == 0:
            if int(answer) >= 2 ** 31 - 1:
                return 2147483647
            return int(answer)
        elif num_exisit == 1 and signal == 1:
            if (int(answer) * -1) <= -2 ** 31:
                return -2147483647
            return (int(answer) * -1)
        else:
            return 0

abc = Solution()
print(abc.myAtoi("-91283472332"))