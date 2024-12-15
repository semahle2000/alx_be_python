#Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

#Prompt the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

#Calculate the mothly savings
monthly_savings = monthly_income - monthly_expenses

#Assume a simple annual interest rate of 5%
annual_interest_rate = 0.05

#calculate the projected annual savings with interest
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

#Prints the results
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}")