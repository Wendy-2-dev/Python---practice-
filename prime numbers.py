n = int(input())
for i in range(2,n+1):
    prime = True
    for divisor in range(2,i):
        if i % divisor == 0:
            prime = False
            break
    if prime:
        print(i,end = " ")