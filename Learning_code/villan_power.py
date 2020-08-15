# a Fight game has become popular
# n - no of villians (each having strength)
# N - User playing game (energy/strength)1

# if you want to kill a villian need stength to be greater than from villian power
# maxxy -> win if enery_alloted - no if villian kill
#
#     n -> no. of testcases "t"
#     no of villiand and no of playing user
#     consists n


# for i in range(number_test_case):
#     number_of_users = int(input())
#     for j in range(number_of_users):
#         villan_power.append(input().split())
#         player_power.append(input().split())
#
# count = 0
# for i in range(number_of_users):
#     if player_power[i] > villan_power[i]:
#         count += 1
#     else:
#         continue
#
# if count == player_power:
#     print("WIN")
# else:
#     print("LOSS")


class win_loss:
    def __init__(self):
        self.count = 0

    def check_power(self, number, villan_power, player_power):
        for i in range(number):
            if player_power[i] > villan_power[i]:
                self.count += 1
            else:
                return False
        return True



number_test_case = int(input())
villan_power = []
player_power = []
test = win_loss()
for i in range(number_test_case):
    number_of_users = int(input())
    villan_power = input().split()
    player_power = input().split()
    if test.check_power(number_of_users, villan_power, player_power):
        print("WIN")
    else:
        print("LOSS")








