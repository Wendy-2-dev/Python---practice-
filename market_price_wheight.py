print("=" * 40)
print("MARKET PRICE COMPARISON TOOL")
print("=" * 40)
pack_list = []
value_list = []
while True:
    log_packs = str(input('enter "yes" or "no":'))
    if log_packs == "no":
        break
    elif log_packs == "yes":
        size = float(input("enter size a s a fraction:"))
        price = float(input("enter price:"))
        pack_list.append([size,price])
    else:
        continue
for item in pack_list:
        unit_price = item[1]/item[0]
        value_list.append([unit_price,item[0]])
value_list.sort()
if len(pack_list) == 0:
    print("No item logged!")
else:
    advantage_price = abs(value_list[0][0] - value_list[-1][0])
    print("{:<15}{:>15}".format("Size in kg","Price per kg"))
    for size in value_list:
        print("{:<15}{:>15.2f}".format(size[-1], size[0]))
    print("... result & recommendation..")
    print(f"Best choice is {value_list[0][1]}kg by ksh.{advantage_price:.2f} per kg cheaper compared to {value_list[-1][1]}kg")




       
        
