#!/usr/bin/env python3

def raise_exception():
    raise TypeError

try:
    rasie_exception()
    print("Funcion ejecutada")
except TypeError:
          print("Excepcion capturada")

print("Programa finalizado")
