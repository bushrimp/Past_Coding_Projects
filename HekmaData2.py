"""Hekma Assignment 2 - due 4/14/21"""
"""Bushra Ibrahim"""

from pdfminer.high_level import extract_text

text = extract_text("HekmaData2a.pdf")
a = text.split('\n\n')

infile = open('HekmaData2.csv','r')
var = []
for line in infile:
    lineList = line[:-1].split(',')
    V = lineList[3]
    if V != 'COLUMN_NAME':
        var.append(V)
        
infile.close()

desc = []
Var = []
B = []
C = []
for v in var:
    if v in a:
        b = a.index(v)
        B.append(b)
        Var.append(a[b])
        desc.append(a[int(b)+1])
    if v not in a: 
        C.append(v)

outfile = open('Columns.csv','w')

for i in range(0,407):
    newList = Var[i] + ',' + desc[i] + ',' + str(i)
    print(newList, file = outfile)

outfile.close()






