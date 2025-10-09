import re
password=(input("enter the password"))
if len(password)<=8:
    if(r"^[A-Z]$",password):
        print("password accepted")
    else:
        print("password invalid")

        if(r"^[a-z]$",password):
            print("password accepted")
        else:
            print("password invalid")
            

            if(r"^[0-9]$",password):
              print("password accepted")
            else:
                print("password invalid")
    
else:
    print("password invalid")
