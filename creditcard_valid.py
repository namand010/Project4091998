# You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
#
# A valid credit card from ABCD Bank has the following characteristics:
#
# ► It must start with a ,  or .
# ► It must contain exactly  digits.
# ► It must only consist of digits (-).
# ► It may have digits in groups of , separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have  or more consecutive repeated digits.

import re


def fun(s):
    # return True if s is a valid email, else return False
    # pattern = "^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    pattern = "^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$"
    sys_pattern = re.compile(pattern)
    if re.match(sys_pattern, s):
        return True
    return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
