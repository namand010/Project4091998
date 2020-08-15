# getMissingNo takes list as argument
# def getMissingNo(A):
#     n = len(A)
#     total = (n + 1) * (n + 2) / 2
#     sum_of_A = sum(A)
#     return total - sum_of_A
#
#
# # Driver program to test the above function
# A = [21, 22, 24, 25, 26]
# miss = getMissingNo(A)
# print(miss)
# # This code is contributed by Pratik Chhajer

def missing_numbers(num_list):
    sum = 0
    org = 0
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    # for x in range(num_list[0], num_list[-1] + 1):
    #     sum += x
    # print(sum)
    # for x in num_list:
    #     org += x
    # print("value ", sum - org)
    print(original_list)
    num_list = set(num_list)
    print(num_list)
    return (list(num_list ^ set(original_list)))


print(missing_numbers([1, 2, 3, 4, 5, 6, 7, 9, 10]))
print(missing_numbers([20, 21, 22, 24, 25]))
