x = 7.0
print(x)
pi = 3.14
if x % 2 == 0:
    print('even')
else:
    print('odd')
a = (x + pi) / 2
print('the average is: %f' % (a))
print('the distances from the avarage are')
print(a - x, a - pi)
z = x * 2 - 1
m = a - x
n = a - pi
b = (m + n) / 2
print('the average of the distances is: %f' % (b))
a = (z + pi) / 2
print('the second avarage with the third variable is %f' % (a))
print('the new distances from the avarage are')
print(a - z, a - pi)
m = a - z
n = a - pi
b = (m + n) / 2
print('the new average of the distances is: %f' % (b))
x1 = 3
y2 = 6
x2 = 9
y1 = 12
from math import sqrt

ed = sqrt((x1 - x2) ** 2 + (y1 + y2) ** 2)
print('the euclidean distance is %f' % ed)

from math import log2

px = 0.15
ic = -log2(px)
print('the informantion content of px is %f' % (ic))

alessio= 'fire and ice'

print(alessio[3])
print(alessio[4])
print(alessio[9])
print(alessio[len (alessio)-1])
print(alessio[len (alessio)-2])
odd=""
for i in range (len(alessio)-1):
    if i %2 ==0:
        odd= odd + alessio[i]
print ('the odd character are: '+ odd)
even=""
for i in range (len(alessio)-1):
    if i %2 != 0:
        even= even+ alessio[i]
print ('the even character are: '+ even)
for i in range (int(len(alessio)/2)):
    print(alessio[i])
print(alessio[::-1])
i='i'
e='e'
icount=0
ecount=0
if i in alessio:
    icount= icount +1
if e in alessio:
    ecount= ecount+1
print (icount)
print(ecount)
if 'and' in alessio:
    print (alessio.replace('and','&'))
if 'fire' in alessio:
    print("there's fire in alessio")
if 're and' in alessio:
    print("there's a re and in alessio")
else :
    print ("there is not re and in alessio")
if 're &' in alessio:
    print("there is re & in alessio")
else:
    print('there is no re & in alessio')
print('the first e is in position: %d '%alessio.find('e'))
print('the last e in alessio is in position : %d'%alessio.find('e',len(alessio)-1,(0)))
cavolo='234 4329 7654 892'
for i in range (len(cavolo)-1):
    if cavolo[i] != " ":
        print ("%d" %(int(cavolo[i]) +3))
    else :
        print(' ')
#ricorda che per convertire un carattere di una stringa in integer : int(str[n])

def increase(n):
    """this function increase the number of one"""
    print(n + 1)
def add(n,m):
    """this function performs the sum of two numbers"""
    print(n+m)
def add3(n,m,l):
    """this function performs the sum of three numbers"""
    print(n+m+l)
def add5(n,m,l,i,h):
    print(n+m+l+h+i)
def prof(said,n):
    print(said*n)
print(prof(' i have data ',4))
#def proff(said,n):
    #print([said]*n)
#print (proff('i have data',4))
def proff(said, separator,n):
    print((said + separator )*n)
print (proff ('i have data',',',4))

list1=[4,8,-9,'the']
list2=['silentforce', 4.67,9]
mergedlist= list1+ list2
print(mergedlist)
if set(list1).intersection(set(mergedlist)) !=[]:
    print('there is list1 in mergedlist')
else :
    print('there is not list1 in mergedlist')
if set(list2).intersection(set(mergedlist))!= []:
    print('there is list2 in mergedlist')
else:
    print('there is not list2 in meged list')
list3=['peppe',9,'maria',4,2]
if set(list3).intersection(mergedlist) == list3:
    print('list3 is contained in mergedlist')
if set(list3).intersection(mergedlist) != []:
    print('there are some elements of list3 in merged list')
else:
    print('there are no element of list3 in mergedlist')
print(set(list3).intersection(mergedlist))

string='23|64|354|-123'
numbers=(string.split('|'))
for i in range (len(numbers)):
        print('%d' % int(numbers[i]))

for i in range (len(numbers)):
    if int(numbers[i]) >0:
        print(' %d'%(int(numbers[i])))


stringa="-1-987-6823-823-8261"
for i in range(0,len(string)+1):
   if stringa[i]!='-' and stringa[i+1]!='-':
        print(stringa[i+1])



list4=[3.14,6.333,98.12,23.1]
print(str(list4).strip('[]'))
#questo è il comando utilizzato per convertire liste in stringhe

def addlist(lista,listb):
    for n in range (len(lista)):
        if len(lista)== len(listb):
            print(lista[n]+listb[n])
listabella=[3,4,2]
listabrutta=[7,6,8]
print(addlist(listabella,listabrutta))

list6=[3,4,5,6,7,8,9,10,11,12]
for n in range (len(list6)):
    if list6[n]% 2!= 0:
        print (list6[n])
for n in range (len(list6)):
    if list6[n]% 5 ==0:
        print(list6[n])

newlist= list(range(8,24))
print(newlist)

listanuova=[5,2,7,8,1,-3]
print(listanuova[0], listanuova[2])
for i in range(len(listanuova)):
    print(((listanuova[i]*2)-2)/3)

print(sum (listanuova))

print(min(listanuova))
print(max(listanuova))
print(sum(listanuova)/len(listanuova))
frutta=' avocado '
strumento=' radar '
print(frutta[::-1] + strumento[::-1]) #in questo modo la stringa viene printata al contrario
print(frutta[:len(frutta)//2])
print(strumento[len(strumento)//2:])



#dna1=input('enter the first string: ')
#dna2=input('enter the second string: ')
dna1='act'
dna2='tga'

def complement(dna1,dna2):
    str=""
    for i in range(len(dna1)):
        if(dna1[i]=='g' and dna2[i]=='c') or (dna1[i]=='c' and dna2[i]=='g') or (dna1[i]=='a' and dna2[i]=='t') or (dna1[i]=='t' and dna2[i]=='a'):
            str=str+'1'
        else:
            str=str+'0'
            break
    if '0' not in str:
        print('yes they are complement')
    else:
        print('no, they are not complement')
    return

#esercizi in classe .

#calcola la distanza tra due punti
print(complement(dna1,dna2))
import math
def distance(p1,p2):
    x1,y1= p1
    x2,y2= p2
    distance= sqrt(((x2-x1)**2+ (y2-y1)**2))
    return (distance)
punto1= (0,5)
punto2= (33,4)
print('the distance is %f' %distance(punto1,punto2))

#calcola le soluzioni di un'equazione
def solvingeq(a,b,c):
    from math import sqrt
    if (b**2 - (a*c)*4) >= 0:
        x1= -b + (sqrt(b**2 - (a*c)*4))/2*(a)
        x2= -b - (sqrt(b**2 - (a*c)*4))/2*(a)
        return x1,x2
    else:
        print('there are no values in the real domain')

soluzioni=solvingeq(2,4,2)
print('the solution of the equation are %d' %(soluzioni[0]))

#scalar by point
def scalarproduct(a,punto1):
    x1,y1=punto1
    scalar= (a*x1, a*y1)
    return scalar
p1=(4,5)
scalarforpoint= scalarproduct(3, p1)
print('the scalar product result : ( %d , %d)' %(scalarforpoint[0],scalarforpoint[1]))

#distance
def distance(a,b):
    from math import sqrt
    x1,y1,z1=a
    x2,y2,z2=b
    distanceab = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return distanceab
punto1=3,5,6
punto2=7,3,4
print('the distance between punto1 and punto2 is: %f' %distance(punto1,punto2,))

#bernestein basis
import math
from math import factorial
def bernstein_basis_polynomial(i,n,t):
    b= (factorial(n)/factorial(i))/factorial(n-i)
    bin= b *(pow (1-t,n-i))*pow(t,i)
    return bin
print('the bernstein basis polynomial is : %f' %bernstein_basis_polynomial(2,3,4))


def even_odd(x):
    if x %2 ==0:
        print('it is even')
    else:
        print ('it is odd')
print(even_odd(5))

#esercizi in classe: crea un dizionario per cui ogni lettera della sequenza corrisponde al numero di volte in cui essa è presente nella sequenza
s='acgcgtaa'
d={}
for i in s:
    d[i]=s.count(i)
print(d)

#oppure in modo più veloce :
for i in set(s):
    d[i]=s.count(i)
print(d)

#esercizio: crea un dizionario che per ogni numero ti faccia corrispondere il suo quadrato
qd={}
intervallo= range(1,11)
def quadratic(valori):
    for i in valori:
        qd[i]= i**2
    return qd

print(quadratic(intervallo))

file=open("testouniprot")
for line in file:
    if 'Mutagenesis' in line:
        print(line)
        col=line.split('\t')
        print('the position of the single point mutation are:%s' %col[3:5])

#scalar by a vector
listproduct = []
def scalar_vector(a,vector):
    for i in range(len(vector)):
        product= a * vector[i]
        listproduct.append(product)
    return (listproduct)
vector=[1,5,7,3,8]
print(scalar_vector(4,vector))


#frequency(dna)
listadna=['c','c','t','g','a','a','a','t','g','g','c']
lista = []
def frequency(dna):
    for i in dna:
        frequenze=(dna.count(i))/len(dna)
        lista.append(frequenze)
    return (lista)
print(frequency(listadna))

#frequency(dna)
d={}
for i in listadna:
    frequenze= (listadna.count(i))/len(listadna)
    d[i]=frequenze
print(d)


#frequency
#def frequenza(contenentunkown):
    #for i in contenentunkown:
        #fi= (contenentunkown.count(i)/len(contenentunkown))
        #l.append(fi)
    #return(l)
#contenuto= input('scrivi il contenuto sconosciuto:')
#print(frequenza(contenuto))

#mode

l=[]
a=[]
d={}
def mode(vettore):
    for i in vettore:
        a.append(i)
        n=(vettore.count(i))
        l.append(n)
        max(l)
    for c in range(0,len(a)):
        d={l[c]:a[c]}
        if l[c]== max(l):
            return a[c]

vector=[2,4,5,5,5,5,6]
print(mode(vector))

#average:
def avarage(x):
    somma = 0
    for i in range (len (x)):
        k=1/len(x)
        somma= somma+x[i]
    media= somma*k
    return media
vettore=[2,3,4]
print(avarage(vettore))

#factorial
l=[]
def factorial(x):
    prodotto=1
    for i in range(0,x):
        l.append(x-i)
    for n in range(len(l)):
        prodotto= prodotto*l[n]
    return prodotto
print(factorial(8))

#es 1 sample exercises
v=[]
l=[]
def times_table(n):
    for i in range(11):
        l.append(i)
        v.append(n*l[i])
        print('%d \t %d \n ' %(l[i],v[i]))

print(times_table(7))

#esercizio numero 2

def print_table(t):
    s1=t[0]
    s2=t[1]

    t=[s1,s2]
    print('%d \t %d \n\n%d \t %d' %(s1[0] , s2[0],s1[1],s2[1]))
m=[[9, 7], [8,5]]
print(print_table(m))

