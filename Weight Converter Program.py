# build a program that asks the user their weight
# user enters their weight and now it prompts them to enter either that was in kilos or pounds
# user enters either k for kilo or l for pounds and it is not case sensitive 
# program will display there weight in pounds or kilos depending on their selections 


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos") # the f in the print function is a formatted function followed by the {} this is for dynamic instances 

else:
    converted = weight / 0.45 #when dividing here use // to get a integer number, we use / to get a float meaning a decimal number
    print(f"You are {converted} pounds")