print('------------------------------------------------ 1')
# Code works, COMMENTED JUST TO RUN THE NEWEST CODE FASTER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# person = {}

# properties = [
#     ("name", str),
#     ("surname", str),
#     ("age", int),
#     ("height", float),
#     ("weight", float),
# ]

# # for prop, p_type in properties:

#     # person[prop] = p_type(input("Please enter your %s: " % prop))
# print(person)


# exiting_variable0 = None
# while exiting_variable0 is None:
#     ask_name = input('Whats your name? ')
#     if not ask_name.isdigit():
#         person["name"] = ask_name
#         exiting_variable0 = 0
#     else:
#         print('Hey, it wasn\'t string')

# person["surname"] = input('whats your surname? ')

# exiting_variable_surname = None
# while exiting_variable_surname is None:
#     ask_surname = input('Whats your surname? ')
#     if not ask_surname.isdigit():
#         person["surname"] = ask_surname
#         exiting_variable_surname = 0
#     else:
#         print('Hey, it wasn\'t string')

# exiting_variable_age = None
# while exiting_variable_age is None:
#     try:
#         person["age"] = int(input('Whats your age? '))
#         exiting_variable_age = 0
#     except ValueError:
#         print('Hey, that wasn\'t a number')

# exiting_variable_heigt = None
# while exiting_variable_heigt is None:
#     try:
#         person["height"] = int(input('Whats your height? '))
#         exiting_variable_heigt = 0
#     except ValueError:
#         print('Hey, that wasn\'t a number')

# exiting_variable_weight = None
# while exiting_variable_weight is None:
#     try:
#         person["weight"] = int(input('Whats your weight? '))
#         exiting_variable_weight = 0
#     except ValueError:
#         print('Hey, that wasn\'t a number')

# print(person)

print('------------------------------------------------ Answer on website')
# not correct, because doesn't inculde string from name and surname!!!


# person = {}

# properties = [
#     ("name", str),
#     ("surname", str),
#     ("age", int),
#     ("height", float),
#     ("weight", float),
# ]

# for property, p_type in properties:
#     valid_value = None

#     while valid_value is None:
#         try:
#             value = input("Please enter your %s: " % property)
#             valid_value = p_type(value)
#         except ValueError:
#             print("Could not convert %s '%s' to type %s. Please try again." % (property, value, p_type.__name__))

#     person[property] = valid_value

# print(person)


print('------------------------------------------------ 2')


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print('Index is greater than the length of the list')


print('------------------------------------------------ 3')


def add_to_list_in_dict(thedict, listname, element):
    try:
        thelist = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(thelist)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))