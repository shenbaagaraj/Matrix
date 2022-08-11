n=3
R =int(input("Emter rows"))
C =int(input("Enter columns"))

matrix = []
print("enter the values:")

for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j],end=" ")
    print()
