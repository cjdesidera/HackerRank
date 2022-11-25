#!/bin/python3

import math
import os
import random
import re
import sys

# Se for impar, imprima Estranho
# Se for par e estiver no intervalo inclusivo de 2 a 5 , imprima Not Weird
# Se for par e estiver no intervalo inclusivo de 6 a 20 , imprima Weird
# Se for par e maior que 20, imprima Not Weird
if __name__ == '__main__':
    n = int(input().strip())
    if n >= 1 and n <= 100:
        if n % 2 == 0:
            if n > 20:
                print('Not Weird')
            else:
                if n >= 6:
                    print('Weird')
                else:
                    print('Not Weird')
        else:
            print('Weird')
