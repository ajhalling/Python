import sys
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Please paste in your input and <CTRL-Z> when finished.")
A = sys.stdin.read().splitlines()
Input = []
for item in A: 
    Input.append(str(item))

Message = str(Input[0])
key = int(Input[1])

print("Input message: "+Message)
print("Input key: "+str(key))

Encoded = ""
for c in Message:
    if c.isalpha(): 
        Encoded += arr[(arr.index(c)+key)%26]
    else: Encoded += c

print("The encoded message with a key of "+str(key)+" is: "+Encoded)