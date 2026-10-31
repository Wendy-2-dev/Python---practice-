""" investory restock Alert‼️"""
stock_list = []
count = 0
while True:
    record = (input("Add a product in:'Y' or 'N'?"))
    if record == 'N' or record == record.lower():
        break 
    elif record == 'Y' or record == record.lower():
        name = str(input("Enter name of the product:"))
        daily_sales = float(input("enter your average daily sales:"))
        current_quantity = float(input("enter current quantity of the product:"))
        order_period = int(input("enter how many days the supplier takes to bring stocks:"))
        safe_stock = float(input("Enter extra stock you order just in case:"))
        reorder_level = (daily_sales * order_period) + safe_stock
        stock_list.append([name,current_quantity,reorder_level])
    else:
        print("Please input as instructed")
        continue 
print("......Inventory restock Alert .....‼️")
print("{:<15}{:>15}".format("Item","Unit"))
for qyt in stock_list:
    if qyt[1] <= qyt[2]:
        unit = (2 * qyt[2]) - qyt[1]
        print("{:<15}{:>15.2f}".format(qyt[0],unit))
        count +=1
if count == 0:
    print("All products are well restocked")
else:
    print("No.of products to be restocked:",count)
















