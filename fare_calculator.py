print("MATATU FARE CALCULATOR")
def fare_calculator(boarding,age):# How matatu charges fare
    if boarding == "short":
        fare = 50
    elif boarding == "long":
        fare = 100
    if age < 12:# under 12 year old passengers 
        fare = fare/2
    return fare

total_passengers = 0
total_fare = 0
max_seats = 14 # Matatu's maximum seats is 14
while total_passengers < max_seats:
    boarding = str(input("enter short/long/done:")) # passenger's duration travel
    if boarding =="done":
        print("I have collected available passengers")
        break
    elif boarding == "short" or boarding == "long":
        age = int(input("enter passenger's age:"))
        fare = fare_calculator(boarding,age)
    total_passengers += 1
    total_fare += fare

print("Matatu's fare data:")
print(f"Total passengers:{total_passengers} \nTotal fare: {total_fare}")
