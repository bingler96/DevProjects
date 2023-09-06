#We use comparison Operators to compare a variable with a value. 

#Example 

#if tempature is greater than 30
    #it's a hot day
#otherwise if it's less than 10
    #it's a cold day
#otherwise
    #it's neither hot nor cold

# > greater then operator
# >= greater then equal to operator
# <= less then or equal to operator 
# == equality operator note this is different from the assignment operator which is one = 
# != not equal operator 

#temperature = 30 

#if temperature > 30:
    #print("It's a hot day")
#else:
    #print("It's not a hot day")

#if name is less than 3 characters long display a valiadation mark
    #name must be at least 3 characters message should be displayed
#otherwise if it's more than 50 characters long 
    #name can be a maximum of 50 characters message should be displayed
#otherwise
    #name looks good!

# we are going to need to convert the number of characters in the string to a integer so for this we use the len function len()

name = "Logan"
len(name)

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good.")