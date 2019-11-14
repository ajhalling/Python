import sys

#read in lines via stdin
print("Please paste in your input and <CTRL-Z> when finished.")
A = sys.stdin.read().splitlines()
Input = []
#separate each line into a list item
for item in A: 
    Input.append(str(item))
#delete the 2nd item in the list, as it's just decorative. 
del Input[1]

#split the list items again into another list, allowing us to see each row individually.
splitrows = []
for i in Input:
    splitrows.append(i.strip("\n").split())

#specify that the first item in the list contains the variable and delete "OUT" as it's unnecessary. 
vars = splitrows[0]
vars.remove('OUT')
#delete the row containing the variables as once we've captured them we don't need it in our list anymore. 
del splitrows[0]

#set up two empty lists that we'll append answers to later, aj is for DNF and aj2 is for CNF. 
aj = []
aj2returnoftheaj = []
#calculate the number of rows 
numrows = len(splitrows)

#large for loop 
for i in range(0, numrows):
    string=""
    rows = splitrows[i]
    #DNF checks if there is a "1" at the end of a row, if there is, it checks the number of variables and then outputs either the variable or variable'
    if int(rows[-1]) == 1:
        for item in rows:
            if len(vars) == 2:
                #loop through each row checking for zeros or ones, if it's a zero the variable is not negated, the inverse is also true. 
                if int(rows[0]) == 1:
                    a = str(vars[0])
                else:
                    a = str(vars[0]+"'")
                if int(rows[1]) == 1:
                    b = str(vars[1])
                else:
                    b = str(vars[1]+"'")
                #append the variable value to the lists we created above.
                anslist = str(a)+" "+str(b)
                aj.append(anslist)
                break
            elif len(vars) == 3:
                #loop through each row checking for zeros or ones, if it's a zero the variable is not negated, the inverse is also true.
                if int(rows[0]) == 1:
                    a = str(vars[0])
                else:
                    a = str(vars[0]+"'")
                if int(rows[1]) == 1:
                    b = str(vars[1])
                else:
                    b = str(vars[1]+"'")
                if int(rows[2]) == 1:
                    c = str(vars[2])
                else:
                    c = str(vars[2]+"'")
                #append the variable value to the lists we created above.
                anslist = str(a)+" "+str(b)+" "+str(c)
                aj.append(anslist)
                break
            elif len(vars) == 4:
                #loop through each row checking for zeros or ones, if it's a zero the variable is not negated, the inverse is also true.
                if int(rows[0]) == 1:
                    a = str(vars[0])
                else:
                    a = str(vars[0]+"'")
                if int(rows[1]) == 1:
                    b = str(vars[1])
                else:
                    b = str(vars[1]+"'")
                if int(rows[2]) == 1:
                    c = str(vars[2])
                else:
                    c = str(vars[2]+"'")
                if int(rows[3]) == 1:
                    d = str(vars[3])
                else:
                    d = str(vars[3]+"'")
                #append the variable value to the lists we created above.
                anslist = str(a)+" "+str(b)+" "+str(c)+" "+str(d)
                aj.append(anslist)
                break
            else:
                print("I see you found the shortcoming of my program, please leave.")
                exit()
    #CNF checks if there is a zero at the end of the row, if there is, it checks for the number of variables and operates accordingly. 
    if int(rows[-1]) == 0:
        for item in rows:
            if len(vars) == 2:
                #loop through each row checking for zeros or ones, if it's a zero the variable is not negated, the inverse is also true. 
                if int(rows[0]) == 0:
                    a = str(vars[0])
                else:
                    a = str(vars[0]+"'")
                if int(rows[1]) == 0:
                    b = str(vars[1])
                else:
                    b = str(vars[1]+"'")
                #append the variable value to the lists we created above.
                anslist =  "("+str(a)+" "+str(b)+")"
                aj2returnoftheaj.append(anslist)
                break
            elif len(vars) == 3:
                #loop through each row checking for zeros or ones, if it's a zero the variable is not negated, the inverse is also true. 
                if int(rows[0]) == 0:
                    a = str(vars[0])
                else:
                    a = str(vars[0]+"'")
                if int(rows[1]) == 0:
                    b = str(vars[1])
                else:
                    b = str(vars[1]+"'")
                if int(rows[2]) == 0:
                    c = str(vars[2])
                else:
                    c = str(vars[2]+"'")
                #append the variable value to the lists we created above.
                anslist =  "("+str(a)+" "+str(b)+" "+str(c)+")"
                aj2returnoftheaj.append(anslist)
                break
            elif len(vars) == 4:
                #loop through each row checking for zeros or ones, if it's a zero the variable is not negated, the inverse is also true.
                if int(rows[0]) == 0:
                    a = str(vars[0])
                else:
                    a = str(vars[0]+"'")
                if int(rows[1]) == 0:
                    b = str(vars[1])
                else:
                    b = str(vars[1]+"'")
                if int(rows[2]) == 0:
                    c = str(vars[2])
                else:
                    c = str(vars[2]+"'")
                if int(rows[3]) == 0:
                    d = str(vars[3])
                else:
                    d = str(vars[3]+"'")
                #append the variable value to the lists we created above.
                anslist = "("+str(a)+" "+str(b)+" "+str(c)+" "+str(d)+")"
                aj2returnoftheaj.append(anslist)
                break
            else:
                print("I see you found the shortcoming of my program, please leave.")
                exit()
#some formatting code, to add separators between DNF and CNF
food = ""
#do a fancy calculation based on number of characters for the amount of --- in formatting. Cool as HECK. 
for i in range(0,len(anslist*len(vars)*3)):
    food += "-"
print(food)
print("DNF: ")  
#formatting the DNF answer to be separated by "+" and not display brackets.     
print(*aj, sep=" + ")
print(food)
print(" ")
print(food)
#print the CNF answer, this one is easier as we can just format the brackets to parenthesis using *
print("CNF:")
print(*aj2returnoftheaj)
print(food)
print(" ")