# LESSER OF TWO EVENS: Write a function that 
# returns the lesser of two given numbers if both numbers are
#even, but returns the greater if one or both numbers are odd



from operator import truediv


def lesser_of_two(num_one, num_two):
    if(num_one % 2 == 0 and num_two % 2 == 0):
        if(num_one < num_two):
            print(f"This is the lesser one {num_one}")
            return num_one
        else:
            print(f"This is the lesser one {num_two}")
            return num_two
    else:
        if(num_one > num_two):
            print(f"This is the larger one {num_one}")
            return num_one
        else:
            print(f"This is the larger one {num_two}")
            return num_two
        
            
        

lesser_of_two(2,5)

# ANIMAL CRACKERS: Write a function takes a two-word 
# string and returns True
# if both words begin with same letter
def animal_cracker(word):
    txt = word.split()
    if(txt[0][0].capitalize() == txt[1][0].capitalize()):
        print('true')
        return True
    else:
        print('false')
        return False
               
animal_cracker('Levelheaded Llama') 
animal_cracker('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of 
# the integers is 20 or if one of the integers is 20. If not, 
# return False

def makes_twenty(n1, n2):
    if(n1 == 20 or n2 == 20 or n1 + n2 == 20):
        print('True')
        return True
    else:
        print('False')
        return False

makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)



# OLD MACDONALD: Write a function that
# capitalizes the first and fourth letters of a name
def old_macdonald(str):
   test = []
   i = 0
   i2 = 4
   
   str1 = str[0].capitalize()
   
   str2 = str[3].capitalize()
   
   test.append(str1)
   
   while i < 2:
       
       test.append(str[i+ 1])
       i = i + 1
       
   test.append(str2)
   
   while i2 < len(str):
       
       test.append(str[i2])
       i2 = i2 + 1
   
   full_w = ''.join(test)
   print(full_w)
           
   
old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a 
# sentence with the words reversed
def master_yoda(txt):
    t = []
    
    s = txt.split()
    i = len(s)
    while i > 0:
       t.append(s[i - 1])
        
        
       i = i - 1
    print(' '.join(t)) 
   
    
    
    
master_yoda('I am home')
master_yoda('We are ready')


# ALMOST THERE: Given an integer n, return True if n
# is within 10 of either 100 or 200


def almost_there(n):
    
    if(abs(100 - n) <= 10 or abs(200 - n) <= 10):
        return True 
    else:
        return False
        
    


# FIND 33:
# Given a list of ints, return True if the 
# array contains a 3 next to a 3 somewhere.



def has_33(nums):
   
    
   for i in range(0, len(nums) -1):
       if (nums[i] == 3 and nums[i+1] == 3):
           return True
       else: 
        return False
        


# has_33([1, 3, 3])           
           

# has_33([1, 3, 1, 3])
            
        
# has_33([3, 1, 3])     

# PAPER DOLL: Given a string, return a string 
# where for every character
# in the original there are three characters

def papper_doll(txt):
    test = []
    
    for x in txt:
        for x2 in range(3):
            test.append(x[0])     
      
        
    full_w = ''.join(test)
    print(full_w)
      

papper_doll('hello')
papper_doll('Mississippi')

# BLACKJACK: Given three integers between 1 and 11, 
# if their sum is less than or equal to 21, return their
# sum. If their sum exceeds 21 and there's an eleven, reduce
# the total sum by 10. Finally, if the sum
# (even after adjustment) exceeds 21, return 'BUST
def blackjack(a, b, c):
    sum = a + b + c
    if(a != 11 and b != 11 and c != 11):
        if(sum <= 21):
            print(f"This is returned {sum}")
            return sum
        else:
            print('Bust')
            return 'BUST'
        
    if( a == 11 or b == 11 or c == 11 and sum > 21):
        sum = sum - 10
        print(f"This is returned {sum}")
        if(sum > 21):
            print('Bust')
            return 'BUST'
        return sum            
   
blackjack(5,6,7) 

blackjack(9,9,9)

blackjack(9,9,11)        
 
 
 
#HELP!   
# SUMMER OF '69: Return the sum of t
# he numbers in the array, except ignore 
# sections of numbers starting with a 6 and 
# extending to the next 9 (every 6 will be
# followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    
    total = 0
    add=  True
    
    
    for num in arr:
        while add:
            if (num != 6):   
                total += num
                break
            else:
                add = False
            while not add:
                if num != 9:
                    break
                else:
                    add = True
                    break
    return total








# HELP!!
# SPY GAME: Write a function that takes in a list
# of integers and returns True if it contains 007 in order

def spy_game(nums):
    
    
    code = [0,0,7,'x']
    
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
        
    return len(code) == 1
    


spy_game([1,2,4,0,0,7,5])
    
# COUNT PRIMES: Write a function that returns the number of prime numbers 
# that exist up to and including a given number


def count_primes(num):
    # check for 0 or 1 input
    if(num < 2):
        return 0
    
    
    # 2 or greater
    
    primes = [2]
    # counter going up to the input num
    x = 3
    

    #  x is going through every number up to input num 
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
            
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
            
    




