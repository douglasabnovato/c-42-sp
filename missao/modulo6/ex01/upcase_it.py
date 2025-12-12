#!/usr/bin/env python3

import sys 

if len(sys.argv) == 2: 
    parametro = sys.argv[1] 
    parametro_maiusculo = parametro.upper()
     
    print(parametro_maiusculo)
else: 
    print("none")