#numbers = [5, 2, 1, 7, 4]
#numbers.append(10) # Append adds a number to our list and by default it adds it at the end of the list 
#print(numbers)

#numbers = [5, 2, 1, 7, 4]
#numbers.insert(0, 10) # Insert adds a number where we define it to in the list, 0 in this case is the index in the list and the 10 is the number we want to add
#print(numbers)

#numbers = [5, 2, 1, 7, 4]
#numbers.remove(7) # Remove will delete the number from the list 
#print(numbers)

#numbers = [5, 2, 1, 7, 4]
#numbers.clear() # Clear removes all the items in the list this method doesn't take any values
#print(numbers)

#numbers = [5, 2, 1, 7, 4]
#numbers.pop() # Pop removes the last item in a list 
#print(numbers)

#numbers = [5, 2, 1, 7, 4]
#print(numbers.index(5)) # Index checks for the existence of an item in the list, this will return the index of the first occurrence of the item so here it would be 0
# If we pass a number here that doesn't exist we will get a error 

#numbers = [5, 2, 1, 7, 4]
#print(50 in numbers) # In is another way to check for existence of an item and is safer to user then index because if the number is not listed it will output False a boolean

#numbers = [5, 2, 1, 7, 5, 4]
#print(numbers.count(5)) # Count what this does is count the occurances of an item, since there is 2 5s here the output is 2 

#numbers = [5, 2, 1, 7, 5, 4]
#print(numbers.sort()) # Sort what this does is sorts the list, when we print it out like this it will return "None" which is an object in python thah represents the absence of a value
#numbers.sort() # This is the correct way to use this method, now all the items are assorted in ascending order least to greatest
#numbers.reverse() # This makes the list sort in decending order from greatest to least 
#print(numbers)

#numbers = [5, 2, 1, 7, 5, 4]
#numbers2 = numbers.copy() # This makes a copy of the list and if we add items to the orginal list it will not make changes to the copied one
#numbers.append(10) # This will add the 10 to the numbers list but not the copied one
#print(numbers2)

# Write a program to remove duplicates in a list

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)