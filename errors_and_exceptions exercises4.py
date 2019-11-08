import logging

print('------------------------------------------------ 1')
# log messages to a file, ignoring anything less severe than ERROR
logging.basicConfig(filename='myprogram.log', level=logging.INFO)


print('------------------------------------------------ 2')

# origin:
# def print_list_element(thelist, index):
    # try:
        # print(thelist[index])
    # except IndexError as err:
        # print('Index is greater than the length of the list. Your index is %s' % err)
        # raise err


# new:
def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        logging.error('The list has no elements at index %d ' % index)


print('------------------------------------------------ 3')

# origin:
# def add_to_list_in_dict(thedict, listname, element):
#     try:
#         thelist = thedict[listname]
#     except KeyError:
#         thedict[listname] = []
#         print("Created %s." % listname)
#     else:
#         print("%s already has %d elements." % (listname, len(thelist)))
#     finally:
#         thedict[listname].append(element)
#         print("Added %s to %s." % (element, listname))


# new:
def add_to_list_in_dict(thedict, listname, element):
    try:
        thelist = thedict[listname]
    except KeyError:
        thedict[listname] = []
        logging.info("Created %s." % listname)   # print changed to logging.info
    else:
        logging.info("%s already has %d elements." % (listname, len(thelist)))
        # print changed to logging.info
    finally:
        thedict[listname].append(element)
        logging.info("Added %s to %s." % (element, listname))  # print changed to logging.info

