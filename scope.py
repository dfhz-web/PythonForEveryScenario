# this is a global scope, it will be available in everything in this file
name = "Daniel"
count = 1

#local scope



# greet("Jhon")

# give a value to a global variable within a function
def another():
  color = "Blue"
  global count
  count += 1
  print(count)
  
    
  def greet(name):   #parameter
      nonlocal color  # to use color from parent function
      color = "red"
      print(color)
      print(name)
  greet("Dave")

another()
# print(count)