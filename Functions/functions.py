import sys
Function = True
OnetoOne = True
Onto = True

#Gather input from stdin and get the information into a list
print("Please paste in your numbers and <CTRL-Z> when finished.")
A = sys.stdin.read().splitlines()
Input = []
for item in A: 
    Input.append(str(item))

#split the lines at the spaces to retreive the individual values
Line1=((Input[0]).split(" "))
Line2=((Input[1]).split(" "))
Line3 = ((Input[2]).split(" "))

#create lists and fill them with the values from lines 1, 2, and 3.
DomainList=[]
CodomainList=[]
RelationList=[]
for item in Line1:
    DomainList.append(item)
for item in Line2:
    CodomainList.append(item)
for item in Line3:
    RelationList.append(item)

n = len(RelationList)/2

#Separate into parallel lists a[] and b[]
i=0
a=[]
b=[]
while i<n:
    a.append(RelationList[i*2])
    b.append(RelationList[i*2+1])
    i+=1
pairs=[]
i=0
for x in range(0,int(n)):
    pairs.append("("+a[i]+","+b[i]+")")
    i+=1


#Check if it's a Function?
#The number of items in the Domain needs to be the same as the number of ordered pairs. There's also a failsafe if they are the same count, but the values are different.
if len(DomainList) == (n):
    domaincount = 0
    i=0
    for d in DomainList:
        val = a[i]
        domaincount += a.count(val)
        i = i+1
    domaincount1 = domaincount/(len(a))
    if domaincount1 != 1:
        Function = False
else:
    Function = False

#Check if it's Onto? A dictionary is a list that is guaranteed to have no duplicates 
sortb = list(dict.fromkeys(sorted(b)))
sortcod = list(dict.fromkeys(sorted(CodomainList)))

#if the dictionary full of y values has the same values as the dictionary full of codomain values then the function *is* onto. Otherwise, it is not. 
if sortb == sortcod:
    Onto = True
else:
    Onto = False

#if the y values from the ordered pairs don't match the dictionary of the ordered pairs then it is not 1-to-1. 
if len(b) == len(sortb):
    OnetoOne = True
else:
    OnetoOne = False

#print out all the stuff
print("Domain:","{",", ".join(DomainList),"}")
print("Codomain:","{",", ".join(CodomainList),"}")
print("Relation:","{",", ".join(pairs),"}")
if Function == True:
    print("This is a function")
    if (Onto == True):
        print("It is onto")
    else:
        print("It is *not* onto")
    if OnetoOne == True:
        print("It is 1-to-1")
    else:
        print("It is *not* 1-to-1")
    if (Onto == True) and (OnetoOne == True) :
        print("It is a bijection")
    else:
        print("It is *not* a bijection")
else:
    print("This is *not* a function")
