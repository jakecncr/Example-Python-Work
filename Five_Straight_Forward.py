#Luke Skywalker has family and friends. Help him remind them who is who.
#Given a string with a name, return the relation of that person to Luke.


def relation_to_luke(name):
	if 'Vader' in name:
		return 'Luke, I am your father.'
	elif 'Leia' in name:
		return 'Luke, I am your sister.'
	elif 'Han' in name:
		return 'Luke, I am your brother in law.'
	elif 'R2D2' in name:
		return 'Luke, I am your droid.'


# Return the total number of possible paths a salesman can travel, given n paths.


import math
def paths(n):
	return math.factorial(n)


# Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice
# with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.


def stutter(word):
	return word[0:2] + '... ' + word[0:2] + '... ' + word + '?'


# Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded
# to the nearest hundredth. See the resources tab for the formula.


import math
def cone_volume(h, r):
    x = r*r
    x = math.pi * x
    h = h/3
    sol = x*h
    return round(sol,2)


#Principles of readable code: make the following function as readable as you can.


def are_true(a, b):
	if a == True and b == True:
		return "both"
	elif a == True and b != True:
		return "first"
	elif a != True and b == True:
		return "second"
	else:
		return "neither"