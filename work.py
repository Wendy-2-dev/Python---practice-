word_list = ['awuor','Wendy','23','year old']
wisdom = word_list.copy()
wisdom.sort()
detail = []
for i in wisdom:
    detail.append(i)
print(" ".join(detail))

list1 = [[1,2,3],
         [1,4,9],
         [1,8,27]]
for row in list1:
    for element in row:
        print(element,end = " ")
    print()

mat_W = [[13,4,5],
         [2,-9,7],
         [7,3,19]]
         
mat_Z = [[2,1,5],
         [3,7,9],
         [-1,13,19]]
         
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(mat_W)):
    for j in range(len(mat_Z[0])):
        for k in range(len(mat_Z)):
            result[i][j] += mat_W[i][k] * mat_Z[k][j]
            

for row in result:
    print(row,end = " ")
    print()
    
square_list = []
for i in range(10):
    square_list.append(i**2)
print(square_list)
cube_list = [i**3 for i in range(10)]
print(cube_list)

word = ["one","two","red","blue"]
new_word = [element + " fish" for element in word]# list comprehension 
for i in new_word:
    print(i)

a = 0
b = 1   
num = 30

fib = [a,b]
while b <= num:
    c = a + b
    a = b
    b = c
    fib.append(c)
print(fib)
new_fib = [i for i in fib if i%2 != 0] #filtering a list
print(new_fib)               