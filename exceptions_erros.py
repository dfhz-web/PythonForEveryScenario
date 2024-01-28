import traceback
import sys
# google python built in exceptions, second option
class JustNotCoolError(Exception):
  pass

x=2
try:
  
  #raise JustNotCoolError("This isn't coll at all, let's solve it")
#   raise Exception("I'm a custom exception!")  # this is not commonly  being used
  #print(x/0)

#customized exception
  if not type(x) is str:

      raise TypeError("Only strings are allowed") # this value overwrite the exception under
  print(u)
  total = 2 / 0
  




# except NameError: 
#   print('NameError means something is probably undefined')
  
# except ZeroDivisionError:
#   print('Raised when the second operator in a division is zero')

# except Exception as error:
#   print(error)

except Exception as error:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Exception Type: ", exc_type)
    print("Exception Value: ", exc_value)
    
    # Extract the line number from the traceback object
    line_num = traceback.extract_tb(exc_traceback)[-1][1]
    print("Line Number: ", line_num)
else:
  print("No exception was raised")
finally:
  print('This block will always run')


#Python built -*in Exceptions
# here is a list of the exceptions
#https://www.w3schools.com/python/python_ref_exceptions.asp