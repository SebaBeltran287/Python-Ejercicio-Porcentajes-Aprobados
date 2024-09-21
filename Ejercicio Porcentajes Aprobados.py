import os
import math
os.system("cls")
def ultimo_promedio (nota1,nota2,nota3):
    promedio=(nota1+nota2+nota3)/3
    return promedio
aprobados=0
reprobados=0
print ("Ingrese las notas de Juan: ")
nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input("Nota 3: "))
promedio_juan=ultimo_promedio(nota1, nota2, nota3)
promedio_juan=round(promedio_juan,1)
print(f"El promedio de Juan es: {promedio_juan}")
if promedio_juan>=4.0:
    aprobados=aprobados+1
else:
    reprobados=reprobados+1
print ("Ingrese las notas de Maria: ")
nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input("Nota 3: "))
promedio_maria=ultimo_promedio(nota1, nota2, nota3)
promedio_maria=round(promedio_maria,1)
print(f"El promedio de Maria es: {promedio_maria}")
if promedio_maria>=4.0:
    aprobados=aprobados+1
else:
    reprobados=reprobados+1
print ("Ingrese las notas de Diego: ")
nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input("Nota 3: "))
promedio_diego=ultimo_promedio(nota1, nota2, nota3)
promedio_diego=round(promedio_diego)
print(f"El promedio de Diego es: {promedio_diego}")
if promedio_diego>=4.0:
    aprobados=aprobados+1
else:
    reprobados=reprobados+1
print ("Ingrese las notas de Francisca: ")
nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input("Nota 3: "))
promedio_francisca=ultimo_promedio(nota1, nota2, nota3)
promedio_francisca=round(promedio_francisca,1)
print(f"El promedio de Francisca es: {promedio_francisca}")
if promedio_francisca>=40:
    aprobados=aprobados+1
else:
    reprobados=reprobados+1
print ("Ingrese las notas de Pedro: ")
nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input("Nota 3: "))
promedio_pedro=ultimo_promedio(nota1, nota2, nota3)
promedio_pedro=round(promedio_pedro,1)
print(f"El promedio de Pedro es: {promedio_pedro}")
if promedio_pedro>=4.0:
    aprobados=aprobados+1
else:
    reprobados=reprobados+1
porcentaje=100/5
porcentaje_aprobados=porcentaje*aprobados
porcentaje_reprobados=porcentaje*reprobados 
print(f"El porcentaje de alumnos aprobados es: {porcentaje_aprobados}%  y el de reprobados es: {porcentaje_reprobados}%")
