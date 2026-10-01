'''
L=input("Pick a letter:")

if (L=="a") or (L=="e") or (L=="i") or (L=="o") or (L=="u"):
    print("It's a vowel")
    
else:
    print("It's a consonant")

a=input("Enter an angle:")
a=float(a)
b=input("Enter another angle:")
b=float(b)
c=input("Enter a third angle:")
c=float(c)

if (a+b+c==180) and (a,b,c>0):
    print("It's a valid triangle")

else:
    print("It's not a triangle")


y=input("Enter a year:")
y=float(y)
 
 
if (y%4!=0):
    print("it's not a leap year")
 
elif (y%4==0) and (y%100!=0):
    print("It's a leap year")

elif (y%4==0) and (y%100==0) and (y%400==0):
    print("It's a leap year")
    
else:
    print("It's not a leap year")
    
'''
Year=input("Enter a year:")
Year=float(Year)

if Year>=0:
    Month=input("Enter a month(number)")
    Month=int(Month)

if (Month==1) or (Month==3) or (Month==5) or (Month==7) or (Month==8) or (Month==10) or (Month==12):
    print("This month has 31 days")
    
elif (Month==4) or (Month==6) or (Month==9) or (Month==11):
    print("This month has 30 days")

elif Month==2:
        
        if (Year%4!=0):
            print("This month has 28 days")
 
        elif (Year%4==0) and (Year%100!=0):
            print("This month has 29 days")

        elif (Year%4==0) and (Year%100==0) and (Year%400==0):
            print("This month has 29 days")
    
        else:
            print("This month has 28 days")
    
    