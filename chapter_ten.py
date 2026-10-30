import math 
x = math.pow(3,3)
y = float(3**3)
print(type(x)== type(y))

print("\"To me programming is more than an important practical art.\n It is also gigantic understanding in the foundation of knowledge.\"")
print("\t.... Grace Hopper.")

word = str(input("Enter a 3 letter word:"))
shift = int(input("shifted by how many letters:"))
for i in word:
    ascii_num = ord(i)
    shift_num = ascii_num  + shift
    shift_i = chr(shift_num)
    print(shift_i,end ="")
print()

tuple_1 = (3,4,6,8)
tuple_1 = list(tuple_1)
tuple_1[0] = 2
tuple_1 = tuple(tuple_1)
print(tuple_1)

def terms():
    while True:
        choice = str(input("enter 'Y' or 'N':"))
        if choice == "Y":
            print("Thank you for accepting")
            break 
        elif choice == "N":
            print("Have a good day")
            break 
        else:
            print("Please enter 'Y' or 'N'")
            continue
print("Do you accept terms and conditions?")
terms()


def accepted():
    print ("Thank you for accepting")
def rejected():
    print("You have rejected the terms")
def terms():
    while True:
        response = str(input("enter 'Y' or 'N':"))
        if response == 'Y':
            accepted()
            break 
        elif response == 'N':
            rejected()
            break 
        else:
            print("Please enter 'Y' or 'N'")
            continue
print("Do you accept the terms and conditions?")
terms()

def print_conf():
    print("link:https://cof.link//34827169")
def book_club():
    book = "Parable of the sower by Octavia Butler"
    date = "15th October,7:30pm"
    print("This month pick:",book)
    print("When:",date)
    print_conf()
member_list = ["Sarah","Ben","Jaya"]
for member in member_list:
    print(f"Join us,{member}, for book club!")
    book_club()


















