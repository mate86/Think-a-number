import os
import random


def initialize():
    guessed_number = str(random.randint(1000, 9999))
    list_of_nums = [guessed_number[num] for num in range(4)]
    print_number(list_of_nums)
    return list_of_nums


def get_input():
    num_of_right_numbers = int(input("How many digits are in the correct position: "))
    return num_of_right_numbers


def print_number(list_of_nums):
    guessed_number = "".join(list_of_nums)
    print("The guess is: %s" % guessed_number)


def new_numbers(list_of_nums, num_of_right_numbers):
    new_numbers_index = []
    new_numbers_index.append(random.randint(0, 3))
    while len(new_numbers_index) < 4 - num_of_right_numbers:
        index = random.randint(0, 3)
        if index in new_numbers_index:
            continue
        new_numbers_index.append(index)

    for i in new_numbers_index:
        list_of_nums[i] = str(random.randint(0, 9))
    return list_of_nums


def check_number(list_of_nums):
    guessed = False
    num_of_right_numbers = get_input()
    if num_of_right_numbers == 4:
        guessed = True
        return guessed
    new_numbers(list_of_nums, num_of_right_numbers)  # Generates the new digits
    print_number(list_of_nums)
    return guessed


def main():
    list_of_nums = initialize()
    # final_number = [0, 0, 0, 0]
    guessed = False
    while True:
        guessed = check_number(list_of_nums)
        if guessed == True:
            print("Win! The number is guessed!")
            return
        continue

main()
