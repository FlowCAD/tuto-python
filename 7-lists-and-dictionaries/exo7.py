# List Slicing
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[:2]
middle = suitcase[2:4]
last = suitcase[4:]
print (first, middle, last)

# Maintaining Order
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")
print animals

# Using loops
start_list = [5, 3, 1, 2, 4]
square_list = []
for number in start_list:
	square_list.append(number ** 2)
square_list.sort()
print square_list

# Lists and Dictionaries
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pouch'].sort() 
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print inventory