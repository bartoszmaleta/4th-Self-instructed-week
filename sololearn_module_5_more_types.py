# None
print(None)

print('------------------------------------------------')


def some_func():
    print("Hi!")


some_func()
var = some_func()
print(var)


print('------------------------------------------------ Dictionaries')
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)


print('------------------------------------------------')
nums = {
    1: "one",
    2: "two",
    3: "three",
}

print(1 in nums)
print("three" in nums)
print(4 not in nums)

print('------------------------------------------------')
pairs = {
    1: "apple",
    "orange": [2, 3, 4], 
    True: False,        # 1 is True? 
    None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

print('------------------------------------------------ Tuples')
words = ("spam", "eggs", "sausages",)

print(words[0])
# Trying to reassign a value in a tuple causes a TypeError.

print('------------------------------------------------ Tuples')
my_tuple = "one", "two", "three"
print(my_tuple[0])

tpl = ()
# Tuples are faster than lists, but they cannot be changed

print('------------------------------------------------ List slices')
# If the first number in a slice is omitted, it is taken to be the start of the list.
# # If the second number is omitted, it is taken to be the end.
# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

print('------------------------------------------------ List slices')
# Negative values can be used in list slicing (and normal list indexing). 
# When negative values are used for the first and second values in a slice 
# (or a normal index), they count from the end of the list.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

print('------------------------------------------------ List comprehensions')
# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
# For example, we can do the following:
# a list comprehension

cubes = [i**3 for i in range(5)]
print(cubes)

nums = [i*2 for i in range(10)]
print(nums)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

a = [i for i in range(20) if i % 3 == 0]
print(a)

# even = [2*i for i in range(10**100)]    # MemoryError
# This issue is solved by generators, which are covered in the next module.

print('------------------------------------------------ String formatting')
nums = [4, 5, 6]
msg = ("Numbers: {} {} {}".format(nums[0], nums[1], nums[2]))
print(msg)

msg2 = f'Hello, {nums}!'
print(msg2)

print('------------------------------------------------ String functions')
# Python contains many useful built-in functions and methods to accomplish common tasks.
# join - joins a list of strings with another string as a separator.

# replace - replaces one substring in a string with another.

# startswith and endswith - determine if there is a substring at the start 
# and end of a string, respectively.

# To change the case of a string, you can use lower and upper.

# The method split is the opposite of join, turning a string with a certain 
# separator into a list.

# Some examples:

print(", ".join(["spam", "eggs", "ham"]))
# prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
# prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
# prints "['spam', 'eggs', 'ham']"

print('------------------------------------------------ Numeric functions')
# To find the maximum or minimum of some numbers or a list, you can use max or min.

# To find the distance of a number from zero (its absolute value), use abs.

# To round a number to a certain number of decimal places, use round.

# To find the total of a list, use sum.

# Some examples:

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

print('------------------------------------------------ List functions')
# Often used in conditional statements, all and any take a list as an argument, 
# and return True if all or any (respectively) of their arguments evaluate to True 
# (and False otherwise).

# The function enumerate can be used to iterate through the values and indices of a list 
# simultaneously.

# Example:

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print('All larger than 5')

print('------------------------------------------------ List functions')
if any([i % 2 == 0 for i in nums]):
    print('At least one is even')

print('------------------------------------------------ List functions')
for v in enumerate(nums):
    print(v)

