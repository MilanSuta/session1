# Declare two variables, a and b. Assign a the value 15 and b the value 12.
a=15
b=12

# Print the types of a and b using the type() function.
print(type(a))
print(type(b))

# Create a code script to perform an addition (a + b) and print the result
print(a+b)

# Create a code script to perform an subtract (a - b) and print the result
print(a-b)

# Create a code script to perform an multyply (a * b) and print the result
print(a*b)

# Create a code script to perform an Division (a / b) and print the result
print(a/b)

# Create a new variable c that stores the result of a divided by b. Make sure c is of type integer
c=int(a/b)

#Print the value and type of c.
print(c, type(c))

# Now convert c to a float and print its new value and type
c = (float(c))
print(c, type(c))

# Declare a string variable message with the value "The result of a divided by b is:".
message = "The result of a divided by b is:"

# Concatenate the message with the value of c (converted to a string) and print the result
con_msg = message+ " " + str(c)
print(con_msg)

# Compare if a is greater than b and print the result (True/False).
print(a>b)

# Check if a is equal to b and print the result (True/False).
print(a==b)