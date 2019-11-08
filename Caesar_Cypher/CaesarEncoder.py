import sys
#there's other ways to get the entire alphabet into a list, but just to be efficient and have less lines of code, it's just inputted like so.
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#accept standard input, get each line into a list item, line 1 being the message and line 2 the key. 
print("Please paste in your input and <CTRL-Z> when finished.")
A = sys.stdin.read().splitlines()
Input = []
for item in A: 
    Input.append(str(item))

#create the variables for Message and Key from the list I created above
Message = str(Input[0])
key = int(Input[1])

#printing out the Message and Key with formatting
print("Input message: "+Message)
print("Input key: "+str(key))

#creating a blank string to add the characters to
Encoded = ""
#for loop goes through each character in the "Message" string. If the character is an alpha character it uses the alphabet list above, the key, and the modulo operator to locate the new character and append it to the blank string. 
#If it's not an alpha character (such as a space) it's skipped and appended to the string.
for c in Message:
    if c.isalpha(): 
        Encoded += arr[(arr.index(c)+key)%26]
    else: Encoded += c

#print out the encoded message with formatting. 
print("The encoded message with a key of "+str(key)+" is: "+Encoded)