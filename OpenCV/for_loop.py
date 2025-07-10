# introduction to for loop

#============================================================
# one dimension
#============================================================
for i in range(8):
    print("I'm the", i, "number!")
    print("scores: %d" %(i))

print("scores: %d" %(i))

#================================================
for i in range(6):
    sum += i
print(sum)

n = input("Please enter the integer number:")
sum = 0
for i in range(int(n)+1):
    sum += i

print(sum)

#================================================
n = int(input("Please enter the integer number:"))
max_number = 0
for i in range(n+1):
    random_n = int((input("Enter a number:")))
    if random_n < max_number:
        print("It's not greater to the maximum", max_number)
    else:
        max_number = random_n
        print("max_number = ", max_number)

#================================================
n = int(input("Please enter the integer number:"))
max_number = 0
for i in range(n):
    random_n = int((input("Enter a number:")))
    if random_n <= max_number:
        print("It's not greater than the maximum", max_number)
        if random_n % 2 == 0:
            print("But it is the odd number!")
    else:
        max_number = random_n
        print("The max_numner is", max_number)
        if(max_number % 2 == 1):
            print("It is the even number!")

#================================================
x = int(input("Please input a number(multiplication):"))
number = 1;
for i in range(1, x+1):
    number = number * i
    print(number)




#============================================================
# two dimension
#============================================================
for x in range(1,10):
    for y in range(1,10):
        print(f"{x} * {y} = {x*y}")

#================================================
a = int(input("minimum number:"))
b = int(input("maximum number:"))
sum = 0
if a >= b:
    print("The range is wrong!")
else:
    for i in range(a, b+1):
        x = i
        if(x % 2 == 0):
            sum += x
print(sum)

#================================================
a = [0 for _ in range(3)]
print(a)

#================================================
a = list(map(lambda x: x**2, [1,2,3,4,5]))
print(a)
print(a[-2])
print(a[1:4])
print(a[::2])
print(a[-5:-1])
print(a[::-1])

#================================================
x = "HelloPython"
print(x[1:4])
print(x[1::2])
print(x[0::2])
print(x[::-1])

#================================================
import random 
x = random.sample(range(1, 10), 5)
print(x)
print(x.sort())
y = sorted(x)
print(y)

#================================================
x = []
print(x)
n = 2
x = 1
x = [x] * n
print(x)
h = 3
y = [x for _ in range(h)]
print(y)

#================================================
x = [0 for _ in range(5)]
sum = 0
for i in range(len(x)):
    num = int(input("Enter any number:"))
    if num > 10:
        sum += num
        x[i] = num
print(sum)
print(x)
print(sum(x))

#================================================
x = random.sample(range(1, 10), 5)
y = int(input("Please input a number from 1 to 10:"))
print(x)
for i in range(len(x)):
    if(x[i] == y):
        print("Find the value", y)
    else:
        print("Failure!")
if y in x:
    print("Success!")
else:
    print("Failure!")

#================================================
x = [[0] * 3 for _ in range(4)]
print(x)
rows = 3
cols = 4
matrix = [[i * j for j in range(cols)] for i in range(rows)]
print(matrix)
for row in matrix:
    print(row)

#================================================
rows = 3
cols = 4
x = [[i * j for j in range(cols)] for i in range(rows)]
print(x)

for i in range(rows):
    rowSum = sum(x[i][:])
    print(rowSum)

for j in range(cols):
    colSum = 0
    for i in range(rows):
        colSum += x[i][j]
    print(colSum)

#================================================
rows = 3
cols = 4
dp = 2
mat = []

for k in range(dp):
    depth = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        depth.append(row)
    mat.append(depth)

for col, mat in enumerate(mat):   
    print(f"depth: {col}")
    for i in mat:
        print(i)
    print()

#================================================
rows = 3
cols = 4
dp = 3
mat = []

for k in range(dp):
    depth = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if k == 0:
                value = 1
            elif k == 1:
                value = 0
            elif k == 2:
                value = 255
            row.append(value)
        depth.append(row)
    mat.append(depth)

for col, mat in enumerate(mat):   
    print(f"depth: {col}")
    for i in mat:
        print(i)
    print()

print(mat)
print((mat[1][2][1]))
print(len(mat[1]))
col2 = [mat[1][i][2] for i in range(len(mat[1]))]
print(col2)

#================================================
