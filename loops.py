#while loop

value = 1
secondValue= 2

#While with break
#Break stops the loop 
# while secondValue <=10:
#     print(secondValue)
#     if secondValue == 5:
#         break
#     secondValue += 1


#SEPERATED BREAK AND CONTINUE

#continue stops at the link, but it starts from loop at the start
#Without going deeper in the cycle

#While with continue
# while value <=10:
    
#     value += 1
#     if value == 5:
#         continue
#     print(value)  # it does not print 5 
# else:
#     print("value is now"+ ' ' + str(value))

names = ["Daniel", "Sara", "John"]
#Use of the for 
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)


# for x in names:
#     if x == "Sara":
#         continue
#     print(x)


# for x in range(4):
#     print(x)

# for x in range(2,4):
#     print(x)

for x in range(12,125,12):
    print(x)
else:
    print("Glad that\'s over and the x value is" +" "+  str(x))

#************************
    
#Nested loops
names = ["Daniel", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + "  " + action + " .")



for action in actions:
    for name in names:
        print(name + "  " + action + " .")



