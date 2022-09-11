"""Hekma Assignment 1 - due 3/16/21"""
"""Bushra Ibrahim"""

#importing pylab and random for graphing use later
import pylab
from random import random

#opening and separating each line from .csv file, and making list of each line
infile = open("HekmaData1.csv",'r')
a = []
for line in infile:
    list1 = line[:-1].split(',')
    a.append(list1)

#collecting specific data from each line into lists
sexlist = []
entryages = []
onsetages = []
racelist = []
edulist = []
mmsegrp = []
mmslist = []
cdrfslist = []
for sublist in a:
    b = sublist[22]
    c = int(sublist[20])
    d = int(sublist[21])
    e = sublist[23]
    f = int(sublist[24])
    g = sublist[25]
    h = int(sublist[26])
    i = sublist[28]
    sexlist.append(b)
    entryages.append(c)
    onsetages.append(d)
    racelist.append(e)
    edulist.append(f)
    mmsegrp.append(g)
    mmslist.append(h)
    cdrfslist.append(i)

#counting number of male and female patients
male = 0
female = 0
for y in sexlist:
    if y == '1':
        male += 1
    if y == '0':
        female += 1

#acquiring the max and min entry ages
entryagesMin = min(entryages)
entryagesMax = max(entryages)

#counting the entry ages within each range 
range1a = 0 #45-55
range2a = 0 #56-65
range3a = 0 #66-75
range4a = 0 #76-85
range5a = 0 #86-95
for k in entryages:
    if k in range(45,56):
        range1a += 1
    if k in range(56,66):
        range2a += 1
    if k in range(66,76):
        range3a += 1
    if k in range(76,86):
        range4a += 1
    if k in range(86,96):
        range5a += 1

#acquiring the max and min onset ages
onsetagesMin = min(onsetages)
onsetagesMax = max(onsetages)

#counting the onset ages within each range 
range1b = 0 #40-50
range2b = 0 #51-60
range3b = 0 #61-70
range4b = 0 #71-80
range5b = 0 #81-90
for j in onsetages:
    if j in range(40,51):
        range1b += 1
    if j in range(51,61):
        range2b += 1
    if j in range(61,71):
        range3b += 1
    if j in range(71,81):
        range4b += 1
    if j in range(81,91):
        range5b += 1

#counting number of patients per race
race1 = 0
race2 = 0
for t in racelist:
    if t == '1':
        race1 += 1
    if t == '2':
        race2 += 1

#acquiring the max and min education
eduMin = min(edulist)
eduMax = max(edulist)

#counting education levels within each range
range1c = 0 #5-10
range2c = 0 #11-15
range3c = 0 #16-25
for s in edulist:
    if s in range(5,11):
        range1c += 1
    if s in range(11,16):
        range2c += 1
    if s in range(16,26):
        range3c += 1
        
#counting patients in each group, 0, 1, or 2
grp0a = 0
grp1a = 0
grp2a = 0
for r in mmsegrp:
    if r == '0':
        grp0a += 1
    if r == '1':
        grp1a += 1
    if r == '2':
        grp2a += 1
    
#counting patients within each mms range
range1d = 0 #0-10
range2d = 0 #11-20
range3d = 0 #21-30
for s in mmslist:
    if s in range(0,11):
        range1d += 1
    if s in range(11,21):
        range2d += 1
    if s in range(21,31):
        range3d += 1

#counting patients in each cdrfs group
grp0b = 0
grp05b = 0
grp1b = 0
grp2b = 0
grp3b = 0
grp4b = 0
grp5b = 0
grpempty = 0
for r in cdrfslist:
    if r == '0':
        grp0b += 1
    if r == '0.5':
        grp05b += 1
    if r == '1':
        grp1b += 1
    if r == '2':
        grp2b += 1
    if r == '3':
        grp3b += 1
    if r == '4':
        grp4b += 1
    if r == '5':
        grp5b += 1
    if r == '':
        grpempty +=1
        
#graphing all findings
colors = {}
Colors1 = []
Colors2 = []
Colors3 = []
Colors4 = []
Colors5 = []
Colors6 = []
Colors7 = []
Colors8 = []

count1 = [male,female]
label1 = ['Male:200','Female:310']

for x in count1:
    colors[x] = (random(),random(),random())
    rgb = colors[x]
    Colors1.append(rgb)

Sexes = pylab.arange(2)
pylab.bar(Sexes,count1,0.5,color = Colors1)
pylab.xticks(Sexes, label1)
pylab.xlabel('Sex: Count')
pylab.ylabel('Number')
pylab.title('Sex - Graph 1')
pylab.show()

count2 = [range1a,range2a,range3a,range4a,range5a]
label2 = ['(45-55): 37','(56-65): 129','(66-75): 217','(76-85): 115','(86-95): 12']

for x in count2:
    colors[x] = (random(),random(),random())
    rgb = colors[x]
    Colors2.append(rgb)

Entry = pylab.arange(5)
pylab.bar(Entry,count2,0.5,color = Colors2)
pylab.xticks(Entry, label2)
pylab.xlabel('Age Range: Count')
pylab.ylabel('Number of Patients')
pylab.title('Entry Age - Graph 2')
pylab.show()


count3 = [range1b,range2b,range3b,range4b,range5b]
label3 = ['(40-50): 25','(51-60): 97','(61-70): 217','(71-80): 150','(81-90): 21']

for x in count3:
    colors[x] = (random(),random(),random())
    rgb = colors[x]
    Colors3.append(rgb)

Onset = pylab.arange(5)
pylab.bar(Onset,count3,0.5,color = Colors3)
pylab.xticks(Onset, label3)
pylab.xlabel('Age Range: Count')
pylab.ylabel('Number of Patients')
pylab.title('Onset Age - Graph 3')
pylab.show()

count4 = [race1,race2]
label4 = ['Race 1: 498','Race 2: 12']

for x in count4:
    colors[x] = (random(),random(),random())
    rgb = colors[x]
    Colors4.append(rgb)

Race = pylab.arange(2)
pylab.bar(Race,count4,0.5,color = Colors4)
pylab.xticks(Race, label4)
pylab.xlabel('Race: Count')
pylab.ylabel('Number of Patients')
pylab.title('Race - Graph 4')
pylab.show()


count5 = [range1c, range2c, range3c]
label5 = ['5-10: 116','11-15: 303','16-25: 91']

for x in count5:
    colors[x] = (random(),random(),random())
    rgb = colors[x]
    Colors5.append(rgb)

Edu = pylab.arange(3)
pylab.bar(Edu,count5,0.5,color = Colors5)
pylab.xticks(Edu, label5)
pylab.xlabel('Education Level: Count')
pylab.ylabel('Number of Patients')
pylab.title('Education - Graph 5')
pylab.show()

count6 = [grp0a, grp1a, grp2a]
label6 = ['0: 296','1: 170','2: 44']

for x in count6:
    colors[x] = (random(),random(),random())
    rgb = colors[x]
    Colors6.append(rgb)

MMSE = pylab.arange(3)
pylab.bar(MMSE,count6,0.5,color = Colors6)
pylab.xticks(MMSE, label6)
pylab.xlabel('MMSE Group: Count')
pylab.ylabel('Number of Patients')
pylab.title('MMSEGRP - Graph 6')
pylab.show()

count7 = [range1d, range2d, range3d]
label7 = ['0-10: 61','11-20: 184','21-30: 265']

for x in count7:
    colors[x] = (random(),random(),random())
    rgb = colors[x]
    Colors7.append(rgb)

MMS = pylab.arange(3)
pylab.bar(MMS,count7,0.5,color = Colors7)
pylab.xticks(MMS, label7)
pylab.xlabel('MMS Group: Count')
pylab.ylabel('Number of Patients')
pylab.title('MMS - Graph 7')
pylab.show()


count8 = [grp0b,grp05b,grp1b,grp2b,grp3b,grp4b,grp5b]
label8 = ['0: 122','0.5: 63','1: 224','2: 83','3: 15','4: 1','5:1']

for x in count8:
    colors[x] = (random(),random(),random())
    rgb = colors[x]
    Colors8.append(rgb)

CDRFS = pylab.arange(7)
pylab.bar(CDRFS,count8,0.5,color = Colors8)
pylab.xticks(CDRFS, label8)
pylab.xlabel('CDRFS Group: Count')
pylab.ylabel('Number of Patients')
pylab.title('CDRFS - Graph 8')
pylab.show()

infile.close()

#printing information summary
print()
print('HEKMA DATA 1 - SUMMARY OUTPUT')
print('- all values are percentages -')
print('- unless otherwise specified -')
print('------------------------------')
print('1. Sex')
print('------------------------------')
print('Male = 39.22')
print('Female = 60.78')
print('------------------------------')
print('2. Entry Age')
print('------------------------------')
print('minimum age = 45 (not a percentage)')
print('maximum age = 91 (not a percentage)')
print('45-55 = 7.25')
print('56-65 = 25.29')
print('66-75 = 42.55')
print('76-85 = 22.55')
print('86-95 = 2.35')
print('------------------------------')
print('3. Onset Age')
print('------------------------------')
print('minimum age = 42')
print('maximum age = 90')
print('40-50 = 4.90')
print('51-60 = 19.02')
print('61-70 = 42.55')
print('71-80 = 29.41')
print('81-90 = 4.12')
print('------------------------------')
print('4. Race')
print('------------------------------')
print('Race 1 = 97.65')
print('Race 2 = 2.35')
print('------------------------------')
print('5. Education')
print('------------------------------')
print('minimum education = 6 (not a percentage)')
print('maximum education = 21 (not a percentage)')
print('5-10 = 22.75')
print('11-15 = 59.41')
print('16-25 = 17.84')
print('------------------------------')
print('6. MMSEGRP')
print('------------------------------')
print('0 = 58.04')
print('1 = 33.34')
print('2 = 8.63')
print('------------------------------')
print('7. MMS')
print('------------------------------')
print('minimum value = 2 (not a percentage)')
print('maximum value = 30 (not a percentage)')
print('0-10 = 11.96')
print('11-20 = 36.08')
print('21-30 = 51.96')
print('------------------------------')
print('8. CDRFS')
print('------------------------------')
print('0 = 23.92')
print('0.5 = 12.35')
print('1 = 43.92')
print('2 = 16.27')
print('3 = 2.94')
print('4 = 0.20')
print('5 = 0.20')
print('note - there was one empty cell (patient ID 377)')
print('------------------------------')


        

























