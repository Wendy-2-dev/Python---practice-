#logical operators
x = 13
print(not x < 10)
# speed limits 
car_speed = int(input("Enter car's speed:"))
freeway_limit = ((car_speed >= 45) and (car_speed <= 70))
if freeway_limit == True:
    print("Good driving")
else:
    print("follow the speed limits.")