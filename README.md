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

# Operations on Matrices

### Addition and Subraction

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

### Multiplication and Division
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
# [ 31, 8, 44
#   67, 20, 101
#   103, 32, 44 ]
```
### Comparing matrices
`Matrix == Matrix | 0 -> bool`
Matrices can be compared for equality to another matrix
Zero is used as an alias for a zero matrix

## Functionalities

`mathmatrix` provides many functionalities for matrices out of the box:

Let's create a sample matrix `matrix` to perform the operations on
```python
from mathmatrix import Matrix

matrix = Matrix(3,3,[[1,2,3],[4,5,6],[7,8,9]])
```

### Transposing a matrix
`Matrix.transpose() -> Matrix`

After creating a matrix, you can transpose a Matrix using the `transpose()` method of Matrix

```python
print(matrix.transpose())
# [ 1, 4, 7
#   2, 5, 8
#   3, 6, 7 ]
```

### Adjoint of a Matrix
`Matrix.adjoint() -> Matrix`

Adjoint of a matrix is calculated as the transpose of cofactor matrix of a Matrix
It can be calculated using the `adjoint()` method

```pyhton 
print(matrix.adjoint())
# [ -3, 6, -3
#   6, -12, 6
#  -3, 6, -3 ]
```

### Determinant of a Matrix
`Matrix.determinant() -> int | float`

```python 
print(matrix.determinant())
# 0
```

### Inverse of a Matrix
`Matrix.inverse() -> Matrix`

Inverse of a matrix only exists for non-singular matrices ( Determinant of the Matrix should not be zero )

```python 
print(matrix.determinant())
# 0
# Since determinant is zero, if we try to calculate Inverse it will throw the error:
# ZeroDivisionError: Determinant of Matrix is zero, inverse of the matrix does not exist
```

### Cofactor of an element
`Matrix.cofactor(m:int, n:int) -> int | float`

Specify the position of the desired element in row number (m) and column number (n) to calculate it's corresponding cofactor

### Chaining functions
Since functions return a new Matrix, you can chain many functions to get the desired output
For example:
```python
matrix.transpose().adjoint().determinant()
(matrix.determinant() * matrix.adjoint()).transpose()
```
are all completely valid

## Additional Functions

### Generating a zero matrix

`gen_zero_matrix(m:int, n:int) -> Matrix`

You can use the `gen_zero_matrix` function to create a zero matrix of a given order
For example,
```python
from mathmatrix import gen_zero_matrix, Matrix
zero3 = gen_zero_matrix(3,3) 
print(zero3)
# [ 0, 0, 0
#   0, 0, 0
#   0, 0, 0 ]
print(zero3 == 0)
# True
```

### Generating an identity matrix

`gen_zero_matrix(m:int, n:int) -> Matrix`

You can use the `gen_zero_matrix` function to create a zero matrix of a given order
For example,

```python
from mathmatrix import gen_zero_matrix, Matrix
zero3 = gen_zero_matrix(3,3) 
print(zero3)
# [ 0, 0, 0
#   0, 0, 0
#   0, 0, 0 ]
print(zero3 == 0)
# True
```

Note:
For any Matrix `matrix`,

```python
print(matrix * matrix.inverse() == gen_identity_matrix(matrix.m, matrix.n))
# Always true (Inverse cannot be calculated for singular matrices so error is thrown in that case)
print((matrix - matrix) == gen_zero_matrix(matrix.m,matrix.n))
# Always true
```
