import sys #importing a few libraries that will make this a lot easier.
import math

print("Please paste in your numbers and <CTRL-Z> when finished.")
A = sys.stdin.read().strip("\n").split() #create a new list to store everything from the standard input, which has been split and stripped of all new line chars.

B=[] #standard input comes in as a list of strings, I'm going to create a new list to put floats into.

for item in A: #create a for loop to turn the strings into floats and append them to list "B"
    B.append(str(item))

#Extracting only the numbers I need from the list and converting them to floats.
s1 = float(B[1])
s2 = float(B[3])
c1 = float(B[5])
c2 = float(B[7])

#using the quadratic formula to solve for r1 and r2
a = 1
b = c1
c = -(c2)
x1 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
x2 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
r1 = -x1
r2 = -x2

#solve for p&q
q = (s2-s1*r1)/(r2-r1)
p = s1-q

#print all of the numbers we already know, plus that nasty mashup of strings and floats I have for S(n).
print("r1 = "+str(r1))
print("r2 = "+str(r2))
print("p = "+str(p))
print("q = "+str(q))
print("S(n) = "+"("+str(p)+")"+"("+str(r1)+")"+"^"+"(n-1)"+" + "+"("+str(q)+")"+"("+str(r2)+")"+"^"+"(n-1)")

#now just using a for loop to evaluate the equation for S(1)to S(10)
for n in range(1,11):
    Sn = (p)*(r1)**(n-1) + (q)*(r2)**(n-1)
    print("S("+str(n)+") = "+str(Sn))
