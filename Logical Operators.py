#If applicant has high income AND good credit 
    #Eligible for loan 

#We are going to use another logical operator OR 

#If applicant has high income OR good credit 
    #Eligible for loan

#If applicant has high income AND doesn't have a criminal record 
    #Eligible for loan 

#AND is a logical operator that combines two conditions

#OR is a logical operator we use if at least one of the conditions is true

#NOT is a logical operartor inverses any boolean value we give it, Basically if we give it a true value it will turn it to false 

#This is not Python specific pretty much any programming language that supports if statements supports logical operators

#has_high_income = True
has_good_credit = True
has_criminal_record = False

#if has_high_income or has_good_credit:
    #print("Eligible for loan")

#if has_high_income and has_good_credit:
    #print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan") 

