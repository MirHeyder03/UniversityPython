# import numpy  as np

# A = np.arange(4)
# print('A =', A)

# B = np.arange(12).reshape(2, 6)
# print('B =', B)

''' 
Output:
A = [0 1 2 3]
B = [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
'''


A = [[1, -2, 3],
     [-4, -5, 6],
     [17, -8, 9]]

max = A[0][0]
for i in range(len(A)):
    for j in range(len(A[0])):
        if (A[i][j] > max):
            max = A[i][j]
print(max)





