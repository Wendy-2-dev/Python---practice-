print("WORD CIPHER")
word = input("Enter 3_letter word")
shift = int(input("shift by how many letters?"))
# convert to ASCII number 
a = chr(ord(word[0]) + shift)
b = chr(ord(word[1]) + shift)
c = chr(ord(word[2]) + shift)
print()
print("The secret message is: ", a  + b  + c)