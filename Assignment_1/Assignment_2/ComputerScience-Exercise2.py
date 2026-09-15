'''
Number=input("Enter a number:")
Number=int(Number)
Total=Number+1
Total=int(Total)
print(f"The next number is {Total}")

number1=input("Enter a number:")
number1=int(number1)
number2=input("Enter another number:")
number2=int(number2)
total=number1+number2
total=int(total)
print(f"The sum of {number1} and {number2} is {total}")

number=input("Enter a number of minutes:")
number=int(number)
Total=number*60
Total=int(Total)
print(f"{number} minutes has {Total} seconds")

base=input("Enter the lenght of the base of the triangle:")
base=float(base)
height=input("Enter the height of the triangle:")
height=float(height)
total=1/2*base*height
total=float(total)
print(f"The area of the triangle is {total}")

Team=input("Enter the name of your team:")
Wins=input("Enter the number of wins:")
Wins=int(Wins)
Draws=input("Enter the number of draws:")
Draws=int(Draws)
Losses=input("Enter the number of losses:")
Losses=int(Losses)
Total=Wins*3+Draws*1+Losses*0
print(f"The total points for {Team} so far is {Total}")


lenght=input("Enter the lenght of the rectangle:")
lenght=float(lenght)
width=input("Enter the width of the rectangle:")
width=float(width)
Total=2*lenght+2*width
Total=float(Total)
input(f"The perimeter of the rectangle is {Total}")

Inches=input("Enter the length in inches:")
Inches=float(Inches)
Total=Inches/12
Total=float(Total)
print(f"There are {Total}feet in {Inches}inches")


Ball=input("Enter the ball speed:")
Ball=float(Ball)
Club=input("Enter the club speed:")
Club=float(Club)
Total=Ball/Club
Total=float(Total)
print(f"The smash factor is {Total}")


n=input("Enter the number of sides in your polygon:")
n=int(n)
Total=(n-2)*180
Total=float(Total)
print(f"The sum of the internal angles in degrees is {Total}")


r=input("Enter the value of the radius:")
r=float(r)
Total=3.14*r*r
print(f"The area of the circle is {Total}")

G1=input("First grade:")
G1=float(G1)
G2=input("Second grade:")
G2=float(G2)
G3=input("Third grade:")
G3=float(G3)
G4=input("Fourth grade:")
G4=float(G4)
G5=input("Fifth grade:")
G5=float(G5)
Total=(G1+G2+G3+G4+G5)/5
Total=float(Total)
print(f"Your average is {Total}")

height=float(input("Whats your height in cm:"))
print(height/2.54,'is your height in inches')
print('Your height in feet is',(height/2.54)/12)

#finish


n=input("value of n:")
n=float(n)
Total=n*n
Total=float(Total)
t0tal=(n*n*n)
t0tal=float(t0tal)
print(f"n squared is {Total} and n cubed is {t0tal}")

P=input("Starting amount:")
P=float(P)
R=input("Interest rate:")
R=float(R)
T=input("Time:")
T=int(T)
total=P*R*T
total=float(total)
Total=P+total
Total=float(Total)
print(f"Total interest {total}, total balance {Total}")
'''

P=input("Starting amount:")
P=float(P)
R=input("Interest rate:")
R=float(R)
T=input("Time:")
T=int(T)
total=P*(1+R)**T
total=float(total)
Total=total-1000
Total=float(Total)
print(f"Total interest {Total}, total balance {total}")

'''
name=input("Name:")
cLass=input("Class:")
age=input("age:")
age=int(age)
print(f"{name}, {cLass}, {age}")
print(name)
print(cLass)
print(age)
'''