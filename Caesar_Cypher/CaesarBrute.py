import sys
#there's other ways to get the entire alphabet into a list, but just to be efficient and have less lines of code, it's just inputted like so.
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#accept standard input, get each line into a list item, line 1 being the message and line 2 the key. 
print("Please paste in your input and <CTRL-Z> when finished.")
A = sys.stdin.read().splitlines()
Input = []
for item in A: 
    Input.append(str(item))

#create the variable for Message
#really, I could set it up so that there isn't a for loop and I just convert the stdin to a string but I'm tired and I want to go home
Message = str(Input[0])

print(Message)

#loop through every possible key using a range function, from 0 to 25. For each key, do the same as what was done in the decoder file. 
for i in range (0,26):
    Decoded = ""
    for c in Message:
        if c.isalpha(): 
            Decoded += arr[(arr.index(c)-i)%26]
        else: Decoded += c
    print("Key of "+str(i)+" decodes to: "+Decoded)

