from typing import Any, Generic, List, Type, Optional
from itertools import repeat
from . import config


def cofactor(l: List[List[int]], m: int, n: int):
    actualn = len(l)
    return [[l[i][j] for j in range(
        0, n)] + [l[i][j] for j in range(
            n+1, actualn)] for i in range(0, m)] + [[l[i][j] for j in range(
                0, n)] + [l[i][j] for j in range(
                    n+1, actualn)] for i in range(m+1, actualn)]

def adjoint(l: List[List[int]]):
    an = len(l)
    return [[((-1) ** (i + j)) * determinant(cofactor(l, i, j)) for j in range(an)] for i in range(an)]


def determinant(l: List[List[int]]):
    det = 0
    if len(l) == 1:
        return l[0][0]
    elif len(l) == 2:
        return (l[0][0] * l[1][1]) - (l[1][0] * l[0][1])
    for col in range(len(l)):
        det += (((-1)**(col)) * l[0][col] * determinant(cofactor(l, 0, col)))
    return det


class Matrix:
    '''
    Creates a new Matrix with order m, n\n
    Takes a nested list to initialize itself\n
    Pass `checkForOrder=False` to prevent checking individually
    '''
    __values: List[List[int]] = []
    m = 0
    n = 0

    def __init__(self, m: int, n: int, listInit: List[List[int]], checkForOrder:bool=True) -> None:
        self.m = m
        self.n = n
        if checkForOrder and config.globalOrderCheck:
            print(checkForOrder)
            print('orderchk')
            if len(listInit) != m:
                raise ValueError(f"Number of lists ({len(listInit)}) in listInit does not match number of rows 'm' ({m})")
            for row in range(len(listInit)):
                if len(listInit[row]) != n:
                    raise ValueError(f"Length of column number: {row+1} is not equal to the value {n} given in order of Matrix")
        self.__values = listInit

    def __str__(self) -> str:
        out = '[ '
        for i in range(self.m-1):
            for j in range(self.n-1):
                out += str(self.__values[i][j]) + ', '
            out += str(self.__values[i][self.n-1]) + '\n  '
        for j in range(self.n-1):
            out += str(self.__values[self.m-1][j]) + ', '
        out += str(self.__values[i-1][self.n-1]) + ' ]'
        return out

    def __eq__(self, __o: object) -> bool:
        if __o == 0:
            return sum([sum(x) for x in self.__values]) == 0

    def __add__(self, other):
        t = type(other)
        if t == int or t == float:
            return Matrix(self.m, self.n, [[other+v for v in x] for x in self.__values], False)
        elif t == Matrix:
            if self.m != other.m or self.n != other.m:
                raise ValueError(
                    'Matrix addition is only implemented for matrices with the same order')
            return [[self[i][j] + other[i][j] for j in range(self.n)] for i in range(self.m)]

    def __truediv__(self,other):
        t = type(other)
        if t == int or t == float:
            return Matrix(self.m, self.n, [[other+v for v in x] for x in self.__values], False)
        elif t == Matrix:
            return self.__mul__(other.inverse())

    def __mul__(self, other):
        t = type(other)
        if t == int or t == float:
            return Matrix(self.m, self.n, [[other*v for v in x] for x in self.__values], False)
        elif t == Matrix:
            if self.n != other.m:
                raise ValueError(
                    'Matrix multiplication can only be implemented for matrices if the number of rows in Matrix 1 is equal to number of columns in Matrix 2')
            return Matrix(self.m, other.n, [[sum([self.__values[i][k] * other[k][j] for k in range(self.n)]) for j in range(other.n)] for i in range(self.m)], False)

        else:
            raise ValueError(
                'Matrix can only be multiplied with an integer, float or another Matrix')

    def __repr__(self) -> str:
        return f"Matrix[{self.m},{self.n}]"

    def cofactor(self, m: int, n: int):
        return [[self.__values[i][j] for j in range(
            0, n)] + [self.__values[i][j] for j in range(
                n+1, self.n)] for i in range(0, m)] + [[self.__values[i][j] for j in range(
                    0, n)] + [self.__values[i][j] for j in range(
                        n+1, self.n)] for i in range(m+1, self.m)]

    def determinant(self) -> int:
        return determinant(self.__values)

    def adjoint(self):
        return Matrix(self.m, self.n, adjoint(self.__values), False).transpose()

    def cofactor(self, m: int, n: int):
        '''
        Returns the Cofactor matrix of a given element in the Matrix
        '''
        return Matrix(self.m, self.n, cofactor(self.__values, m, n), False)

    def inverse(self):
        '''
        Calculates the inverse of a non-singular matrix using the determinant and adjoint of the matrix
        '''
        det = determinant(self.__values)
        if det == 0:
            raise ZeroDivisionError(
                'Determinant of Matrix is zero, cannot calculate inverse of matrix')
        return self.adjoint() * (1/det)

    def transpose(self):
        '''
        Returns the tranpose of the matrix
        '''
        return Matrix(self.n, self.m, [[self.__values[j][i] for j in range(self.m)] for i in range(self.n)], False)

    def __getitem__(self, sub: Any) -> List[int]:
        t = type(sub)
        if t == int:
            try:
                return self.__values[sub]
            except IndexError:
                raise Exception('Row number must be an integer greater than or equal to 1' if sub <
                                0 else 'Row number exceeds size of the Matrix')


def gen_zero_matrix(m: int, n: int) -> Matrix:
    '''
    Generates a zero matrix of order m x n
    '''
    return Matrix(m, n, [].extend(repeat([].extend(repeat(0, n)), m)), False)

def gen_identity_matrix(m: int, n: int) -> Matrix:
    '''
    Generats an idenitity matrix of order m x n
    '''
    return Matrix(m, n, [[1 if (i+j) % 2 == 0 else 0 for j in range(n)] for i in range(m)], False)
