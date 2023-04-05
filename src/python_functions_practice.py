def return_10():
    return 10

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number,second_number):
    return first_number * second_number

def divide(first_number,second_number):
    return first_number / second_number

def length_of_string(string):
    return len(string)

def join_string(string_1,string_2):
    return string_1 + string_2

def add_string_as_number(string_1,string_2):
    return int(string_1) + int(string_2)

import calendar
def number_to_full_month_name(month_number): 
    return calendar.month_name[month_number]

def number_to_short_month_name(month_number):
    return calendar.month_abbr[month_number]

# -------------------------------------------------
# Further

def volume(length):
    return length * length * length

def reverse_string(word):
    word_reversed = word[::-1]
    return word_reversed

def farenheit_to_celsius(degrees_farenheit):
    return (degrees_farenheit - 32) * 5 / 9