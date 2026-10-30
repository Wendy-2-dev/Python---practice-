def verify_user(username):
    while True:
        if len(username) < 5:
            print("username must be at least 5 characters")
        elif " " in username:
            print("Must not contain any space")
        elif username[0].lower() == username[0]. upper():
            print("Must start with a letter not a number or a symbol")
        else:
            break
        username = str(input("enter username:"))
    return username 
     
username = str(input("enter username:"))
phone_num = str(input("enter your phone number:"))
password = (verify_user(username).lower()+ phone_num[-2:])
print(f"password is {password}")









    
        
        
