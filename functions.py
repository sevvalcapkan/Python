import math
import statistics
import random
import os
import re
import urllib.request
import json
import sys
import datetime
import itertools
import functools
import sqlite3

# Mathematical Functions
abs_value = abs(-10)
divmod_result = divmod(10, 3)
power = pow(2, 3)
rounded = round(3.14159, 2)
max_value = max(4, 9, 2, 6)
min_value = min(4, 9, 2, 6)
sum_values = sum([1, 2, 3, 4, 5])
sqrt = math.sqrt(25)
sin = math.sin(0.5)
cos = math.cos(0.5)
tan = math.tan(0.5)
ceil = math.ceil(3.7)
floor = math.floor(3.7)

# Data Conversion and Type Checking
to_int = int("10")
to_float = float("3.14")
to_str = str(42)
to_bool = bool(1)
type_check = isinstance(10, int)

# Data Structures
len_list = len([1, 2, 3, 4, 5])
list_values = list((1, 2, 3, 4, 5))
tuple_values = tuple([1, 2, 3, 4, 5])
dict_values = dict(key1=1, key2=2, key3=3)
set_values = set([1, 2, 3, 4, 5])
range_values = list(range(1, 6))

# Input/Output Operations
print_output = print("Hello, World!")
user_input = input("Enter your name: ")
file = open("example.txt", "r")
file_contents = file.read()
file.close()

# String Operations
len_string = len("Hello, World!")
upper_string = "Hello, World!".upper()
lower_string = "Hello, World!".lower()
split_string = "Hello, World!".split(",")
join_string = ",".join(["Hello", "World"])
strip_string = "   Hello, World!   ".strip()

# File Operations
path_exists = os.path.exists("example.txt")
is_file = os.path.isfile("example.txt")
is_dir = os.path.isdir("example_dir")
list_dir = os.listdir("path/to/directory")
os.mkdir("new_directory")
os.remove("file_to_delete.txt")

# Regular Expressions
search_result = re.search(r"\bworld\b", "Hello, world!")
match_result = re.match(r"\bHello\b", "Hello, World!")
findall_result = re.findall(r"\b\w+\b", "Hello, World!")
sub_result = re.sub(r"\bworld\b", "Python", "Hello, world!")

# Random Number Generation
random_float = random.random()
random_int = random.randint(1, 10)
random_choice = random.choice(["apple", "banana", "cherry"])
list_to_shuffle = [1, 2, 3, 4, 5]
random.shuffle(list_to_shuffle)

# System and Environment
command_line_args = sys.argv
sys_exit = sys.exit(0)
env_vars = os.environ

# Date and Time
current_datetime = datetime.datetime.now()
custom_datetime = datetime.datetime(2023, 5, 25, 12, 30, 0)
time_difference = datetime.timedelta(days=7)

# Iteration
for number in itertools.count(1, 2):
    if number > 10:
        break

for element in itertools.cycle([1, 2, 3]):
    if element > 5:
        break

# Partial Functions
add_two_numbers = functools.partial(lambda x, y: x + y, 2, 3)
multiply_by_three = functools.partial(lambda x, y: x * y, y=3)

# SQLite Database Operations
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INT, name TEXT)")
cursor.execute("INSERT INTO example VALUES (1, 'John')")
cursor.execute("SELECT * FROM example")
results = cursor.fetchall()
connection.close()
