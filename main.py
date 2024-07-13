# Get loan info from user
loan = int(input("Please Enter the Loan Account: "))
term = int(input("Please Enter the Loan Term: "))
rate = float(input(" Please Enter the Loan Rate: "))
down = int(input("Please Enter the Loan Down Payment: "))

# calculate loan
months = term * 12
rate_monthly = rate / 100 / 12
payment = (rate_monthly / (1-(1+ rate_monthly) ** (-months))) *(loan-down)

# Return the monthly payment
print("Your monthly payment is: " + 'GH¢' + str(round(payment,2)))
