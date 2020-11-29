# suma de dos matrices
print('--suma de dos matrices--')
x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0, ]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = +x[i][j] + y[i][j]

print(result)

# Transportar matriz
print('--Transportar matriz--')
x = [[12, 7, 3], [4, 5, 6]]
x_transportada = [[0, 0], [0, 0], [0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        x_transportada[j][i] = x[i][j]
print(x_transportada)

# multiplicar dos matrices: el numero de columnas de la matriz A debe ser igual al nmero de filas de la matriz B
print('---multiplicar matrices--')
# [[a11, a12, a13],[a21,a22,a23],[a31,a32,a33]] * [[b11, b12] [b21,b22]] = [[c11, c12], [c21,c22], [c31,c32]]
# c11 = a11*b11 + a12*b21 + a13*b31
# c21 = a21*b11 + a22*b21 + a23*b31
# c31 = a31*b11 + a32*b21 + a33*b31
# c12 = a11*b12 + a12*b22 + a13*b32
# c22 = a21*b12 + a22*b22 + a23*b32
# c32 = a31*b12 + a32*b22 + a33*b32

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# resultado matriz de 3x4
R = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

# iterrar filas de X
for x in range(len(X)):
    # iterrar columnas de Y
    for y in range(len(Y[0])):
        # iterrar filas de Y
        for c in range(len(Y)):
            R[x][y]+=X[x][c]*Y[c][y]

print(R)

