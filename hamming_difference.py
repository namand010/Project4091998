def TotalHammingDistance(n):
    i = 1
    sum = 0

    while n // i > 0:
        sum = sum + n // i
        i = i * 2

    return sum


if __name__ == '__main__':
    N = 9

    print(TotalHammingDistance(N))
