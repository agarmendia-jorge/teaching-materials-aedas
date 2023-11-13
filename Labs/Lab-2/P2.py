"""
    Este fichero contiene todos los métodos de la práctica
    Estos comentarios los utiliza pdoc3 para generar la documentación
    Dentro de un entorno virtual (Windows)
    pylint P2.py --rc-file my_pylintrc
"""
__author__ = "Antonio Garmendia"
__copyright__ = "Copyright 2024"
__credits__ = ["eps-uam", "A. Garmendia", "A. Someone Else"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Team"
__email__ = "antonio.garmendia@uam.es"
__status__ = "Production"


import time

def fibonacci_rec(number: int)-> int:
    """
    Esta función devuelve el número de fibonacci
    """
    f1: int = 1
    if number <= f1:
        return number
    fn = fibonacci_rec(number-1) + fibonacci_rec(number-2)
    return fn

###############################################################################################
# Módulo de Python que empieza a ejecutarse
if __name__ == '__main__':
    nb: int = 20
    start = time.time()
    fibonacci_number = fibonacci_rec(nb)
    finish = time.time()
    print(f'El número de fibonacci es: {fibonacci_number}')
    print(f'El algoritmo tardó: {finish - start} en encontrar el número de Fibonacci para el número {nb}')
    