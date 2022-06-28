 
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
st = st.split()
i = 0

for w in st:
    if w[0].lower() == 's':
        print(w)
# Use range() to print all the even numbers from 0 to 10.

for i in range(0,11,2):
    print(i)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.


nl = [x for x in range(1,51) if x % 3 == 0 ]
print(nl)
# another way to do it
list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
myList = []
for mine in list:
    if mine % 3 == 0:
        myList.append(mine)
print(myList)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
st = st.split()
word = []
for x in st:
    if len(x) % 2 == 0:
        word.append('EVEN')
    else:
        word.append(x)
print(word)
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

intergers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

my_l = []

for n in intergers:
    if n % 3 == 0 and n % 5 == 0:
           my_l.append('FizzBuzz')
    elif n % 3 == 0:
        my_l.append('Fizz')
    elif n % 5 == 0:
         my_l.append('Buzz')  
    else:
        my_l.append(n)
print(my_l)




# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
st = st.split()

myl = []

i = 0

while i < len(st):
    myl.append(st[i][0])
    i = i + 1

print(myl)
# another way 
nl = [x[0] for x in st]
print(nl)