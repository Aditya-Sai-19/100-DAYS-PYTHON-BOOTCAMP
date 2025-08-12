print("Welcome to the tip calculator!\nWe will help you calculate the tip and split\n")

bill_amount = float(input("What is the total bill amount?\n $"))
tip_choice = int(input("How much tip would you like to give? (in percentage)\nChoose an option from the below\n 1. 10% \n 2. 15%\n 3. 20%\n 4. Any other percentage\n"))
if tip_choice == 1:
    tip_percent = 10/100
elif tip_choice == 2:
    tip_percent = 15/100
elif tip_choice == 3:
    tip_percent = 20/100
else:
    tip_percent = float(input("Enter the amount of tip percentage you want to give: "))
    #print("\r%\n")
    tip_percent = tip_percent / 100
total_amount = bill_amount + (bill_amount * tip_percent)

persons = int(input("Among how many people do you want to split the bill?\n"))
final_amount = round(total_amount / persons ,2)
print(f"The total amount to be paid by each person is \n ${final_amount}")