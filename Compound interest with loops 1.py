
# Making a function to check if the value will be positive.
def positive_number(prompt):
    while True:
        try:
            f_Value = float(input(prompt))
            if f_Value <= 0:
                print("The number must be positive.")
            else:
                return f_Value
        except ValueError:
            print("Please enter a number.")

def non_negative_number(prompt):
    while True:
        try:
            f_value = float(input(prompt))
            if f_value < 0:
                print("The value cannot be negative. Please try again.")
            else:
                return f_value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#Asking the user for input.
f_deposit = positive_number("What is the original deposit: ")
f_interest_rate_percentage = positive_number("Enter the Interest Rate Percentage: ")
f_months = positive_number("Enter the Number of Months: ")
f_goal = non_negative_number("Enter the Goal amount: ")

# Convrting the interest rate to a decimal.
f_interest_rate_decimal = f_interest_rate_percentage / 100
f_monthly_interest_rate = f_interest_rate_decimal / 12

#Couldn't figure out how to use a different loop.
print("\nCompounding the interest for the specified number of months:")
f_balance = f_deposit
for i in range(1, int(f_months) + 1):
    f_monthly_interest = f_balance * f_monthly_interest_rate
    f_balance += f_monthly_interest
    print(f"Month: {i} ${f_balance:,.2f}")


i_months_goal = 0
f_balance = f_deposit

# The amount of interest untl we meet our goal.
while f_balance < f_goal:
    f_monthly_interest = f_balance * f_monthly_interest_rate
    f_balance += f_monthly_interest
    i_months_goal += 1
# The number of months it will take to reach the goal.
print(f"\nIt will take: {i_months_goal:,} months to reach the goal of ${f_goal:,.2f}.")

