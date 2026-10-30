# addition function 
def add_three(input_var):
    output_var = input_var + 3
    print(output_var)
input_var = int(input())
add_three(input_var)
# Cinema concessions stand 
def concessions():
    print("Food/drink options:")
    print("popcorn🍿: $8-10")
    print("candy🍬🍭: $3-5")
    print("soft drink🍷🍻: $3-7")
concessions()
# terms and conditions using control flow 
def accepted():
    print("Thank you for accepting")
def rejected():
    print("You have rejected the terms.Thank you.")
def terms():
    print("Do you accept the terms and conditions?")
    response = str(input())
    if response == "Y":
        accepted()
    elif response == "N":
        rejected()
    else:
        print("Invalid input")
    