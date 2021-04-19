#!/usr/bin/env python
# coding: utf-8
	•	Write a Python Program to Find the Factorial of a Number?
	•	Write a Python Program to Display the multiplication Table?
	•	Write a Python Program to Print the Fibonacci sequence?
	•	Write a Python Program to Check Armstrong Number?
	•	Write a Python Program to Find Armstrong Number in an Interval?
	•	Write a Python Program to Find the Sum of Natural Numbers?

# In[5]:


## Write a Python Program to Find the Factorial of a Number? 
a = int(input("Enter a number to find the factorialL:"))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# In[7]:


num=int(input('enter a number'))
f=1
for i in range(1,num+1):
  f=f*i
print ('factorial of', num, '=',f)


# In[11]:


## Write a Python Program to Display the multiplication Table?
a=int(input('enter a number'))
for i in range(1,a):
    print(a, 'x', i, '=', a*i)



# In[12]:


## Write a Python Program to Print the Fibonacci sequence?


nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[2]:


## Write a Python Program to Check Armstrong Number?


num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[5]:


# Program to check Armstrong numbers in a certain interval

lower = 1000
upper = 200000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# In[7]:


## Write a Python Program to Find the Sum of Natural Numbers?
a = int(input("Enter a number:"))
if a<0:
    print("Enter a positive Number")

else:
   sum = 0
   # use while loop to iterate until zero
   while(a> 0):
       sum += a
       a -= 1
   print("The sum is", sum)
    


# In[ ]:




