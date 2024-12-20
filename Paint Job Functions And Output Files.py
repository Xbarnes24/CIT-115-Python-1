#Validate function to determine a numeric value
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("The value must be positive and non-zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# 
def getGallonsOfPaint(squareFeet, feetPerGallon):
    gallons_needed = squareFeet / feetPerGallon
    return int(gallons_needed)
    if gallons_needed == int(gallons_needed)else int(gallons_needed) + 1

# Function to calculate the labor hours for the job
def getLaborHours(laborHoursPerGallon, totalGallons):
    return laborHoursPerGallon * totalGallons

# Function to calculate the labor cost for the job
def getLaborCost(laborHours, laborChargePerHour):
    return laborHours * laborChargePerHour

# Function to calculate the paint cost
def getPaintCost(totalGallons, laborHoursPerGallon):
    return totalGallons * paintPrice

# Function to get the sales tax rate for the state
def getSalesTax(state):
    state_tax_rates = {
        'CT': 0.06,
        'MA': 0.0625,
        'ME': 0.085,
        'NH': 0.0,
        'RI': 0.07,
        'VT': 0.06
    }
    return state_tax_rates.get(state.upper(), 0.0)

# Function that shows the estimated cost and prints to file
def showCostEstimate(squareFeet, paintPrice, feetPerGallon, laborHoursPerGallon, laborChargePerHour, state, customerLastName):
    totalGallons = getGallonsOfPaint(squareFeet, feetPerGallon)
    laborHours = getLaborHours(laborHoursPerGallon, totalGallons)
    laborCost = getLaborCost(laborHours, laborChargePerHour)
    paintCost = getPaintCost(totalGallons, paintPrice)
    salesTaxRate = getSalesTax(state)
    salesTax = (paintCost + laborCost) * salesTaxRate
    totalCost = paintCost + laborCost + salesTax

    # Print to the screen
    print(f"\nCost Estimate for {customerLastName}'s Paint Job:")
    print(f"Square Feet of Wall: {squareFeet}")
    print(f"Paint Price per Gallon: ${paintPrice:.2f}")
    print(f"Feet per Gallon of Paint: {feetPerGallon}")
    print(f"Labor Hours per Gallon: {laborHoursPerGallon}")
    print(f"Labor Charge per Hour: ${laborChargePerHour:.2f}")
    print(f"State: {state}")
    print(f"Gallons of Paint Needed: {totalGallons}")
    print(f"Labor Hours Required: {laborHours:.2f}")
    print(f"Labor Cost: ${laborCost:.2f}")
    print(f"Paint Cost: ${paintCost:.2f}")
    print(f"Sales Tax Rate: {salesTaxRate * 100}%")
    print(f"Sales Tax: ${salesTax:.2f}")
    print(f"Total Cost: ${totalCost:.2f}")

    fileName = f"{customerLastName}_PaintJobOutput.txt"
    with open(fileName, "w") as file:
        file.write(f"Cost Estimate for {customerLastName}'s Paint Job:\n")
        file.write(f"Square Feet of Wall: {squareFeet}\n")
        file.write(f"Paint Price per Gallon: ${paintPrice:.2f}\n")
        file.write(f"Feet per Gallon of Paint: {feetPerGallon}\n")
        file.write(f"Labor Hours per Gallon: {laborHoursPerGallon}\n")
        file.write(f"Labor Charge per Hour: ${laborChargePerHour:.2f}\n")
        file.write(f"State: {state}\n")
        file.write(f"Gallons of Paint Needed: {totalGallons}\n")
        file.write(f"Labor Hours Required: {laborHours:.2f}\n")
        file.write(f"Labor Cost: ${laborCost:.2f}\n")
        file.write(f"Paint Cost: ${paintCost:.2f}\n")
        file.write(f"Sales Tax Rate: {salesTaxRate * 100}%\n")
        file.write(f"Sales Tax: ${salesTax:.2f}\n")
        file.write(f"Total Cost: ${totalCost:.2f}\n")

    print(f"\nThe cost estimate has been written to the file: {fileName}")

#Where the program is actually ran or displayed
def main():
    squareFeet = getFloatInput("Enter wall space in square feet: ")
    paintPrice = getFloatInput("Enter paint price per gallon: ")
    feetPerGallon = getFloatInput("Input feet per gallon: ")
    laborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    laborChargePerHour = getFloatInput("Labor charge per hour: ")

 
    state = input("State job is in: ")
    customerLastName = input("Customer last name: ")

    # Show the cost estimate and write it to a file
    showCostEstimate(squareFeet, paintPrice, feetPerGallon, laborHoursPerGallon, laborChargePerHour, state, customerLastName)

# Run the program
if __name__ == "__main__":
    main()
