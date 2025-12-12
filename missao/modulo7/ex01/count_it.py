#!/usr/bin/env python3

import sys
 
args_do_usuario = sys.argv[1:]
 
num_parametros = len(args_do_usuario)
 
if num_parametros == 0:
    print("none")
else: 
    print(f"parameters:{num_parametros}") 
    for param in args_do_usuario:
        comprimento = len(param)
        print(f"{param}:{comprimento}")

