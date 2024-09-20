num=int(input("pcik a integer number 1-9:" ))
doy=int(input("enter your doy:"))
num1=(num*2+5)*50
yes=num1+1774
no=num1+1773
condition=input("did you celebrate your birthday??(yes/no):")

if condition=="yes": 
    
    print("this is your age:",(yes-doy)-num*100)

else  :
    #no
    print("this is your age:",(no-doy)-num*100)
    