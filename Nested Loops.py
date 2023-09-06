# adding one loop inside of another loop 

#for x in range(4):
    #for y in range(3):
        #print (f'({x}, {y})')

# This program gets executed we work through our first interation of the x range then we move onto the first interation of the y range and when its complete it goes back through the y range interation until it does all 3 then it goes back to the x range for the 2nd part and so on. 

numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)