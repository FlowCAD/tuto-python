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


# Function called by another one
def cube(number):
  """return the cube of a number"""
  return number ** 3

def by_three(number):
  """test if a number is divisible by 3"""
  print number
  if number%3 == 0:
    print "Yes"
    return cube(number)
  else:
    print "No"
    return False

by_three(9)