print(10**2 + 200 / 2 - 99.75)

#Answer these 3 questions without typing code. Then type code to check your answer.
#What is the value of the expression 4 * (6 + 5)
#44
# What is the value of the expression 4 * 6 + 5
# 29
# What is the value of the expression 4 + 6 * 5 
# 34
# What is the type of the result of the expression 3 + 1.5 + 4?
# float
# What would you use to find a number’s square root, as well as its square?
# ** for squared
# ** 0.5 for sqare roor
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
'hello'[1]
# reverse string using slicing
s ='hello'
print(s[ : : -1])
# Given the string hello, give two methods of producing the letter 'o' using indexing.
s = 'hello'
print(s[4])

print(s[-1])

# Build this list [0,0,0] two separate ways.

my_list = [0,0,0]
my_l =[]
my_l.append([0,0,0])
print(my_l)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)

# sort 

list4 = [5,3,4,6,1]

list4.sort()

print(list4)

#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# What is the major difference between tuples and lists?

# tuples are immutable

# how do you create a tuple?
# use (1, 5, 7)

# what is unique about a set

# items can not be repeated every item is unique 
# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print("this is the set")
print(set(list5))

# 2 > 3
False 
# 3 <= 2
False

# 3 == 2.0
False

# 3.0 == 3
True

# 4**0.5 != 2
False

# Final Question: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']

False