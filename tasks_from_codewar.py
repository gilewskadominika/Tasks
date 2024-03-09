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
# ------------------------------------------------------------------------------------------------------------
# Your classmates asked you to copy some paperwork for them. You know that there are 'n'
# classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.


def counting_pages(n, m):
    return m * n if n > 0 and m > 0 else 0

print(counting_pages(5, 1))
# ------------------------------------------------------------------------------------------------------------
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.


def checking_array(val, arr):
    for element in arr:
        if val == element:
            return True
    return False


def is_elem_in_arr(x, a):
    return x in a
# ------------------------------------------------------------------------------------------------------------
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def get_str_from_bool(value):
    return "Yes" if value is True else "No"
# ------------------------------------------------------------------------------------------------------------
# Given two integers a and b, which can be positive or negative, find the sum of all the integers
# between and including them and return it. If the two numbers are equal return a or b.
# Note: a and b are not ordered!


def get_sum_from_a_to_b(a, b):
    sum_ = 0
    if a == b:
        return a
    elif b > a:
        for element in range(a, b+1):
            sum_ += element
    else:
        for element in range(b, a+1):
            sum_ += element
    return sum_
# ------------------------------------------------------------------------------------------------------------
# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle
# can be built with the sides of given length and false in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).


def check_triangle(a, b, c):
    if a > b and a > c:
        if b + c > a:
            return True
    elif b > a and b > c:
        if a + c > b:
            return True
    elif c > a or c > b:
        if a + b > c:
            return True
    return False
# ------------------------------------------------------------------------------------------------------------
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.


def get_initials(name):
    splitted_name = name.split()
    first = splitted_name[0][:1].upper()
    second = splitted_name[1][:1].upper()
    lst = []
    lst.append(first)
    lst.append(second)
    return '.'.join(lst)

# print(get_initials('dupa dupa'))

# def abbrev_name(name):
#     lst = []
#     x = name.split()
#     for i in x:
#         lst.append(i[0])
#     return '.'.join(lst).upper()
#
# def abbrev_name(name):
#     return '.'.join(w[0] for w in name.split()).upper()
# ------------------------------------------------------------------------------------------------------------
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?


def int_into_str(digit):
    return str(digit)
# ------------------------------------------------------------------------------------------------------------
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def get_even_or_odd(number):
    return 'Even' if number % 2 == 0 else "odd"
# ------------------------------------------------------------------------------------------------------------
# Your task is to make a function that can take any non-negative integer as an argument and return it
# with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.


def get_highest_number(number):
    number = list(str(number))
    number.sort(reverse=True)
    return ''.join(number)

# print(get_highest_number(125394))


def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))
# ------------------------------------------------------------------------------------------------------------
# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.


def check_isogram(word):
    return len(word) == len(set(word.lower()))
# ------------------------------------------------------------------------------------------------------------
