#!/usr/bin/python3.5
"""

A module that multiplies 2 matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ A function that multiplies 2 matrices

    Args:
        m_a: the matrix a
        m_b: the matrix b

    Returns:
        the result of the multiplication


    """

    return (np.matmul(m_a, m_b))
