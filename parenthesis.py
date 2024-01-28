def outer_function_with_parentheses():
    def inner_function():
        return "Hello from inner function"
    
    return inner_function()

def outer_function_without_parentheses():
    def inner_function():
        return "Hello from inner function"
    
    return inner_function

# Using the functions
result_with_parentheses = outer_function_with_parentheses()
result_without_parentheses = outer_function_without_parentheses()

print(result_with_parentheses)
print(result_without_parentheses())
