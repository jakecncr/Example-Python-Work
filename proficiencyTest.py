# Interview level Python challenges


# FizzBuzz challenge
# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, return the number


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0 and num % 5 != 0:
        return "Fizz"
    elif num % 3 != 0 and num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

# Imagine a circle and two squares: a smaller and a bigger one.
# For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
# Create a function, that takes an integer (radius of the circle)
# and returns the difference of the areas of the two squares.


def square_areas_difference(r):
	aBigSquare = (2 * r) ** 2
	aSmallSquare = r**2 + r**2
	return aBigSquare - aSmallSquare