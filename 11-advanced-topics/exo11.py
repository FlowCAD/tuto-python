# Advanced Topics

#Iterators for Dictionaries
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}
print "tuples: ", my_dict.items()
print "keys: ", my_dict.keys()
print "values: ", my_dict.values()
for key in my_dict:
  print key, my_dict[key]
for number in range(5):
  print number,
for letter in "Eric":
  print letter, 


#Building Lists
evens_to_30 = [i for i in range(31) if i % 2 == 0]
print "evens_to_30: ", evens_to_30
even_squares = [i ** 2 for i in range(1, 12) if (i ** 2) % 2 == 0]
print "even_squares: ", even_squares


#List Slicing
l = [i ** 2 for i in range(1, 11)]  # Devrait etre [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]  # Donne [9, 25, 49, 81]
to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14]
print "to_21: ", to_21
print "odds: ", odds
print "middle_third: ", middle_third


#Anonymous Functions
my_list = range(16)
print "by tree only: ", filter(lambda x: x % 3 == 0, my_list)