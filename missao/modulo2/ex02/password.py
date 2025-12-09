#!/usr/bin/env python3

correct_password = "42spD+"
password_your = input("Usuario, insira uma senha: ")

if (correct_password == password_your):
    print("ACESSO CONCEDIDO.") 
else: 
    print("ACESSO NEGADO.")