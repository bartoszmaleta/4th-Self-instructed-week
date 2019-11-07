# # Everything works! Commented, because it raises errors! Module is about handling errors!

# # ------------------------------------------------
# # try:
# #     num = 5 / 0
# # except:     # should use specific error handling!
# #     print("An error occurred")
# #     raise

# # ------------------------------------------------
# # print(1)
# # assert 2 + 2 == 4
# # print(2)
# # assert 1 + 1 == 3
# # print(3)

# # ------------------------------------------------
# # temp = 10
# # assert (temp >= 0), "Colder than absolute zero!"

# # ------------------------------------------------
# myfile = open("filename.txt")

# # ------------------------------------------------
# # write mode
# open("filename.txt", 'w')

# # read mode
# open("filename.txt", 'r')
# open('filename.txt')

# # binary write mode
# open('filename.txt', 'wb')
# # You can use the + sign with each of the modes above to give them extra 
# # access to files. For example, r+ opens the file for both reading and writing.

# # ------------------------------------------------
# file = open('filename.txt', 'w')
# # do stuff to the file
# file.close()

# ------------------------------------------------
file = open('filename.txt', 'r')
cont = file.read()
print(cont)
file.close()

# ------------------------------------------------
# To read only a certain amount of a file, you can provide a number as an argument 
# to the read function. This determines the number of bytes that should be read.


print('------------------------------------------------')
file = open('filename.txt', 'r')
print(file.read(16))

print('------------------------------------------------')
print(file.read(12))

print('------------------------------------------------')
print(file.read(3))
file.close()

print('------------------------------------------------')
# print 4 charater of the text in 21 lines
# file = open("filename.txt", "r")
# for i in range(21):
#     print(file.read(4))
# file.close()

print('------------------------------------------------')
# After all contents in a file have been read, any attempts to read 
# further from that file will return an empty string, because you are 
# trying to read from the end of the file

# file = open("filename.txt", "r")
# print(file.read())
# print("Re-reading")
# print(file.read())
# print("Finished")
# file.close()

# print('------------------------------------------------')
# file = open('filename.txt', 'r')
# print(file.readline())
# file.close()

# print('------------------------------------------------')
# file = open('filename.txt', 'r')

# for line in file:
#     print(line)

# file.close()

print('------------------------------------------------')
# The "w" mode will create a file, if it does not already exist.
file = open('newfile2.txt', 'w')
file.write('This has been written to a file')
file.close()

file = open('newfile.txt', 'r')
print(file.read())
file.close()

print('------------------------------------------------')
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

print('------------------------------------------------')
msg = 'hello world'
file2 = open('newfile3.txt', 'w')
amount_written = file2.write(msg)
file2 = open('newfile3.txt', 'r')
reading_file2 = file2.read()
print(reading_file2)
print(amount_written)
file2.close()

print('------------------------------------------------')
try:
    f = open("filename2.txt", 'w')
    f.write('Some test text')
    f = open('filename2.txt', 'r')
    print(f.read())
finally:
    f.close()

print('------------------------------------------------')
# The file is automatically closed at the end of the with statement, 
# even if exceptions occur within it.

with open('filename2.txt') as f:
    print(f.read())
