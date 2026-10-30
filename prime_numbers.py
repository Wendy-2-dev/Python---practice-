# prime numbers
num = 2
max_nums = int(input())
divisor = 2
while num <= max_nums:
    is_prime = True 
    while divisor <= num:
        if num % divisor == 0:
            is_prime = False 
            break
            divisor += 1
    if is_prime:
        print(num)
    num += 1
    