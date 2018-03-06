# A Day at the Supermarket
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}


def calculate_stock_price(items):
  """calculate the price of all the stock"""
  total = 0
  for key in items:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    total += prices[key] * stock[key]
  return total


def compute_bill(food):
  """calculate the price of my shopping list"""
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total


shopping_list = ["banana", "orange", "apple"]


print 'The price of all the stock is: ' + str(calculate_stock_price(stock))
print 'The price of my shopping list is: ' + str(compute_bill(shopping_list))
print 'The price of all the stock is: ' + str(calculate_stock_price(stock))