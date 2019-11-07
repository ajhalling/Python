import sys
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Please paste in your input and <CTRL-Z> when finished.")
A = sys.stdin.read().splitlines()
Input = []
for item in A: 
    Input.append(str(item))

Message = str(Input[0])

print(Message)

for i in range (0,26):
    Encoded = ""
    for c in Message:
        if c.isalpha(): 
            Encoded += arr[(arr.index(c)-i)%26]
        else: Encoded += c
    print("Key of "+str(i)+" decodes to: "+Encoded)

