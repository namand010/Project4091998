def compress(string):
    temp={}
    result=" "
    for x in string:
        if x in temp:
            temp[x] = temp[x]+1
        else:
            temp[x] = 1
    for key, value in temp.items():
        result += str(key) + str(value)

    return result


if __name__ == '__main__':
    s = input("Enter the string:")
    print(compress(s))