#Define 6 functions 
#Make them floats
#Print else statement for all 6 options 

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def square(x, y):
    return x**y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Root")


while True:
    
    print("Please do not break me. I am trying my best -some sad calculator")
   
    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ("1", "2", "3", "4", "5", "6"):
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
        except ValueError:
            
            print("Invalid input. Please enter a number.")
            continue

        if choice == "1":
            print(a, "+", b, "=", add(a, b ))

        elif choice == "2":
            print(a, "-", b, "=", subtract(a, b))

        elif choice == "3":
            print(a, "*", b, "=", multiply(a, b))

        elif choice == "4":
            print(a, "/", b, "=", divide(a, b))
        
        elif choice == "5":
               print(a, "**", b, "=", (a ** b))
            
        elif choice == "6":
            
                print(a, "math.sqrt", b, "=", (a, b))
        
       
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")





# def calculate_hemi(r: int):
#     return (2 * 3.14 * r)
    
# def calculate_cube(a: int):
#     return (4 * a ** 2)
    
#     while True:
    
#         calculation = input("Enter Calculation: Hemisphere/Cube")
    
#         if calculation  == "Hemisphere":
            
#             return calculate_hemi
        
#         elif():
            
#             if calculation == "Cube":
                
                
#                 return("calculate_cube")
            
    
        
#         else:
        
#             print("Okay Cool")
    
    
