#!/usr/bin/env python3

import sys
 
args_do_usuario = sys.argv[1:]

found_z = False  
 
if len(args_do_usuario) == 1:
    target_string = args_do_usuario[0]  
    for char in target_string: 
        if char == 'z':
            print("z")
            found_z = True
 
if not found_z and len(args_do_usuario) != 1: 
 
    if not found_z and len(sys.argv) != 2: 
        pass  
 
