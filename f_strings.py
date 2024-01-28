person= "daniel"
coins = 3

print("\n" + person + " has " + str(coins)+ " coins left")


#don't use
message = "\n%s has %s coins left" %(person, coins)
print(message)

message = "\n{} has {} coins left".format(person, coins)
print(message)

message = "\n{1} has {0} coins left".format(coins,person )
print(message)


message = "\n{person} has {coins} coins left".format(coins=coins,person=person )
print(message)

#With a dictionary 
player = {'person': 'Daniel', 'coins': 3}
message = "\n{person} has {coins} coins left".format(**player) #Call the dictionary
print(message)

#######################
#f-strings! this is the way

message = f"\n{person} has {coins}  coins left."
print(message)

message = f"\n{person} has {2*5}  coins left."
print(message)

message = f"\n{person.upper()} has {2*5}  coins left."
print(message)


#With a dictionary 
data = {'person': 'Daniel', 'coins': 3}
message = f"\n{data['person']} has {2*5}  coins left."
print(message)



### you can pass formatting options
#from now on you can try python string format method in google
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")  #just wanted 2 decimals using fix

for num in range(1,11):
   print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
   print(f"\n{num} divided by 4.52 is  {num / 4.52:.2%}")