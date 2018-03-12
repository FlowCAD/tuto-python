# Advanced Topics

#Iterators for Dictionaries
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}
print my_dict.items()
print my_dict.keys()
print my_dict.values()
for key in my_dict:
  print key, my_dict[key]
for number in range(5):
  print number,
for letter in "Eric":
  print letter, 


#Building Lists
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
even_squares = [i ** 2 for i in range(1, 12) if (i ** 2) % 2 == 0]
print even_squares