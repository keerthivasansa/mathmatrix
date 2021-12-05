### Features
- Addition, Multiplication, Division, Subraction operations supported between matrices and between a matrix and a int / float
- Calculates:
	- Determinant
	- Inverse
	- Cofactor of a given element in the Matrix
	- Adjoint

## Getting started

#### Creating a Matrix

To create a matrix, specify the order of the Matrix (mxn) where the first argument (m) is the number of rows in the matrix and the second argument (n) is the number of columns

We can use a nested list to represent a Matrix during initialization of an object
In a nested list, the length of the outer list would be 'm' and the number of elements the inner lists have would be 'n'
```python
from matrix import Matrix

matrix_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix1 = Matrix(3, 3, matrix_list)

print(matrix1)
#Prints:
# [ 1, 2, 3
#   4, 5, 6
#   7, 8, 9 ]
```

## Addition and Subraction

We can add and subract matrices extremely easily:
```python
matrix_list2 = [
    [0, 1, 3], 
    [5, 2, 7], 
    [7, 1, 9]
]
matrix2 = Matrix(3, 3, matrix_list2)
matrix3 = matrix1 + matrix2
print(matrix3)
#Prints:
# [ 1, 3, 6
#   9, 7, 13
#   14, 9, 18 ]
```
Adding an int / float to a matrix will perform the operation on all elements of the matrix and return a new matrix
```python
matrix4 = matrix1 + 5
print(matrix4)
#Prints:
# [ 6, 7, 8
#   9, 10, 11
#   12, 13, 14 ]
# Same way,
print(matrix4 - matrix1)
# [ 5, 5, 5
#   5, 5, 5
#   5, 5, 5 ]
print(matrix1 - 3)
#Prints:
# [ -2, -1, 0
#   1, 2, 3
#   4, 5, 6 ]
```

## Multiplication and Division
Matrix multiplication can only be implemented if the number of columns in the first matrix is equal to the number of rows in the other matrix.
Basically:
A `m x n` Matrix can only be multiplied with a `n x l` Matrix . 

The order of the resultant Matrix will be `m x l`

Example:
```python
# m x n * n x l : Gives l x m
# 2 x 3 * 3 x 2 : Gives 2 x 2
# 2 x 3 * 4 x 2 : Cannot mutliply
``` 

Internally, division is calculated by multiplying a matrix and the inverse of the other matrix therefore the same condition applies for division

```python
print(matrix1 * 5)
# [ 5, 10, 15
#   20, 25, 30
#   35, 40, 45 ]
print(matrix1 * matrix2)

```