'''
n=input("Enter Grade:")
n=float(n)

if (n<=100) and (n>=90):
    print("Grade:A")
    
if(n<=90) and (n>=80):
    print("Grade:B")
    
if(n<=80) and (n>=60):
    print("Grade:C")
    
if(n<=60):
    print("GradeD")

N=input("Enter cost:")
N=float(N)

if N>10000:
    print("Tax:",N*0.15)
    
if (N<=10000) and (N>=5000):
    print("Tax:",N*0.10)
    
if (N<=5000):
    print("Tax:",N*0.05)

N=input("Enter number:")
N=float(N)

if (N>0) or (N%2==0):
    print("true")
else:
    print("false")
'''
color=input("Enter Red:")

if (color=="Red") or (color=="rEd") or (color=="reD"):
    print("Thats a great choice")
else:
    print("I do not understand")