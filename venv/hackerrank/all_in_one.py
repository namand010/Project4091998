def print_formatted(number):
    # your code goes here
    for i in (1,n+1):
        print(i, end=" ")
        print(str(oct(i))[2:] , end=" ")
        a = str(hex(i))[2:]
        print(a.upper(), end=" ")
        print(str(bin(i))[2:])




if __name__ == '__main__':
    n = int(2)
    print_formatted(n)