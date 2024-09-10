# Varibales "constantes":
SEGS_EN_1_HORA = 3600
HORAS_EN_1_DIA = 24
DIAS_EN_1_ANIO = 365

# Variables
mi_edasd = 39

# Multiplicas y obtienes el mismo resultado
"""print("")
edad = mi_edad * DIAS_EN_1_ANIO * HORAS_EN_1_DIA * SEGS_EN_1_HORA
print("")
# print(edad)"""

# Evaluar expresiones
print("")
"""print(1>3)
print("")"""

# Usando if
a = 3

"""if a > 0:
    print('"a" es mayor que cero')
else:
    print('"a" es menor que cero')"""


"""def sum(a,b):
  print(a/b)
sum(15,4)"""




def calcula_segundos_vividos(anios):
    S_EN_H = 3600 # segundos en una hora
    H_EN_D = 24 # horas en un día
    D_EN_A = 365 # días en un año
    calcula_segundos_vividos = anios * D_EN_A * H_EN_D * S_EN_H
    return calcula_segundos_vividos
mi_edad = 39
print(calcula_segundos_vividos(anios = mi_edad))

hija_edad = 1
resultado_hija = (calcula_segundos_vividos(anios=hija_edad))

resultado = calcula_segundos_vividos(anios = mi_edad)
print(f"Has vivido aproximadamente {resultado} segundos.")
print(f"Y tu hija a vivido aproximadamente {resultado_hija} segundos.")


"""def regresa_foo():
  #foo = 9 # variable del ámbito local
  return foo

foo = 1 # variable del ámbito global""

# Intentamos invocar a nuestra función:
print(regresa_foo())"""

"""def regresa_spam():

  
  Función prueba que no recibe argumentos.
  
  spam = 9 # variable del ámbito local
  return spam

# foo = 1 # variable del ámbito global

# Intentamos pedir el valor de spam
print(regresa_spam())"""

#  EJERCICIO 1: ÁREA DE UN CUBO
def area_cubo(arista):

   area_cubo = 6*(arista)**2
   return area_cubo

arg_usuario=4

areaCubo = area_cubo(arista=arg_usuario)

print(F'El área del cubo es de {areaCubo} cm ')



















print("")