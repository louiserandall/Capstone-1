import math

# Create an investment calculator and home loan replacement calculator

# Define investment or bond to user


print ("Investment, to calculate the amount of interest you will earn on your investment")
print ("Bond, to calculate the amount you will have to pay on a home loan")


# Ask user to input their choice between investment or bond

invest_or_bond = str(input("Please enter either, investment or bond from the menu above to proceed: "))

# If investment is selected as true ask user to answer further questions

if invest_or_bond == "investment":
        if True: 
            deposit_1 = float(input("Please enter the amount of money you are depositing: ")) # Amount of money

            percet_1 = float(input("Please enter the interest rate as a percentage: ")) # Interest rate

            years_1 = float(input("Please enter the number of years you plan on investing: ")) # Number of years investing

            interest_1 = str(input("Please enter the type of interest between simple or compound interest: ")) # Type of interest simple or compound

# Calculate simple interest using this formula A =P *(1 + r*t)

        if interest_1 == "simple":
            "simple" == interest_1
            simple_interest = deposit_1 *(1 + percet_1/100 * years_1)
            total = interest_1
            print (f"Your simple interest earned over {years_1} years will be £ {simple_interest:.2f}".format()) # print output of calculation

# Calculate compound interest using this formula A = P * math.pow((1+r),t)

        elif interest_1 == "compound":
            "compond" == interest_1
            compound_interest = deposit_1 *math.pow((1 + percet_1/100), years_1)
            total = compound_interest
            print (f" Your compound interest earned over {years_1} years will be £: {compound_interest:.2f}".format()) # print output of calculation 

elif invest_or_bond == "bond":
        if True:
            value_1 = float(input("Please enter the value of your house: ")) # Value of house

            interest_2 = float(input("Please enter the interest rate as a percentage: ")) # Interest rate

            months_1 = float(input("Please enter the number of months you plan to take to repay the bond: ")) # Number of months

# calculate repayment = (i * P)/(1 - (1 + i)**(-n))
            repayment_1 = (interest_2/100/12 * value_1) / (1 - ( 1 + interest_2/100/12) ** (- months_1))

            print (f"Your monthly repayment will be £: {repayment_1:.2f}".format()) # print output of calculation 
else:
    print("This is an invalid input, please try again and resubmit either investment or bond to proceed: ")            
