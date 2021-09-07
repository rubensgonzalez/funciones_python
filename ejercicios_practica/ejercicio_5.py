# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones y módulos
import random

# --------------------------------
# Aquí dentro definir la función contar

def contar(lista_numeros):
 print("Ingrese el Numero que desea saber cuantas veces esta en la lista")
 a= int(input())
 cant= lista_numeros.count(a)
 print("La cantidad e veces que {} se repite en la Lista es: {}".format(a, cant))
 return


def contar1(lista_numeros, n):
 cant= lista_numeros.count(3)
 return cant
 


# Aquí copiar la función lista_aleatoria
# ya elaborada

def lista_aleatoria(inicio, fin, cantidad):
   mi_lista_aleatoria= []
   i=0
   while i != cantidad:
    i+=1  
    numero = random.randrange(inicio, fin+1)
    #mi_lista_aleatoria[i-1] = numero
    mi_lista_aleatoria.append(numero)
   return mi_lista_aleatoria

# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    inicio = 0
    fin = 9
    cantidad = 5

    # Alumno: Crear la función "contar"

    # Utilice la función "lista_aleatoria"  creado antes 
    # para generar una lista de 5 números en
    # un rango de 1 a 9 inclusive

    # lista_numeros = lista_aleatoria(inicio, fin, cantidad)
    
    lista_numeros = lista_aleatoria(inicio, fin, cantidad)
    
    # Generar una una nueva funcion que se llame "contar",
    # que cuente la cantidad de veces que un elemento pasado
    # por parámetro se repite en la lista también pasada por parámetro
   
    contar(lista_numeros)
    
    # Para saber cuantas veces se repiten el elemento pasado
    # en la lista pueden usar el método nativo de list "count"

    # Por ejemplo creo una lista de 5 elemtnos
    
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)
    
    cantidad_tres = contar1 (lista_numeros, 3)

    # Luego de crear la función invocarla en este lugar:
    # Averiguar cuantas veces se repite el numero 3

    # cantidad_tres = contar(lista_numeros, 3)

    # Imprimir en pantalla "cantidad_tres" que informa
    # cuantas veces se repite el tres en la lista
    
    print("La cantidad de veces que se repite 3 es : {}".format(cantidad_tres))
    
    # print(cantidad_tres)

    print("terminamos")
