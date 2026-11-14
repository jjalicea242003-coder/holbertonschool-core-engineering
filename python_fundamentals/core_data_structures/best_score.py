#!/usr/bin/env python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    mejor_nombre = None
    mejor_puntuacion = None

    for nombre, puntuacion in a_dictionary.items():
        if mejor_puntuacion is None or puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            mejor_nombre = nombre

    return mejor_nombre
