#!/usr/bin/env python3

number_one = input("Usuario, insira o primeiro numero: ")

number_two = input("Usuario, insira o segundo numero: ")

mult_numbers = int(number_one) * int(number_two)

if mult_numbers > 0:
    print("Esta multiplicacao e positivo.")
elif mult_numbers < 0:
    print("Esta multiplicacao e negativa.")
else: 
    print("Esta multiplicacao e zero.")