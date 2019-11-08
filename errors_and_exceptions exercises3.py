print('------------------------------------------------ 1')
person = {}

properties = [
    ("name", str),
    ("surname", str),
    ("age", int),
    ("height", float),
    ("weight", float),
]

for property, p_type in properties:
    valid_value = None

    while valid_value is None:
        try:
            value = input("Please enter your %s: " % property)
            valid_value = p_type(value)
        except ValueError as ve:  # just added 'as ve'
            print("Could not convert %s '%s' to type %s. Please try again." % (property, value, p_type.__name__))
            print(ve)  # just added this line

    person[property] = valid_value

print(person)


print('------------------------------------------------ 2')
try:
    age = int(input("Please enter your age: "))
except ValueError as err:
    print("You entered incorrect age input: %s" % err)
    raise err