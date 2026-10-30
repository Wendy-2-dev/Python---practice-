print("=" * 40)
print("Daily mobile money transactions")
print("=" * 40)
print()

def fee_categories(amount):
    if amount < 1000:
        fees = 10
    elif amount < 10000:
        fees = 25
    else:
        fees = 55
    return fees
    
transaction = []
total_deposit = 0
total_withdrawal = 0
total_fees = 0

while True:
    log_money = str(input("logging a transaction?enter:'enter' or 'done':"))
    if log_money == "done":
        break
    elif log_money == "enter":
        transaction_type = str(input("enter 'deposit' or 'withdrawal':"))
        amount = float(input("enter amount: "))
        if transaction_type == 'deposit':
            total_deposit +=amount 
        elif transaction == 'withdrawal':
            total_withdrawal +=amount
        else:
            continue 
        fee = fee_categories(amount)
        total_fees +=fee
        transaction.append([transaction_type, amount,fee])
    else:
        print("Invalid input!try again!")
 
print("......FULL STATEMENT..........")
print("{:<15}{:>10}{:>10}".format("Type","Amount","Fees"))
for item in transaction:
   print("{:<15}{:>10.2f}{:>10.2f}".format(item[0],item[1],item[2]))
print("......Total summary...........")
print("{:<15}{:>10.2f}".format("total deposited",total_deposit))
print("{:<15}{:>10.2f}".format("total withdrawn",total_withdrawal))
print("{:<15}{:>10.2f}".format("total fee paid",total_fees))    