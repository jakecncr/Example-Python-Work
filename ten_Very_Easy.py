# A function to convert a string to an integer.


def to_int(txt):
    x = int(txt)
    return x


# A function to convert an integer to a string


def to_str(num):
    y = str(num)
    return y


# A function for counting the total number of legs on a farm


def animals(chickens, cows, pigs):
    legs = chickens * 2 + cows * 4 + pigs * 4
    return legs


# Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.


def convert(hours, minutes):
    seconds = hours * 3600 + minutes * 60
    return seconds


# Create a function that takes a base number and an exponent number and returns the calculation.


def calculate_exponent(num, exp):
    solution = num ** exp
    return solution


# Create a function that takes a list of numbers. Return the largest number in the list.


def findLargestNum(nums):
    return max(nums)


# Create a function that takes a list and returns the difference between the biggest and smallest numbers.


def difference_max_min(lst):
    x = max(lst)
    y = min(lst)
    solution = x - y
    return solution


# Create a function that takes three arguments prob, prize, pay and returns True
# if prob * prize > pay; otherwise return False.


def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    else:
        return False


# Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.


def divisible_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False


# Create a function that takes a list and returns the sum of all numbers in the list.


def get_sum_of_elements(lst):
    return sum(lst)
