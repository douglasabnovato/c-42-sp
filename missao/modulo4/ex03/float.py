#!/usr/bin/env python3

one_num = input("Me dê um número: ")

if_float = float(one_num)

if if_float.is_integer():
    print(f"'{one_num}' - este numero e inteiro")
else:
    print(f"'{one_num}' - este numero e decimal")