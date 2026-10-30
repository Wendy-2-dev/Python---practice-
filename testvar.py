#calculating area
def print_area(base,height):
    return (base * height)/2
# find area
b = int(input())
h = int(input())
print_area(b,h)
print(f"Area of the triangle 📐 is:{print_area(b,h)}")
# curving scores
def print_scores(test_scores, bonus):
    for i in range(len(test_scores)):
        test_scores[i] = test_scores[i] + bonus 
grades = [67,68,72,71,69]
adds = 10
print_scores(grades,adds)
for grade in grades:
    print(f"{grade} would be updated to {print_scores(grades,adds)}")
from myfunctions import km2mi
print("Woah, that's like", round(km2mi(40)))
 
     
       
        

 