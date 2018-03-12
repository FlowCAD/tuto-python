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