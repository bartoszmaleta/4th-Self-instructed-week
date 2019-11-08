# print('------------------------------------------------ The with statement, Using the exception object')
# Code works, COMMENTED JUST TO RUN THE NEWEST CODE FASTER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# try:
#     age = int(input("Please enter your age: "))
# except ValueError as err:
#     print(err, '\nwrong type')
#     print('You enterd incorrect age input: %s ' % err)


# print('------------------------------------------------ Raising exceptions')
# # We can raise exceptions ourselves using the raise statement:

# try:
#     age = int(input("Please enter your age: "))
#     if age < 0:
#         raise ValueError("\n{} is not a valid age. Age must be positive or zero.".format(age))
# except ValueError as err:
#     print("You entered incorrect age input: %s" % err)
# else:
#     print("I see that you are %d years old." % age)

# Here are a few common exception types which we are likely to raise in our own code:

# TypeError: this is an error which indicates that a variable has the wrong type for some operation. 
# We might raise it in a function if a parameter is not of a type that we know how to handle.

# ValueError: this error is used to indicate that a variable has the right type but the wrong value. 
# For example, we used it when age was an integer, but the wrong kind of integer.

# NotImplementedError: we will see in the next chapter how we use this exception to indicate 
# that a class’s method has to be implemented in a child class.

print('------------------------------------------------ Raising exceptions')

# Something we may want to do is raise an exception that we have just 
# intercepted – perhaps because we want to handle it partially in the current function, 
# but also want to respond to it in the code which called the function:

try:
    age = int(input("Please enter your age: "))
except ValueError as err:
    print("You entered incorrect age input: %s" % err)
    raise err