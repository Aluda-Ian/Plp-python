#input and output in python refers to the process of takin input from the users and displaying out put to the user

# name = input("Enter your name")
# print("hello your name is " )

#input function takes the string argumennt (prompt) which displayed to the user

#print funtion displays the out put to the user


# name = input("what is your name")
# age = input (' what is your age?')

# print("hello" + name + "! you are" +age+ "years old.") qa\M 

#input output can be used to take input from the user , display output , read and write files eg csv and text


#UNDERSATANDING HOW TO READ AND WRITE FILES IN PYTHON

# r (read only ) this mode is used to only read the contesnt of the file.
#w (wirte only )  this mode is used to write to a file . if the file exists its contents will be truncated
#and a new file with same name will be created 
#a (append Only) this mode is used to append an existing file . if the file does not exist a new file wilh the specified name will be created 
#X (write only, exclusive creation)  this mode is used to write a file only if the file does not already exists

# example

#open file for readeg

# file = open("example.txt", "r")

# #read the content of the file

# content = file.read()

# print(content)

# file.close


#how to writ a file in python

# #open file for writing
# file = open("exampe.txt", "w")

# #writ some text to the file

# file.write("hello world!?\n")
# file.write("This is a text.\n")

# #file close

# file.close()

#python file objects

#pythone has inbuilt fuctions to create ,read ,write and manipulate accessible files. the io module is te default module for accesing iles that can be used off the shelf without ev3en importing it 
#before you read and write or manipulate data you need to mae use of the module  open(filenamem access _model)


# my_file_handle = open("mynewtextfile.txt")
# my_file_handle = open("/path")
# my_file_handle = open("c://")


#how to read a file 
# file_object = open(filename, mode) #mode method
# file_object = open("example.txt") #method r read
# file_object.close()

# print(f.name)
# print(f.closed)
# print(f.mode)

#how to read a file
# file_object = open(filename,mode)
# file_contents = file_object.read()
# file_object.close()














