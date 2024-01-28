#Dictionaries 
#are used to store data values that are in key values pairs

band = {
    "vocals" : "Plant",
    "guitar" : "page"
}

band2 = dict(vocals="Planty", guitar="swera", alt="de")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

#List all values   # also I can list all keys if I want to
print(band.values())

#list of key/values paris as tuples
print(band.items())

#verify a key exists
print("guitar" in band)
print("guitareeee" in band)

#Changhe values 
band["vocals"] = "Coverdale"
# print(band)
band.update({"base" : "HWD"})
print(band)


#Remove items
#1remove
print(band.pop("base"))
print('****')
print(band)

print('****')

#Added
band["drums"] = "Bonham"
print(band)


#REmove last added
print('*it removes the last item added***')
print(band.popitem())  #tuple
print('****')
print(band)


#Delete and clear
band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print('enmpty dict')
print(band2)

del band2


#Copy dictionaries in the bad way with an reference
# band2 = band  #create a reference 
# print(band2)
# del band["vocals"]
# print("bad copy")
# print(band)
# print(band2)

#Copy dictionaries
band2 = band.copy()
band2["drumnss"] = "Luis"
print(band)
print(band2)

#or use the dictionary constructor function
band3 = dict(band)
print("Good copy")
print(band3)


#Nested dictionaries
member1 = {
    "name" : "Plant",
    "instrument" : "vocals"
}
member2 = {
    "name" : "Page",
    "instrument" : "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
#
print(band["member1"]["name"])



#SETS
#formal and final data collected type
nums = {1,2,3,4,5}
nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#No duplicates allowed 
nums = {1,2,2,2,3,3}
print(nums)

#True is a dupe of 1, False is a dupe 
# of zero
nums = {1, True, 2, False ,3,4,0}
print(nums)

#Check if a value is in a set
print(2 in nums)


#But you cannot refer to an element in the set with an 
#index position or a key

#Add a new element to a set
nums.add(8)
print(nums)

#Add elements from one set to another
users = ['Dave', 'Daniel', 'Sara']  #this is a list
nums.update(users)
print(nums)
print(type(nums))


#You can use update with lists, 
# tuples, and dictionaries too 


#Merge two sets to create a new set
one ={1,2,3}
two= {3,4,5}
three = one.union(two)
print(three)


#keep only the duplicates
one ={1,2,3,4}
two= {5,6,7,8,1}

one.intersection_update(two)
print("one")
print(one)
print("two")
print(two)


#keep everything except the duplicates
one ={1,2,3,4}
two= {1,2,3}

one.symmetric_difference_update(two)
print(one)


