# Implement the following function:
# de _list_of_dice_rolls(n)
# The function is given a positive integer n. When called, it creates and
# returns a list with n dice rolls results (each is a random number 1-6).

import random

def list_of_dice_rolls(n):
    res_list = []
    for count in range(n):
        curr_roll = random.randint(1,6)
        res_list.append(curr_roll)
    return res_list

def main():
    print("Please enter a positive integer:")
    input_num = int(input())
    dice_roll_results = list_of_dice_rolls(input_num)
    print(dice_roll_results)

main()
