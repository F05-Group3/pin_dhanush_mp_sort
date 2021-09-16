from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	random_list = list(range(number))
	random.seed(seed)
	random.shuffle(random_list)
	return random_list

def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	array = gen_random_int(number, seed)

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = ",".join(list(map(str, array)))
	array_str += '.'

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():

	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	to_sort = document.getElementById("generate").innerHTML

	to_sort_list = to_sort[:-1].split(',')

	sorted_list = bubble_sort(to_sort_list)

	array_str = ','.join(sorted_list) + '.'
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	user_val_list = list(map(str, value.strip().split(',')))

	sorted_user_val_list = bubble_sort(user_val_list)

	array_str = ','.join(sorted_user_val_list) + '.'

	document.getElementById("sorted").innerHTML = array_str


def bubble_sort(array):
	for i in range(len(array)-1):
		for j in range(len(array) - i -1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array


