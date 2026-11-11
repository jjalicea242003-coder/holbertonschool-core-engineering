#!/usr/bin/env python3

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]

def print_list_integer(my_list=[]):
    for numero in my_list:
        print("{:d}".format(numero))

print_list_integer(lista)
