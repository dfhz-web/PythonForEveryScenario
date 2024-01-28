import math 

# String data type


#literal assigment 
first = "Daniel"
last = "Herrera"

# print(type(first))
# print(type(first) ==  str)
# print(isinstance(first, str))

#constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) ==  str)
# print(isinstance(pizza, str))

#Concatenation
fullname = first  + " "  + last 
print(fullname)

fullname += " !"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s. "
print(statement)


#multiple lines
multiline = '''
hey, how are you?                                        

I was just checking in.                             
                                             All good?

'''
print(multiline)



# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)


#String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                        "
multiline = "             " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("   ")
#Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$2".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("   ")

#String index values
print(first[-1])  #-1 last value 
print(first[::-1])  #reversed string
print(first[0:])  

# Some methods return boolean data 
print(first.startswith("f"))
print(first.endswith("l"))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric data types

#integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
  
# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print("   ")

# Built-in functios for numbers
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa,1))

print("    ")

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Castian a string to a number
zipcode = "10000"
zip_code = int(zipcode)
print(type(zip_code))







