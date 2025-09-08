import example as addition

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# call the add function from module
result = addition.add(a, b)

print("The sum is:", result)
