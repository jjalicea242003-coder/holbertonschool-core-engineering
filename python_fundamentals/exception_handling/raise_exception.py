#!/usr/bin/env python3

def rasie_exception():
    raise Typeerror

try:
    rasie_exception()
    print("Funcion ejecutada")
except TypeError:
          print("Excepcion capturada")

print("Programa finalizado")
