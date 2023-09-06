secret_number = 9 
guess_count = 0 # this represents the number of guesses the user has made | i was the orginal varible used but we changed it to something more descriptive and instead of having to make the change to all the lines of code, right click the variable and rename it that way press enter and it will change that throughout the entire code 
guess_limit = 3  
while guess_count < guess_limit: # we need this to repeatly ask the user for a guess | We are not using the <= because then the loop would be executed 4 times | We also should store 3 in a separate variable to make our code  more readable | In Python or while loops can optionally have an else part similary to the if statements
   guess = int(input('Guess: ')) 
   guess_count += 1 
   if guess == secret_number:
      print('You Won! ')
      break # this terminates a loop
else: # this will run if the while loop completes successfully without an immediate break
   print('Sorry, you failed!')
      