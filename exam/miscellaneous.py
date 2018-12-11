# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
lista= list(range(21,40))
print('the list is %s' %lista)
for i in lista:
    if i %2 ==0:
        print('%d is even' %i )
for i in lista:
    if i %3==0:
        print('%d is multiple of 3' %i)
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

# Exercise 2
# Print the last two elements of L


# Exercise 3
# What's wrong with the following piece of code? Fix it and
# modify the code in order to have it work AND to have "<i> is in the list"
# printed at least once

L = ['1', '2', '3']
for i in range(10):
    if '%d' %i in L:
        print('%s is in the list' %i)
    else:
        print('%s not found' %i)

print('the last two elements of L are %s' %L[1::])

# Exercise 4
# Read the first line from the sprot_prot.fasta file
f=open('sprot_prot.fasta','r')
F=f.readline()
print(F)
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list
homo=F.split('OS=')
print(homo[1])
# Exercise 5

# Split the second element of the list of Exercise 4 using blanks as separators
blankssplit=homo[1].split(' ')

# concatenate the first and the second elements and print the resulting string
print('%s %s'%(blankssplit[0],blankssplit[1]))

# Exercise 6
# reverse the string 'asor rosa'
string='asor rosa'
print('the reverse of the string is the string itself : %s ' %string[::-1])

# Exercise 7
# Sort the following list:
L = [1, 7, 3, 9]
L.sort()
print('the sorted list is %s' %L)

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
newlist=[]
for i in range(len(L)):
    L.sort()
    newlist.append(L[i])
print('newlist is the sorted list: %s' %newlist)


# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
f=open('table','w')
F=f.write('2 \t 4 \n3 \t 6')
f.close()
