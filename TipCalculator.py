print("Welcome to Tip Calculator.")
bill=float(input("What was the total bill ? $"))
tip=int(input("What percentage tip would you like to give ? 10, 12 or 15 ? "))
people=int(input("How many people to split the bill ? "))
#tip=round((bill+(tip/100*bill))/people,2)
#if round is not used format can be used to round the numbers.
tip="{:.2f}".format((bill+(tip/100*bill))/people)
print(f"Each person should pay: ${tip}")