users = ['Dave', 'Daniel', 'Sara']
data = ['Dave', 42, True]
emptylist=[]

print("Dave" in emptylist)
print(users[0])
print(users[-1])   #the last data
print(users[-2])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))
#add data from a certain posotion when using a loop, it is possible example
# words.append(line[1:])

#Add data
users.append('elsa')
print(users)

#Add another list 
users += ['Jason']
print(users)

#Extend another array 
users.extend(['Robert', 'Jimmy'])
print('trying')
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

#add values in a certain position
users[2:2] = ['Eddi','Alex']
print(users)

#replace values
users[1:5] = ['Robert', 'jPH']
print(users)

#remove
users.remove('Bob')
print(users)


#return the last value in our list
print(users.pop())

#if we print user, the last value will be not added     
print(users)

#remove
del users[0]
print(users)

del data
#if u try to print it will be no data to show , and an error instead 

#clear
dataa = ['daniel', 'felipe']
dataa.clear()
print(dataa)


#sort order alphabetical with slice 
print('****')
print(users)
users[1:2] = ['sara']
users.sort()
print(users)

#sort with arguments within
#in that way sort respects capitalize and lower case to alphabetize
users.sort(key=str.lower)
print(users)


# sort, order everything numerically 
my_list = [4, 2, 8, 1, 5]
my_lists = [4, 2, 8, 1, 5]
my_list.reverse()
print(my_list)

#get the list descending with the key by saving the value
my_lists.sort(reverse=True)
print(my_list)

#same thing as previously without saving the value
print(sorted(my_list, reverse=True))
print(my_list)

# how to make a copy
my_list_copy = my_list.copy()
mynums = list(my_list)
myycopy = my_list[:]
print(my_list_copy)
print(mynums)
print(myycopy)


#check typy of list
print(type(my_list))

#created list 
mylist = list([1, 'nellu', True])
print(mylist)


#TUPLES 
#list except data inside will not change, and the order will no change

mytuple = tuple(('Daniel', 42, True))
anothertuple = (1,4,2,3,2,2,2)

print(mytuple)
print(anothertuple)
print(type(mytuple))

#adding packing the tuple, unpacked the tuple, and the packed
newlist = list(mytuple)
newlist.append('neil')
newtuple = tuple(newlist)
print(newlist)


(*one, two, hey) = anothertuple


print('**********')
print(one)
print(two)
print(hey)
print('**********')
print(anothertuple.count(2))