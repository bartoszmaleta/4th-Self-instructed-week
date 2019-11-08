# https://python-textbok.readthedocs.io/en/stable/Errors_and_Exceptions.html

# Errors can be classified into three major groups:

# - syntax Errors
# - runtime Errors
# - logical errors

print('------------------------------------------------ Syntax errors')
# Common Python syntax errors include:

# leaving out a keyword
# putting a keyword in the wrong place
# leaving out a symbol, such as a colon, comma or brackets
# misspelling a keyword
# incorrect indentation
# empty block


print('------------------------------------------------ Runtime errors')
# When a program comes to a halt because of a runtime error, we say that it has crashed.
# Some examples of Python runtime errors:

# division by zero
# performing an operation on incompatible types
# using an identifier which has not been defined
# accessing a list element, dictionary value or object attribute which doesn’t exist
# trying to access a file which doesn’t exist


print('------------------------------------------------ Logical errors')
# However, more frequently these kinds of errors are caused by programmer carelessness. Here are some examples of mistakes which lead to logical errors:

# using the wrong variable name
# indenting a block to the wrong level
# using integer division instead of floating-point division
# getting operator precedence wrong
# making a mistake in a boolean expression
# off-by-one, and other numerical errors

print('------------------------------------------------ Try and except statements')

# while True
try:
    age = int(input("Please enter your age: "))
    print("I see that you are %d years old." % age)
except ValueError:
    print("Hey, that wasn't a number!")

try:
    dividend = int(input("Please enter the dividend: "))
    divisor = int(input("Please enter the divisor: "))
    print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
except(ValueError, ZeroDivisionError):
    print("Oops, something went wrong!")