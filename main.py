from login import Login,Register
while(True):
    o = input("1-login\n2-signUP\n3-exit\nenter one of this numbers : ")
    if(o=="1"):
        Login()
    elif(o=="2"):
        Register()
    else:
        break
print("thank you :) ")