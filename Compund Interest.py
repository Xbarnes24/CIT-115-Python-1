PV = float(input("Enter the starting principal: "))
R = float(input("Enter the annual interest rate: "))
r = R / 100
t = float(input("For many times per year is the interest compounded?: "))
m = int (input("For how many years will the account earn interest?:"))
FV =PV *(1 + r/m)**(m*t)

print(f"At the end of 2 years you will have ${FV:,.2f}")

