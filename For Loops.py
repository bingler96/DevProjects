# for loop - control flow structure that allows you to iterate over a sequence of elements (list, tuple, string, or other iterable objects) and perform a set of statements for each element in the sequence. 
# commonly used when you want to repeat a block of code a specific number of times or when you want to process each item in a collection one by one
# tuple - an ordered, immutable collection of elements. Very similar to lists.
# immutable - once you create a tuple you cannot change its contents (add, remove, or modify elements) Often used when you want to ensure that the order of elements remains constant. 
# we can define lists using []
# range() function used for creating a range of numbers 
#for item in 'Python': #this will output Python making a new line per letter 1)P 2)y 3)t 4)h 5)o 6)n
    #print (item)

#for item in ['logan', 'Anna', 'Landen', 'Logan Jr']: #another example with a list 
    #print(item)

#for item in range(10): # this will display numbers 0-9 per line example with the range function 
    #print(item)

#for item in range(500, 510): #this example we can range from a set of numbers with a starting point and a ending 
    #print(item)

#for item in range(5, 10, 2): # we can pass a step in the range function the 2 makes this skip 6 and 8 
    #print(item)

prices = [10, 20, 30] # we wanted to add all the numbers in this cart 
total = 0 # had to define a variable for the totaL and the starting cost was 0 
for price in prices:
    total += price # used augmented assignment operator to simplify the code the longer way to write this would be *total = total + price*
print(f"Total: {total}")