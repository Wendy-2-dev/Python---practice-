import math
def average(x,y):
    return (x + y) / 2
print(math.__name__)
print(__name__)
def cel2fah(c):
    """ convert temp from Celsius to Fahrenheit"""
    return (9/5 * c) + 32
print(math.__name__)
print(__name__)
def fah2cel(f):
    """convert temp from Fahrenheit to Celsius"""
    return 5/9 * (f - 32)
print(math.__name__)
print(__name__)
def km2mi(km):
    """ convert distance from kilometers to miles"""
    return km/1.60934
print(math.__name__)
print(__name__)
def mi2km(mi):
    """ convert distance from miles to kilometers"""
    return mi * 1.60934
print(math.__name__)
print(__name__)
def rad2deg(R):
    """ convert radians to degrees"""
    return R * (180/math.pi)
print(math.__name__)
print(__name__)
def deg2rad(D):
    """ convert degrees to radians"""
    return (D * math.pi) / 180
print(math.__name__)
print(__name__)
def Fibonacci(fn1,fn2,N):
    N = int(input())
    for fn3 in range(N):
        fn3 = fn1 + fn2
        fn1 = fn2
        fn2 = fn3
        print(fn1,fn2,end = " ")
print(math.__name__)
print(__name__)
def area_rectangle(length, width):
    return length * width
print(math.__name__)
print(__name__)
def area_circle(radius):
    return math.pi * radius**2
print(math.__name__)
print(__name__)
   
        
  
  
    
    

