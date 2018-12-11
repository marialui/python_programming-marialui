# average_function.py
# For this exercise the pseudo-code is required (in this same file)
# Write a function that calculates the average of the values of
# any vector of 10 numbers
def avarage(x):
    somma = 0
    for i in range (len (x)):
         k=1/len(x)
         somma= somma+ int(x[i])
    media= somma*k
    return media

# Each single value of the vector should be read from the keyboard
# and added to a list.

def vector_input():
    l=[]
    for i in range(10):
        value=input('the value of the vector is: ')
        l.append(value)
    return l
a=vector_input()
print(a)
print('the avarage of the vector is: %f'%(avarage(a)))

# Print the input vector and its average
# Define separate functions for the input and for calculating the average

"""pseudocode:
-take 10 number as an input
-put the input number in a list
-sum the numbers each number of the list 
-put the result of the sum in a variable
-divide the variable for 10 
-show the result





"""
