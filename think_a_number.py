import os
import random


def new_random_number():
    guessed_number = str(random.randint(1000, 9999))
    list_of_nums = [guessed_number[num] for num in range(4)]
    print("The guess is: %s" % guessed_number)
    return list_of_nums


def get_input():
    num_of_right_numbers = int(input("How many digits are on the correct position: "))
    return num_of_right_numbers


def generate_random_list(num_of_right_numbers, list_of_nums):
    temp_list = list_of_nums
    good_position_list = []
    # for i in range(num_of_right_numbers):

    return list_of_nums


def check_cases(num_of_right_numbers, list_of_nums):
    original_list_of_nums = list_of_nums
    good_num = {"1": None, "2": None, "3": None, "4": None}
    if num_of_right_numbers == 0:
        new_random_number()
    if num_of_right_numbers == 1:
        pass
    if num_of_right_numbers == 2:
        pass
    if num_of_right_numbers == 3:
        pass
    if num_of_right_numbers == 4:
        guessed_number = "".join(list_of_nums)
        print("Your number is: %s", % guessed_number)
    list_of_nums[0] = str(random.randint(0, 9))
    guessed_number = "".join(list_of_nums)
    print("The guess is: %s" % guessed_number)
    # if get_input() < num_of_right_numbers:
    return list_of_nums


def main():
    list_of_nums = new_random_number()
    num_of_right_numbers = get_input()
    check_cases(num_of_right_numbers, list_of_nums)


main()
