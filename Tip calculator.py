print("=" * 40)
print("TIP CALCULATOR")
print("-" * 45)
print()
bill_amount = float(input(" Enter bill amount:$"))
percentage_to_tip = int(input(" Enter percentage to tip:"))
tip_decimal = percentage_to_tip/100
number_of_people = int(input(" Enter number of people:"))
print()
tip_amount = tip_decimal * bill_amount
total_amount = tip_amount + bill_amount
tip_per_person = tip_amount/2
total_amount_per_person = total_amount/2
print()
print("Tip amount: $" , round(tip_amount,2))
print("Total amount: $" , round(total_amount,2))
print()
print()
print("Tip per person: $" , round(tip_per_person,2))
print("Total_per_person: $", round(total_amount_per_person,2))