#!/usr/bin/env python3

number_your = input("Usuario, insira um numero")
number_your_int = int(number_your)

if number_your_int < 0:
    print("Este número e negativo.")
elif number_your_int > 0:
    print("Este número e positivo.")
else: 
    print("Este número e positivo e negativo.")