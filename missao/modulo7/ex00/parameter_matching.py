#!/usr/bin/env python3

import sys

output = "none"
 
args_do_usuario = sys.argv[1:]
 
if len(args_do_usuario) >= 1: 
    parametro_esperado = args_do_usuario[0]
     
    entrada_usuario = input("What was the parameter? ")
     
    if entrada_usuario == parametro_esperado:
        output = "Good job!"
    else:
        output = "Nope, sorry..." 

print(output)
