temp = float(input())
unit = str(input())
# change Fahrenheit to Celsius and vice versa 
if unit == "F":
    new_temp = (temp - 32) * 5/9
    print(new_temp,end= "°C")
else:
    new_temp = (temp * 9/5) + 32
    print(new_temp, end= "°F")
    