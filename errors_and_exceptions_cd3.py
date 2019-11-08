import logging

print('------------------------------------------------ Debugging programs')

# pdb
# pdb is a built-in Python module which we can use to debug a program while it’s running. 
# We can either import the module and use its functions from inside our code, or 
# invoke it as a script when running our code file. We can use pdb to step through our program, 
# either line by line or in larger increments, inspect the state at each step, and 
# perform a “post-mortem” of the program if it crashes.

# Here is how we would use pdb in our code:

# import pdb

# ---------------------------------------------
# def our_function():
    # bad_idea = 3 + "4"


# pdb.run('our_function()')
# ---------------------------------------------
# Here is how we would run it as a script:

# python3 -m pdb ourprogram.py
# More extensive documentation, including the full list of commands which can be used inside the debugger, can be found at the link above.


print('------------------------------------------------ Logging')

# There is a consistent set of logging level names which most languages use. 
# In order, from the highest value (most severe) to the lowest value (least severe), they are:

# CRITICAL – for very serious errors
# ERROR – for less serious errors
# WARNING – for warnings
# INFO – for important informative messages
# DEBUG – for detailed debugging messages


# log messages to a file, ignoring anything less severe than ERROR
logging.basicConfig(filename='myprogram.log', level=logging.ERROR)

# these messages should appear in our file
logging.error("The washing machine is leaking!")
logging.critical("The house is on fire!")

# but these ones won't
logging.warning("We're almost out of milk.")
logging.info("It's sunny today.")
logging.debug("I had eggs for breakfast.")

# There’s also a special exception method which is used for logging exceptions. 
# The level used for these messages is ERROR, but additional information about the 
# exception is added to them. This method is intended to be used inside exception 
# handlers instead of error:

try:
    age = int(input("How old are you? "))
except ValueError as err:
    logging.exception(err)

print(logging)