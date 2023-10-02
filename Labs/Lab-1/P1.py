"""
    Este fichero contiene todos los métodos de la práctica
    Estos comentarios los utiliza pdoc3 para generar la documentación
    Dentro de un entorno virtual (Windows)
    (AEDAS) pdoc --html P1.py 
"""

import numpy as np

def matrix_multiplication(m_1: np.array, m_2: np.array) -> np.array:
    """ 
    Multiplica dos matrices 
    
    Args:
        m_1: Matriz número uno
        m_2: Matriz número dos
    
    Returns:
        Numpy Array: Matriz resultante de la multiplicación de m_1 por m_2    
    """
    n_rows, n_interm, n_columns = \
    m_1.shape[0], m_2.shape[0], m_2.shape[1]
    m_product = np.zeros( (n_rows, n_columns) )
    for i in range(n_rows):
        for j in range(n_columns):
            for k in range(n_interm):
                m_product[i, j] += m_1[i, k] * m_2[k, j]
    return m_product