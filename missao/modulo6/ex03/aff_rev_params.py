#!/usr/bin/env python3

import sys  

numero_de_parametros_reais = len(sys.argv) - 1
 
if numero_de_parametros_reais < 2:
    print("none")
else:
     
    parametros_reais = sys.argv[1:]
    
    parametros_reversos = parametros_reais[::-1]
     
    for param in parametros_reversos:
        print(param)

