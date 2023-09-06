#names = ['John', 'Bob', 'Logan', 'Sarah', 'Anna']
#print(names) # the output of this will be exatly as it is defined in the names variable with the [] 


#names = ['John', 'Bob', 'Logan', 'Sarah', 'Anna']
#print(names[1]) # we can access individual characters in a string using an index inside the {} this will show Bob as the index of 1 
# we can also pass a negative index and that would start which the characters at the end of the string so it would return Anna

#names = ['John', 'Bob', 'Logan', 'Sarah', 'Anna']
#print(names[2:]) # we use a : to select a range of items, from here it will return names ['Logan', 'Sarah', 'Anna']  
# Leaving the [2:] the empty space after the : is a default value so it will always return items til the end of the list 
# The [] does not modify our original list they return a new list

#names = ['John', 'Bob', 'Logan', 'Sarah', 'Anna']
#print(names[2:4]) # This is specifying a end index, this will return all the items up until this index, The output would be ['Logan', 'Sarah']

#names = ['John', 'Bob', 'Logan', 'Sarah', 'Anna']
#names[0] = 'Jon' # We can also modify our list by doing this, we list the index we are modifying then the correction we are making
#print(names)

# Write a program below that can find the highest number in a list

numbers = [3, 6, 2, 8, 4, 10] # This is defining a list with random numbers
max = numbers[0] # To define the largest number in this list we needed to define another variable, Intially we want to assume the first item in the list is the largest number. More than likely this is wrong so we need to iterate over this list, therefore we need to loop through it. Get each item and compare it with max. If it's greater than Max, then we need to reset max to that number. 
for number in numbers: # This is the iteration over the list, the loop 
    if number > max: # If we come across a number greater then max 
        max = number # Max is now set to the greater number
print(max) # This will print out the highest number in the list