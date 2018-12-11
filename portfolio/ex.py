#5.5 fasta file reading
def reading(file):
    filefasta=open(file,'r')
    fasta=filefasta.read()
    filefasta.close()
    return fasta
print(reading('her.fasta'))

l=[]
aa=[]
def reading2(file):
    filefasta=open(file,'r')
    for line in filefasta:
        if '>' not in line:
            line.strip('\n')
            l.append(line.strip('\n'))
            for i in range(len(l)):
                aa.append(list(l[i]))
    print(l)

    print(len(aa))

print(reading2('her.fasta'))