from typing import Any, Generic, List, Type, Optional, Union
from itertools import repeat
from . import config

intOrFloat = Union[int, float]
nestedList = List[List[intOrFloat]]


def cofactor(l: nestedList, m: int, n: int):
    actualn = len(l)
    return [[l[i][j] for j in range(
        0, n)] + [l[i][j] for j in range(
            n+1, actualn)] for i in range(0, m)] + [[l[i][j] for j in range(
                0, n)] + [l[i][j] for j in range(
                    n+1, actualn)] for i in range(m+1, actualn)]


def adjoint(l: nestedList):
    an = len(l)
    return [[((-1) ** (i + j)) * determinant(cofactor(l, i, j)) for j in range(an)] for i in range(an)]


def determinant(l: nestedList):
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
    __values: nestedList = []
    m = 0
    n = 0

    def __init__(self, m: int, n: int, listInit: nestedList, checkForOrder: bool = True) -> None:
        self.m = m
        self.n = n
        if checkForOrder and config.globalOrderCheck:
            if len(listInit) != m:
                raise ValueError(
                    f"Number of lists ({len(listInit)}) in listInit does not match number of rows 'm' ({m})")
            for row in range(len(listInit)):
                if len(listInit[row]) != n:
                    raise ValueError(
                        f"Length of column number: {row+1} is not equal to the value {n} given in order of Matrix")
        self.__values = listInit

    def __str__(self) -> str:
        out = '[ '
        for i in range(self.m-1):
            for j in range(self.n-1):
                out += str(self.__values[i][j]) + ', '
            out += str(self.__values[i][self.n-1]) + '\n  '
        for j in range(self.n-1):
            out += str(self.__values[self.m-1][j]) + ', '
        out += str(self.__values[self.m-1][self.n-1]) + ' ]'
        return out

    def __eq__(self, __o: object) -> bool:
        if __o == 0:
            return sum([sum(x) for x in self.__values]) == 0
        elif type(__o) == Matrix:
            if self.m != __o.m or self.n != __o.n:
                return False
            for i in range(self.m):
                for j in range(self.n):
                    if self.__values[i][j] != __o[i][j]:
                        return False
            return True
        else:
            raise ValueError(
                'Equality can only be checked between matrices or between a matrix and a 0')

    def __add__(self, other):
        t = type(other)
        if t == int or t == float:
            return Matrix(self.m, self.n, [[other+v for v in x] for x in self.__values], False)
        elif t == Matrix:
            if self.m != other.m or self.n != other.m:
                raise ValueError(
                    'Matrix addition is only implemented for matrices with the same order')
            return Matrix(self.m, self.n, [[self[i][j] + other[i][j] for j in range(self.n)] for i in range(self.m)])
        else:
            raise ValueError(
                'Addition can only be checked between matrices or between a matrix and a nubmer (int or float)')

    def __sub__(self, other):
        t = type(other)
        if t == int or t == float:
            return Matrix(self.m, self.n, [[other-v for v in x] for x in self.__values], False)
        elif t == Matrix:
            if self.m != other.m or self.n != other.m:
                raise ValueError(
                    'Matrix addition is only implemented for matrices with the same order')
            return Matrix(self.m, self.n, [[self[i][j] - other[i][j] for j in range(self.n)] for i in range(self.m)])
        else:
            raise ValueError(
                'Subraction can only be checked between matrices or between a matrix and a nubmer (int or float)')

    def __truediv__(self, other):
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

    def determinant(self) -> intOrFloat:
        return determinant(self.__values)

    def adjoint(self):
        return Matrix(self.m, self.n, adjoint(self.__values), False).transpose()

    def cofactor(self, m: int, n: int) -> intOrFloat:
        '''
        Returns the Cofactor matrix of a given element in the Matrix
        '''
        if self.m != self.n:
            raise ValueError(
                'Cofactors are only available for square matrices')
        return (-1)**(m+n) * determinant(cofactor(self.__values, m-1, n-1))

    def inverse(self):
        '''
        Calculates the inverse of a non-singular matrix using the determinant and adjoint of the matrix
        '''
        det = determinant(self.__values)
        if det == 0:
            raise ZeroDivisionError(
                'Determinant of Matrix is zero, inverse of the matrix does not exist')
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
    outer = []
    inner = []
    inner.extend(repeat(0, n))
    outer.extend(repeat(inner, m))
    return Matrix(m, n, outer, False)


def gen_identity_matrix(m: int, n: int) -> Matrix:
    '''
    Generats an idenitity matrix of order m x n
    '''
    return Matrix(m, n, [[1 if i == j else 0 for j in range(n)] for i in range(m)], False)
