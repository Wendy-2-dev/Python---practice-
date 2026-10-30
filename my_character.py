# one string character object 
s_input = str(input())
if "a" <= s_input.lower() <= "t" or "A" <= s_input.upper() <= "T":
    print(True)
else:
    print(False)
# modifying immutable string ,here we are replacing the 1st character of the string with -*-
x = "string"
x = "*" + x[1:]
print(x)
greeting = "Hello my fellow classmates"
print(greeting[0:6])
greeting = "Hi" + greeting[5:]
print(greeting)
string_variable = "great"
indices = [0,1]
string_variable = string_variable[2:]
print(string_variable)
        