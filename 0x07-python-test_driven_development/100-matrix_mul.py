#!/usr/bin/python3
"""
    Modulus for mult of matix
"""


def matrix_mul(m_a, m_b):
    """
    i = 0
        Mult of matrix
        Args:
            m_a: matrix 1
            m_b: matrix 2
        return new matrix mult
    """
    i = 0 #renglon
    j = 0 #columna
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if m_a == []:
        raise ValueError("m_a can't be empty")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if m_b == []:
        raise ValueError("m_b can't be empty")
    if m_a[0] is not None:
        i = len(m_a[0])
    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a must be a list")
        if row == []:
            raise ValueError("m_a can't be empty")
        for value in row:
            if type(value) != int and type(value) != float:
                raise TypeError("m_a should contain only integers or float")
        if len(row) != i:
            raise TypeError("each row of m_a must be of the same size")
    if m_b[0] is not None:
        i = len(m_b[0])
    for row in m_b:
        j = j + 1
        if type(row) != list:
            raise TypeError("m_b must be a list")
        if row == []:
            raise ValueError("m_b can't be empty")
        for value in row:
            if type(value) != int and type(value) != float:
                raise TypeError("m_b should contain only integers or float")
        if len(row) != i:
            raise TypeError("each row of m_b must be of the same size")
    #Se pone interesante
    if (i != j):
        raise ValueError("m_a and m_b can't be multiplied")
        