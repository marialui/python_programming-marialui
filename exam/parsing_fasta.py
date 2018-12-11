# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file)
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght
# Use separate functions for the input and the output

f=open('sprot_prot.fasta','r')
F=f.readlines()
s=''

for i in F:
   s=s+i
entries=s.split('>')
entries=entries[1::]
for entry in entries:
    i=entries.find('\n')
print(entries)

