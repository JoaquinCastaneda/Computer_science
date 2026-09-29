'''
name=input("What's your name:")

if (name=="Huey") or (name=="Dewey") or (name=="Louie"):
    print("I think you might be one of Donald Duck's nephews")
    
elif (name=="Morty") or (name=="Ferdie"):
    print("I think you might be one of Mickey Mouse's nephews")
    
else:
    print("You're not a nephew of any character I know")

n=input("Enter an integer number:")
n=int(n)

if (n%3==0) and (n%5==0):
    print("FizzBuzz")

elif n%5==0:
    print("Buzz")
    
elif n%3==0:
    print("Fizz")

n=input("Enter a number:")
n=float(n)

if n<=0:
    print("The number is negative or zero",end=" ")
    
    if n%2==0:
        print("and even")
    
    else:
       print("and odd")
elif n>0:
    print("The number is positive",end=" ")
    
    if n%2==0:
        print("and even")
    
    else:
       print("and odd")

'''
city=input("Are you living in Athlone? (Enter Y or N) ")

if city=="Y":
    age=input("How old are you? ")
    age=float(age)

    if age>=18:
        r=input("Are you registered to vote? (Enter Y or N) ")
        
        if r=="Y":
            print("You can vote")
        
        else:
            print("You must register to vote")

    elif age<18:
        print("You must be 18 years or older to vote")
else:
    print("You must live in Athlone to vote")
    
    

