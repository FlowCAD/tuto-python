# Taking a Vacation
def hotel_cost(nights):
  """Calculate cost by nights"""
  return 140 * nights

def plane_ride_cost(city):
  """Calculate cost of flights"""
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  """Calculate cost of renting a car"""
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost


def trip_cost(city, days, spending_money):
  """Calculate cost of all the trip"""
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money


print trip_cost("Los Angeles", 5, 600)