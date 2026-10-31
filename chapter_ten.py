def donate(name = "Anonymous", amount = 5,msg = " "):
    return"{:<10}{:^20.2f}{:>15}".format(name,amount,msg)

print("{:<10}{:^20}{:>15}".format ("Donor's name","amount donated","Donor's message"))
print(donate(amount = 1000000,msg = "All shall be well"))
print(donate("Wendy",20000,"You're are doing a great job"))
print(donate(name = "Wendy",msg = "Keeps up mobilizing"))
string_variable = "great ambience"
indices = [0,1]
print(string_variable[2:])
print(string_variable.index("h"))