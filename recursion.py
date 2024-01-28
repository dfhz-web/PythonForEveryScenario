def add_one(num):
    if(num >=9):
        return num +1  #when it reaches 10 will be stored
    total = num + 1
    print(total)

    return add_one(total)

add_one(1)
mynewtotal = add_one(1)  #here 
print(mynewtotal)    # print and you get 10

#got it


