# Python file I/O (input/output)

#Writing the result of a list comprehension in an output file
my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
for i in my_list:
  my_file.write(str(i)+ "\n")
my_file.close()


#Reading the written data
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()


#Writing data and automaticaly open/close the concerned file
with open("text.txt", "w") as textfile:
  textfile.write("Success!")


#Checking if the file is closed
if not textfile.closed:
  textfile.close()
print textfile.closed