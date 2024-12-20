# Creating a function and data validating.
def getFloatInput(prompt):
    while True:
        try:
            userInput = input(prompt)           
            value = float(userInput)
            if value <= 0:
                print("The value must be positive and non-zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Creating a function to get the median of the list. Using statistics function would be much easier but I get it. JK
def getMedian(entries):
    entries.sort()
    count = len(entries)
    
    # Median for odd numbers
    if count % 2 != 0:
        oddNum = count // 2
        return float(entries[oddNum])
    
    # Median for even numbers
    else:
        evenNum1 = count // 2 - 1
        evenNum2 = count // 2
        return float((entries[evenNum1] + entries[evenNum2]) / 2)

# Creating the main function and sales list.
def main():
    salesValues = []

    while True:
        salesPrice = getFloatInput("Enter property sales value: ")
        salesValues.append(salesPrice)

        while True:
            userPrompt = input("Enter another value Y or N: ").strip().lower()
            if userPrompt in ['y', 'n']:
                break
            else:
                print("Please enter Y or N.")
        
        if userPrompt == 'n':
            break

    salesValues.sort()

    # Displays each property value depending on how many values are input
    print("\nSorted Sales Values:")
    for value in salesValues:
        print(f"${value:,.2f}")
    
    minimum = min(salesValues)
    maximum = max(salesValues)
    total = sum(salesValues)
    average = total / len(salesValues)
    median = getMedian(salesValues)
    commission = total * 0.03

    print(f"\nMinimum : ${minimum:,.2f}")
    print(f"Maximum : ${maximum:,.2f}")
    print(f"Total : ${total:,.2f}")
    print(f"Average : ${average:,.2f}")
    print(f"Median : ${median:,.2f}")
    print(f"Commission : ${commission:,.2f}")

main()
