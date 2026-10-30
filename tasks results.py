# presenting keyword score 
def keyword_score(keyword, document):
    document = document.lower()
    count = 0
    for score in keyword:
        score = score.lower()
        if score in document:
            count += 1
        percent = (count/len(keyword))*100
        return str(percent) + "%"
db = ["Wendy", "Awuor","Founder","&","CEO"]
doc = "She is Wendy Awuor"
print(keyword_score(db,doc))


#cleaning CSV file 
def delete_airbnb(all_rows):
    clean_list = []
    for row in all_rows:
        platform = row[1]
        if platform == "Airbnb.com":
            continue
        clean_list.append(row)
    return clean_list
my_data = [["John","Airbnb.com","2024-01-05"],["Leila","Booking.com","2024-04-10"],["Sara","Expedia","2024-05-01"],["Ahmed","Airbnb.com","2024-04-15"]]
print(delete_airbnb(my_data))


# foreign currency exchange 💱 calculator 
def exchange_money(budget, exchange_rate, spread):
    """budget: amount of domestic currency you're exchanging
    exchange_rate: amount of domestic currency equal to 1 unit of foreign currency
    Returns: value of the exchanged (foreign) currency"""
    exchange_rate = exchange_rate +(exchange_rate * (spread/100))
    estimated_value = budget/ exchange_rate
    return estimated_value
def bill_amount(denom,num_bills):
    """
    denom: value of a single bill (e.g. 20)
    num_bills: how many bills you have
    Returns: total value of all the bills
    """
    bill_value = denom * num_bills
    return bill_value

def exchanged_amount(exchange_money, bill_amount, budget, exchange_rate, spread, denom, num_bills):
    """
    exchange_money:how to change domestic currency to foreign currency 
    bill_amount: bill accumulated in domestic currency 
    here we are changing the bill amount to foreign currency"""
    converted = exchange_money(budget, exchange_rate, spread)
    bills = bill_amount(denom,num_bills)
    whole_bills = int(converted / denom)
    return whole_bills * denom
    
def remaining_amount(budget, useable_amount):
    """
     amount remaining after you have spent a fraction of your budget
     """
    change = budget - useable_amount
    return change 

budget = float(input("enter your budget:"))
cohort = float(input("enter your bill denom:"))
expenses_amount = int(input("enter each bill_amount:"))
commission = float(input("enter your spread:"))
currency_rate = float(input("enter the exchange_rate:"))
planned_amount = float(input("enter your useable_amount:"))
print("How forex work:",exchange_money(budget, currency_rate, commission))
print("Amount spend in domestic currency:",bill_amount(cohort, expenses_amount))
print("Bill amount in foreign currency:", exchanged_amount(exchange_money,bill_amount, budget, currency_rate, commission, cohort, expenses_amount))
print("Remain_amount:", remaining_amount(budget, planned_amount))

# 

    
    
    
    
    
    
    
            
        



    