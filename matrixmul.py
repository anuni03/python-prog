c1=int(input("Enter the number of columns in matrix1 "))
r1=int(input("Enter the number of rows in matrix1  "))
c2=int(input("Enter the number of columns in matrix2  "))
r2=int(input("Enter the number of rows in matrix2  "))
rslt=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
mat1=[]
mat2=[]
print("Enter matrix 1:")
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(int(input()))
    mat1.append(a)
print("Enter matrix 2: ")
for i in range(0,r2):
    b=[]
    for j in range(0,c2):
        b.append(int(input()))
    mat2.append(b)
if r1!=c2:
    print("Matrix cannot be multiplied")
else:
    for i in range(0,r1):
        for j in range(0,c1):
            for k in range(0,r2):
                rslt[i][j]+=mat1[i][k]*mat2[k][j]

print("Multiplication of above matrix is: ")
for i in range(0,r1):
    for j in range(0,c2):
        print(rslt[i][j],end=" ")
    print()
       