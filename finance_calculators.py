# Step 1: Import math module
# Step 2: Display the menu to the user
# Step 3: Take user's choice as input and convert it to lowercase
# Step 4: Take investment details as input
# Step 5: Perform investment calculation
# Step 6: Display the result
# Step 7: Take bond details as input
# Step 8: Calculate monthly repayment for the bond
# Step 9: Display the result


# Step 1: Import math module
import math

# Step 2: Display the menu to the user
print("Choose either investment or bond from the menu below to proceed:")
print("investment - to calculate the amount of interest you'ill earn on your investment")
print("bond - to calculate the eamount you'll have to pay on home loan")

# Step 3: User's choice as input and convert it to lowercase
choice = input("Enter either 'investment' or 'bond': ").lower()

# Step 4: Take investment details as input
if choice == 'investment':
    amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()
    
    # Step 5: Perform investment calculation
    if interest_type == 'simple': total_amount = amount * (1 + interest_rate * years)
    elif interest_type == 'compound': total_amount = amount * math.pow((1 + interest_rate), years)

    # Step 6: Display the result
    print(f"Your total amount after {years} years will be: {total_amount:.2f}")
elif choice == 'bond':
    
    # Step 7: Take bond details as input
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    months = int(input("Enter the number of months yoyu plan to take to repay the bond: "))
    
    # Step 8: Calculate monthly repayment for the bond
    monthly_interest_rate = interest_rate / 12
    repayment = (monthly_interest_rate * present_value) / (1 -math.pow((1 + monthly_interest_rate), -months))

    #Step : Display the result
    print(f"Your monthly bond repayment will be: {repayment:.2f}")
    esle: print("Invalid input. Please choose either 'investment' or 'bond'.")
