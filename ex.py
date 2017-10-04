import python_utility

def my_function(d):
  _ = python_utility.Util()
  return _.is_empty(d)


a = ""
b = 123
c = 12.3
dictionary = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}#{}
_array = [1, 2, 3, 4, "5", "hello", 6]#[]
# print(type(_array))
u = python_utility.Util()
print(my_function(a))

print(u.is_int(a))