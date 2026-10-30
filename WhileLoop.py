"""
Fibonacci is a series of numbers in which each number is the sum of two preceding numbers.the Fibonacci sequence starts with two ones. consider the following code that prints all Fibonacci numbers less than 20.
"""
# Initializing the first two Fibonacci numbers.
f = 1
g = 1
print(f,end = ' ')
# Run the loop while the last Fibonacci number is less than 20.
while g < 20:
    print (g,end = ' ')
# calculate the next Fibonacci number and update the last two sequence.
temp = f
f = g
g = temp + g

