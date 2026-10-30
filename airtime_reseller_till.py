print("=" *40)
print("AIRTIME AGENT TILL")
print("=" * 40)

share = 0.03
total_customer = 0
total_commission = 0
while True:# we use while loop when we don't know amount of clients 
    amount = str(input("enter 50/100/250/done:"))
    if amount == "50" or amount == "100" or amount == "250":
        amount = int(amount)
        cut = amount * share
        total_commission += cut
        total_customer += 1
    elif amount == "close":
        break
    else:
        print("invalid input")
        continue 
        amount = str(input("enter 50/100/250/done:"))
print(f"total clients:{total_customer}")
print (f"total commission:{total_commission}") 
        
    	
    	
