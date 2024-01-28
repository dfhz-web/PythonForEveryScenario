# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a function to square a number
def square(x):
    return x ** 2

# Use map() to apply the square function to each item in the list
squared_numbers = map(square, numbers)

# Convert the result to a list and print it
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)