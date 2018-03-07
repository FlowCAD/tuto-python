lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]


def average(numbers):
  """calculate average of marks"""
  total = float(sum(numbers))
  total = total / len(numbers)
  return total


def get_average(student):
  """calculate global average for a student"""
  homework = average(student["homework"]) * 0.1
  quizzes = average(student["quizzes"]) * 0.3
  tests = average(student["tests"]) * 0.6
  return homework + quizzes + tests


def get_letter_grade(score):
  """give a letter grade"""
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"


def get_class_average(class_list):
  """calculate global average for the class"""
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)


for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]
  print get_average(student)
  print get_letter_grade(get_average(student))
print get_class_average(students)
print get_letter_grade(get_class_average(students))