import sys
import math

#read from stdin
print("Please paste in your numbers and <CTRL-Z> when finished.")
A = sys.stdin.read().strip("\n").split() 
B=[] 

for item in A:
    B.append(str(item))

#create the variables for the numbers we need from the imput.
s1 = float(B[1])
c = float(B[3])
gn = float(B[5])

#create the string to be printed out
print("S(n) = "+str(c)+"^(n-1) * "+str(s1)+" + sigma("+str(c)+"^(n-i) * "+str(gn)+")")

#nested loops to calculate the answers. 
for n in range(1,11):
    i = 2
    Sn = c**(n-1)*(s1)
    while i<=n: #while loop does the function of sigma. 
        Sn += c**(n-i)*(gn)
        i+=1
    print("S("+str(n)+") = "+str(Sn))
