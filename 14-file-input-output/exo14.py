# Python file I/O (input/output)

#Writing the result of a list comprehension in an output file
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for i in my_list:
  my_file.write(str(i)+ "\n")
  
my_file.close()