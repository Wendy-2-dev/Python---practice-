# Meal order 
print('=' * 45)
print("Lunch meal option")
print ('=' * 45)
print("1:Ceaser salad\n2: Spicy chicken wrap\n3: Butternut squash soup")
print()
print('=' * 45)
print("Dinner meal options")
print('=' * 45)
print("1: Backed salmon\n2: Turkey burger\n3: Mushroom risotto")
print()
choice = str(input ("Lunch or Dinner:\n"))
meal = int(input("(1-3):"))
print()
if meal == 1:
    if choice == "Lunch":
        print(f"Your order:Ceaser salad")
    elif choice == "Dinner":
        print(f"Your order:Baked salmon")
    else:
            print("Invalid choice go back to menu!")
if meal == 2:
    if choice == "Lunch":
        print("Your order: Spicy chicken wrap")
    elif choice == "Dinner":
        print("Your order: Turkey burger ")
    else:
        print("Invalid choice go back to the menu!")
if meal == 3:
    if choice == "Lunch":
        print("Your order: Butternut squash soup")
    elif choice == "Dinner":
        print("Your order: Mushroom risotto")
    else:
        print("Invalid choice go back to the menu!")
     
        
        
        
    

