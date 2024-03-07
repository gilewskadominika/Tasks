# zadania z codewars
# ------------------------------------------------------------------------------------------------------------
# zadanie na sumę cyfr z dowolnie długiej listy, zawierającej int, float i - wartości, gdy [] ma zwracać 0
def get_sum(digits):
    return sum(digits)
# ------------------------------------------------------------------------------------------------------------
# zadanie ma zwrócić daną liczbę jako odwróconą listę cyfr po ,


def get_reversed_digits(digits):
    list_of_digits = []
    for digit in str(digits):
        list_of_digits.append(digit)
    result = list_of_digits[::-1]
    return result


print(get_reversed_digits(23454))

# ------------------------------------------------------------------------------------------------------------
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
# Use conditionals to return the proper message:
# case	                return
# name equals owner	    'Hello boss'
# otherwise	            'Hello guest'


def greetings(name, owner):
    if name == owner:
        return 'Hello boss'
    return 'Hello guest'
# ------------------------------------------------------------------------------------------------------------
# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language )
# that receive a list of integers as input, and return the largest and lowest number in that list, respectively.


def get_min(digits):
    my_min = digits[0]
    for digit in digits:
        if digit < my_min:
            my_min = digit
    return my_min


def get_max(digits):
    my_max = digits[0]
    for digit in digits:
        if digit > my_max:
            my_max = digit
    return my_max
# ------------------------------------------------------------------------------------------------------------
# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.


def get_area_or_perimeter(length, width):
    if length == width:
        return length * width
    return 2 * length + 2 * width
# ------------------------------------------------------------------------------------------------------------
# Complete the solution so that it reverses the string passed into it.


def get_reversed(words):
    return words[::-1]
# ------------------------------------------------------------------------------------------------------------
# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:


def find_needle(array):
    return f'found th needle at position {array.index('needle')}'
# print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
# ------------------------------------------------------------------------------------------------------------
# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.


def get_math(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    if operation == '-':
        return value1 - value2
    if operation == '/':
        return value1 / value2
    if operation == '*':
        return value1 * value2
# ------------------------------------------------------------------------------------------------------------
# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element
# ( by value, not by index! ).
# The highest or lowest element respectively is a single element at each edge, even if there are more
# than one with the same value.
# Mind the input validation. If an empty value ( null, None, Nothing etc. ) is given instead of an array,
# or the given array is an empty list or a list with only 1 element, return 0.


def get_summy(array):
    if array is None or array == 0 or array == [] or len(array) == 1:
        return 0
    my_min = array[0]
    my_max = array[0]
    for element in array:
        if element > my_max:
            my_max = element
        if element < my_min:
            my_min = element
    return sum(array) - my_max - (my_min)


def get_sum_arr(arr):
    return sum(arr) - max(arr) - min(arr)


def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0