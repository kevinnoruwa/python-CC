# Write a function that computes the volume of a
# sphere given its radius.
# 4/3(πr^3)

import math
def vol(rad):
    
    result = (4/3) * (math.pi) * (rad**3)
    print(result)
    
vol(2)
# Write a function that checks whether 
# a number is in a given range 
# (inclusive of high and low)

def ran_check(num, low,high):
    if (num >= low and  num <= high):
        print(f"{num} is in the range bewtween {low} and {high}")
    else:
        print(f"{num} not in range")
        
        
ran_check(5,2,7)


def ran_bool(num, low, high):
    if (num >= low and  num <= high):
        print("True")
        return True
      
      
    else:
          print("False")
          return False


ran_bool(3,1,10)


# Write a Python function that accepts a string and 
# calculates the number of 
# upper case letters and lower case letters.

def up_low(s):
    total_uppercase = 0;
    total_lowercase = 0
    
    i = 0
    while i < len(s):
        if(s[i].isupper()):
            total_uppercase += 1 
            i += 1
        elif(s[i].islower()): 
           
             total_lowercase += 1
             i += 1
        else:
            i += 1
                
           

    print(f"number of upper case characters: {total_uppercase}")
    print(f"number of lower case characters: {total_lowercase}")
    

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# Write a Python function that takes a list and returns 
# a new list with unique elements of the first list.


def unique_list(lst):
    
    new_list = []
    
    for i in range(0,len(lst)):
        
        if(lst[i] not in new_list):
            new_list.append(lst[i])
        else:
            pass
    print(new_list)
        
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
        
    
 
 
 
 
# Write a Python function to multiply all the numbers in a list.    

def multiply(num):
    num_total = 1
    for n in num:
        num_total *= n
        
    print(num_total)

 

multiply([1,2,3,-4]) 


def palindrome(s):
    
    full_string = s.replace(' ', '')
    
    rev = full_string[::-1]
    reg = full_string
    
    if(rev == reg):
        print("True")
        return True
    else:
        print("False")
        return False
   
   
     


palindrome('nurses run') 
    
            

# Write a Python function to check whether a 
# string is pangram or not. (Assume the string passed 
# in does not have any punctuation)
# Pangrams are words or sentences containing
# every letter of the alphabet at least once.


def ispangram(str1, a):
   alphaset = set(a)
   str1 = str1.replace(' ', '')
   str1 = str1.lower()
   
   str1 = set(str1)
   print(str1 == alphaset)
   return str1 == alphaset
   
    



ispangram("The quick brown fox jumps over the lazy dog", ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])