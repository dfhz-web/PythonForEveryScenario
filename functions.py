def hello_world():
    print("Hello world!")

hello_world()  # Call the function

#function to show on screen without using throughout our code
# def sum(num1, num2):  #parameters
#     print(num1 + num2)
# sum(2,4) #arguments


def sum(num1=3,num2=4):
    if (type(num1)is not int or type(num2) is not int):
        return 4
    return num1 + num2

total = sum(2,7)
print(total)


def multiple_items(*args):  #the * makes this a tuple
    print(args)
    print(type(args))   #tuples as a result 

multiple_items("daniel", "sara", 2, False)


def mult_named_items(**kwargs):  # the ** makes a dictionary 
    print(kwargs)
    print(type(kwargs))
mult_named_items(first = "daniel", last = "sara", number = 2, desicion = False)

    