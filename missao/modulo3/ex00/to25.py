#!/usr/bin/env python3

number_one = int(input("Usuario, entre com um numero menor que 25: "))

if number_one < 25:
    while number_one <= 25:
        print("Dentro do loop, minha variável e: ", number_one)
        number_one += 1
else:
    print("Error")