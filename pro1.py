import time

print("Hello user!")

time.sleep(2)

print("This program can only execute four simple operations")

time.sleep(1.5)

print("1. Addition")

print("2. Subtraction")

print("3. Multiplication")

print("4. Division")

print("5. To Exit the program")

choice = float(input("Please enteryour choice from the above table: "))

if choice == 1:    
   
    a = float(input("Please enter the first number: "))
   
    b = float(input("Please enter the second number: "))
    
    print("Okay, your answer is: ") 
    
    print(a+b) 

elif choice == 2:   

    a = float(input("Please enter the first number: "))
   
    b = float(input("Please enter the second number: "))
    
    print("Okay, your answer is: ") 
    
    print(a-b)

elif choice == 3:    
    
    a = float(input("Please enter the first number: "))
   
    b = float(input("Please enter the second number: "))
    
    print("Okay, your answer is: ") 
    
    print(a*b)

elif choice == 4:
    
    a = float(input("Please enter the first number: "))
   
    b = float(input("Please enter the second number: "))
    
    print("Okay, your answer is: ") 
    
    print(a/b)

elif choice == 5:   
    
    print("Thank you for using this program")
    
    exit()

else : 
    
    print("You entered the wrong input.nNow you have to start the program again.\nAs I dont know how to properly loop this LOL!")

time.sleep(60)

print("You will automaticly exit the program in 60 secs")