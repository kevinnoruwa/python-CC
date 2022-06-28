# Handle the exception thrown by the code below by
# using try and except blocks.

# for i in ['a','b','c']:
#     print(i**2)
    
try:
    # attempt to run code 
    for i in ['a','b','c']:
        print(i**2)
except:
    # if their is an error this will be printed out
    print("Their is a type error")
    


# Handle the exception thrown by the code below
# by using try and except blocks. 
# Then use a finally block to print 'All Done.'

# x = 5
# y = 0
# z = x/y

try:
    x = 5
    y = 0
    z = x/y
except: 
    print("their is a zeroDivisonError")
    
finally:
    # This runs no matter what
    print("All Done")
    


# Write a function that asks for 
# an integer and prints the square of it.
# Use a while loop with a try, except, 
# else block to account for incorrect inputs.

def ask():
    while True:
        
        try:
            result = int(input("enter an integer: "))
            result = result**2
            
        except:
            print("An error occured! Please try again!")
            continue
        
        else:
            # if code under the try section runs well this code
            # will be printed
            print(f"Thank you, your number squared is: {result}")
            break

ask()


