
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


def regresa_foo():
  #foo = 9 # variable del ámbito local
  return foo

foo = 1 # variable del ámbito global""

# Intentamos invocar a nuestra función:
print(regresa_foo())

def regresa_spam():

  
  #Función prueba que no recibe argumentos.
  
  spam = 9 # variable del ámbito local
  return spam

# foo = 1 # variable del ámbito global

# Intentamos pedir el valor de spam
print(regresa_spam())


#  EJERCICIO 1: ÁREA DE UN CUBO

def area_cubo(arista):

   area_cubo = 6*(arista)**2
   return area_cubo

arg_usuario=4

areaCubo = area_cubo(arista=arg_usuario)
print("")
print("5.1 Área de un cubo")
print(f'Cuando la arista es de {arg_usuario} cm, el área superficial del cubo es de {areaCubo} cm^2')

print("")

# 5.2 LA HIPOTENUSA

print("5.2 La Hipotenusa")

def hipo (c_opuesto, c_adjacente):
    hipo = (c_opuesto**2 + c_adjacente**2)**(1/2)
    return hipo

us_c_opuesto = 3
us_c_adjacente = 2

hipotenusa = hipo(c_opuesto=us_c_opuesto,c_adjacente=us_c_adjacente)
hipoto = format(hipotenusa,'.2f')
print(f'Cuando el cateto opuesto es de: {us_c_opuesto} cm y el cateto adjacente es de: {us_c_adjacente} cm, la hipotenusa es de: {hipoto} cm')
# Se recomienda round. Qué hace la función y no solo copiar por copiar. qué hace round y format.
# Se pueden utilizar ambas formas. Para legibilidad dejar los parametros, q se presete la menor cantidad de confusiones, se entienda la logica. Encontrar un equilibrio entre legilibidad/logica


# ÁMBITO LOCAL Y GLOBAL



"""
Para usar git en la terminal como lo hemos estado haciendo:
1.- git status: ver cambios en el repositorio
2.- git add <nombre de tu archivo>: agrega el archivo a un repositorio
3.- git commit -m "mensaje": confirma los cambios
4.- git push: sube los cambios a la nube
############################
si alguien hizo cambios y sabes que los hay; para actualizar tu repositorio local haces:
git pull
y puedes trabajar y proseguir con los pasos anteriores.
"""











"Agregando un comentario para probar git"

print("")