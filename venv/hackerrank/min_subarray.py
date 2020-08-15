from hackerrank import unit_f


# print(arr[])

def minArray(arr, wind):
    # wind = 3
    vcf = []
    tmp = 0
    for i in range(len(arr) - (wind - 1)):
        temp = sorted(arr[i:i + wind])
        print(temp)
        diff = temp[-1] - temp[0]
        # if diff not in vcf:
        vcf.append(diff)
    return vcf[0], vcf[-1]

    # print(vcf[0])
    # print(vcf[-1])




