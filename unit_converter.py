print("-" * 40)
print("UNIT CONVERTER: DISTANCE AND WEIGHT")
print("-" * 40)
print()
"""
Creating a program that converts distance between kilometers and miles, and weight between kilometers and pounds.
"""
print("1.Kilometers→Miles" + "\n" + "2.Miles→Kilometers" + "\n" + "3.Kilograms→pounds" + "\n" + "4.Pounds→Kilograms")
print()
your_unit =int(input("choose(1-4)"))
if your_unit == 1:
    km = float(input("Enter distance in kilometers:"))
    miles = km * 0.621371
    print(f"Distance in miles: {miles:.2f}mi")
elif your_unit == 2:
    miles = float(input("Enter distance in miles:"))
    km = miles * 1.60934
    print(f"Distance in kilometers: {km:.2f}km")
elif your_unit == 3:
    kg = float(input("Enter Weight in kilograms:"))
    pounds = kg * 2.20462
    print(f"Weight in pounds: {pounds:.2f}Ib")
elif your_unit == 4:
    pounds = float(input("Enter Weight in pounds:"))
    kg = pounds * 0.453592
    print(f"Weight in kg: {kg:.2f}kg")
else:
    print("the system do not recognize your unit, kindly provide a unit within the bracket(1-4) and try again!")
