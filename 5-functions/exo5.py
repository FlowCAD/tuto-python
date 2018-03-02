# Basic function
def spam():
  """Prints the string "Eggs!" to the console"""
  print "Eggs!"

spam()

# Function with parameters
def power(base, exponent):
  """raise the first argument to the power of the second"""
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)