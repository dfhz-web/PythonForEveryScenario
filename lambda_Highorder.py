# it is a single expression that returns a value
#anonymous functions
# we can assigne a lambda value to a variable

#takes two arguments and returns their sum:
add = lambda x, y: x + y   #arguments : expressions
print(add(5,5))

squared = lambda num, nume:  num * nume
print(squared(2,4))

addTwo = lambda num : num + 2
print(addTwo(12))

sum_total = lambda a,b : a + b
print(sum_total(2,2))

#################################
#When I don't want save for later
print('buildinding it !')
def funcBuilder(x):
    return lambda num : num + x


addTen = funcBuilder(10) # it is received as x parameter
addTwenty = funcBuilder(20)


print(addTen(7))    # the 7 es the one received that will represent num (funcBuilder)
print(addTwenty(7))


print("example")
def builder(x):
    return lambda num: num * x
exa = builder(2) # represents x as a parameter
print(exa(4))    # represents lambda num



################################################
# High order function

print("high order function with map")
numbers = [4,78,52,12,1,0]
squared_nums =  map(lambda num : num * num, numbers)
print(list(squared_nums))


###################################################
#% remainder
  #if true will be a odd number
print("high order function with filter")

#it will print all the True results
odd_nums = filter(lambda num : num % 2 == 0, numbers )
print(list(odd_nums))

##########################################
print("functools")
from functools import reduce
# acc accumulated,  crr updated value
# is used for applying a binary function in a cumulative way to the
#items of an iterable, from left to right, so as to reduce the iterable 
#to a single accumulated result.
#For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
#calculates ((((1+2)+3)+4)+5). The left argument, x, is the
#accumulated value and the right argument, y, is the update value from 
#the iterable.
#
#
number_group = [1,2,3,4,5,1]
total  = reduce(lambda acc, curr: acc + curr, number_group, 2)  # 2 is the inicializer and it is put first in the calculation
print(total)

#easier to
print("Using sum")
print(sum(number_group, 2))


###
#using str 
print("Complex")

names = ['Daniel', 'Jacob janglesssssss','sara catayi']
char_count = reduce(lambda acc, curr: acc + len(curr) ,names, 0)
print(char_count)

# high order is when it receives a function as an argument or returns a functino





 




