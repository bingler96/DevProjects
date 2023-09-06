# We use while loops to execute block of code multiple times and there are often useful in building interactive programs and games. 
# in the code below the program will keep adding 1 to i until it reaches 6 then the statement is no longer true breaking the while loop 

i = 1 # i is used for short for index here 
while i <= 5: # while this condition is true the code in this block will be repeatedly executed
    print('*' * i) # Going to make things interesting by adding a *, with this expression we can repeat a string. When we multiply a string by a number the string will be repeated
    i = i + 1 # the reason we are adding a 1 is so i wont be 1 forever we will end up with a infinite loop 
print("Done")