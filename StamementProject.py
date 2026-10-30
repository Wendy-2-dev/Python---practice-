print("1. 8 * 2 + 18 ** 3\n" + "2. 60 / 4 > 56 and 16 == 2**3\n" + "3. 34 * 4 + 5 / 6 - 12\n" + "4. 3 - 5 == 2 and 72 /2 -10 < 12\n" + "5. 196 /14 + 46 // 3")
choice = int(input("Choose(1-5):"))
if choice == 1:
    print("\nExpression: 8 * 2 + 18 ** 3")
    print("i) start with exponentiation (18 ** 3)\nii)go to multiplication (8 * 2)\niii) add i.e (8 * 2) + (18 ** 3)")
    result = (8 * 2) + (18 ** 3)
    print(result)
elif choice == 2:
    print("\nExpression: 60 / 4 > 56 and 16 == 2 ** 3")
    print("1.solve exponentiation part i.e 2 ** 3 , then division part i.e 60 / 4,then compare the division part with 56  , check if 16 is equal to the exponentiation result, if both sides are true then the result is true\n")
    result = ((60 / 4 ) > 56) and( 16 ==( 2**3))
    print(result)
elif choice == 3:
    print("\nExpression: 34 * 4 + 5 / 6 - 12")
    print("start with multiplication,then division, then addition ,then subtraction\n")
    result = (34 * 4) + (5 / 6) - 12
    print(result)
elif choice == 4:
    print("\nExpression: 3 - 5 == 2 and 72 / 2 - 10 < 12")
    print("start with division, subtraction, subtraction,less than sign, the equal to sign,the check with and, if both expressions are true then the result is true\n")
    result = ((3 - 5) == 2) and (((72 / 2) - 10) < 12)
    print(result)
elif choice == 5:
    print ("\nExpression: 196 / 14 + 46 // 3")
    print("division, floor division, addition")
    result = (196 / 14) + (46 //3)
    print(result)
else:
    print("Invalid choice! choose between 1→5")
    
    
    