message = str(input())
shift = len(message)
for i in message:
    j = chr(ord(i) + shift)
    print(j,end = " ")