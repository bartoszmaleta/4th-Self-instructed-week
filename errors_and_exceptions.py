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


# Code works, COMMENTED JUST TO RUN THE NEWEST CODE FASTER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# print('------------------------------------------------ Try and except statements')

# # while True
# try:
#     age = int(input("Please enter your age: "))
#     print("I see that you are %d years old." % age)
# except ValueError:
#     print("Hey, that wasn't a number!")


# print('------------------------------------------------ Try and except statements')
# try:
#     dividend = int(input("Please enter the dividend: "))
#     divisor = int(input("Please enter the divisor: "))
#     print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
# except(ValueError, ZeroDivisionError):
#     print("Oops, something went wrong!")


# print('------------------------------------------------ Try and except statements')
# try:
#     dividend = int(input("Please enter the dividend: "))
#     divisor = int(input("Please enter the divisor: "))
#     print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
# except ValueError:
#     print("The divisor and dividend have to be numbers!")
# except ZeroDivisionError:
#     print("The dividend may not be zero!")


print('------------------------------------------------ Try and except statements')
# Note that in the example above if a ValueError occurs we won’t know whether it was caused by the 
# dividend or the divisor not being an integer – either one of the input lines could cause that error. 
# If we want to give the user more specific feedback about which input was wrong, we will have to 
# wrap each input line in a separate try-except block

# try:
#     dividend = int(input("Please enter the dividend: "))
# except ValueError:
#     print("The dividend has to be a number!")

# try:
#     divisor = int(input("Please enter the divisor: "))
# except ValueError:
#     print("The divisor has to be a number!")

# try:
#     print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
# except ZeroDivisionError:
#     print("The dividend may not be zero!")

print('------------------------------------------------ Error checks vs exception handling')

# n = None
# while n is None:
#     s = input('Please enter an integer: ')
#     if s.lstrip('-').isdigit():
#         n = int(s)
#     else:
#         print('%s is not an integer.' % s)


# # with exception handling

# n = None
# while n is None:
#     try:
#         s = input('Please enter an integer2: ')
#         n = int(s)
#     except ValueError:
#         print('%s is not an integer2.' % s)


print('------------------------------------------------ The else and finally statements')
# The else and finally statements
# There are two other clauses that we can add to a try-except block: else and finally. 
# else will be executed only if the try clause doesn’t raise an exception:

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Hey, that wasn't a number!")
else:
    print("I see that you are %d years old." % age)

# When we edit this program in the future, we may introduce additional statements 
# that should also be executed if the age input is successfully converted. Some of 
# these statements may also potentially raise a ValueError. If we don’t notice this, 
# and put them inside the try clause, the except clause will also handle these 
# errors if they occur. This is likely to cause some odd and unexpected behaviour. 
# By putting all this extra code in the else clause instead, we avoid taking this risk.

# The finally clause will be executed at the end of the try-except block no matter 
# what – if there is no exception, if an exception is raised and handled,
# if an exception is raised and not handled, and even if we exit the block using break, 
# continue or return. We can use the finally clause for cleanup code that we always 
# want to be executed:

try:
    age = int(input("Please enter your age2: "))
except ValueError:
    print("Hey, that wasn't a number!")
else:
    print("I see that you are %d years old." % age)
finally:
    print("It was really nice talking to you.  Goodbye!")