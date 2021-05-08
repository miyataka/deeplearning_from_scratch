import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
type(x)

# 1.5.3
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x + y
x - y
x * y
x / y

x / 2.0


# 1.5.4
A = np.array([[1, 2], [3, 4]])
print(A)
A.shape
A.dtype

B = np.array([[3, 0], [0, 6]])
A + B
A * B

print(A)
A * 10


# 1.5.5
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])

A * B


# 1.5.6
X = np.array([[51, 55], [14, 19], [0, 4]])
X[0]
X[0][1]

for row in X:
    print(row)

X = X.flatten()
print(X)

X[np.array([0, 2, 4])]

X > 15
X[X > 15]
