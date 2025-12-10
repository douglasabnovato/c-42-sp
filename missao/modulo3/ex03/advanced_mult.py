#!/usr/bin/env python3

multiplication_table = 0

while (multiplication_table <= 10):
    print("Table of ", multiplication_table, ": ", end=" ")
    index = 0

    while (index <= 10):
        print(multiplication_table * index, end=" ")
        index += 1

    print() 
    multiplication_table += 1 