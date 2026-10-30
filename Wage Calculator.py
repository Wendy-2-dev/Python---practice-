print("WAGE CALCULATOR")
print("*" * 35)
""" calculate how much money you will earn in a part time job using starting working time, starting stopping time and your hourly pay rate """
starting_hrs = int(input("Enter your starting hour:"))
starting_mins = int(input("Enter your starting minutes:"))
stopping_hrs = int(input("Enter your stopping hours:"))
stopping_mins = int(input("Enter your stopping minutes:"))
hourly_rate = float(input("your hourly rate pay:"))
print()
# show calculation 
start =(starting_hrs * 60) + starting_mins
stop =(stopping_hrs * 60) + stopping_mins
hours =(stop - start)/60
payment = hours * hourly_rate
# show output 
print(f"Worked: {starting_hrs}:{starting_mins:02d} to {stopping_hrs}:{stopping_mins:02d}")
print(f"Hours: {hours:.1f}")
print(f"Payment: ${payment:.2f}")

	

