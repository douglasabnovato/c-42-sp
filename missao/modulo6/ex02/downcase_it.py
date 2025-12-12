#!/usr/bin/env python3

import sys 

if len(sys.argv) == 2: 
    parametro = sys.argv[1] 
    parametro_minusculo = parametro.lower()
     
    print(parametro_minusculo)
else: 
    print("none")