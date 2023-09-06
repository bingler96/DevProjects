# This game does not have a graphical interface or gooey the focus is to build the engine for the game. 
# Instructions on how to build the program
# When the program starts we want it to have the cursor just sitting waiting for the user to enter the command | When they type help it should bring a menu of option for them to type
# start - to start the car | Car started . . . Ready to go! 
# stop - to stop the car | Car stopped 
# quit - to exit  
# any other commands typed out the program should show I dont understand that 

# variable to what the user enters | Then we can continue to run the loop until the user types quit
# we want to run this loop until the user types quit | We need to have something in place just in case the user types something in capital or lower case to accept any input from the user thats when the .lower or .upper
command = "" # "" Is a empty string - that has no characters
started = False
while True: 
    command = input(">").lower() # with the ,lower() here we dont need to repeat the line of code through the code, all the inputs will be received as lower. 
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True 
            print("Car started... Ready to go!" ) # needed to add this so when the user types start twice it will show a message telling them its already started
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False 
            print("Car stopped.") # same as above we need to tell the user if they stopped the car twice
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car 
quit - to quit the game""")
    elif command == "quit":
        break # If we do not include this break and the user types quit the print statement below it will display still. 
else:
    print("Sorry, I don't understand that")