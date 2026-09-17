'''
Water=input("Enter the temp of water:")
Water=float(Water)

if Water>=100:
    print("it is Gaseous")
    
elif Water<=0:
    print("it is solid")
    
else:
    print("it is liquid")

bill=input("Enter the bill:")
bill=float(bill)

if bill>=2000:
    a=bill*0.15
    total=bill+a
    print(f"(you need to pay {total})")
    
elif bill>=1500:
    b=bill*0.10
    Total=bill+b
    print(f"(you need to pay {Total})")
    
elif bill>=1000:
    c=bill*0.05
    Total3=bill+c
    print(f"(you need to pay {Total3})")
    
else:
    print(f"(you need to pay {bill})")
'''
n1=input("Enter a number:")
n1=float(n1)
n2=input("Enter another number:")
n2=float(n2)
Operator=input("Enter +,-,* or /:")


if Operator=='+':
    a=n1+n2
    print(f"({a})")

elif Operator=='-':
    b=n1-n2
    print(f"({b})")
elif Operator=='*':
    c=n1*n2
    print(f"({c})")
elif Operator=='/':
    d=n1/n2
    print(f"({d})")


'''
d=input("Enter a number:")
d=int(d)

if d==1:
    print("Sunday")
    
elif d==2:
    print("Monday")
    
elif d==3:
    print("Tuesday")
    
elif d==4:
    print("Wednesday")
    
elif d==5:
    print("Thursday")
    
elif d==6:
    print("Friday")
    
elif d==7:
    print("Saturday")
'''