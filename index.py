""" Gabriel Souza Scopel - 222210262    
Kaique da Silva Fernandes - 222210114
Murilo Carvalho Povoa da Silva - 222210346
Matheus Arcanjo - 222210205 """


from math import *

def P_a():
    print("1 - Entrada θ1, θ2, I0 e saída em I1 e I2")
    print("2 - Entrada θ1, θ2, I1 e saída em I0 e I2")
    print("3 - Entrada θ1, θ2, I2 e saída em I0 e I1")
    a = input("Insira o código do que você deseja calcular: ")
    if(a == "1"):
        P_a1()
    elif(a == "2"):
        P_a2()
    elif(a == "3"):
        P_a3()
    else:
        print("Digite um comando válido")
        P_a()
def P_a1():
    ang1 = radians(float(input("Informe o ângulo θ1: ")))
    ang2 = radians(float(input("Informe o ângulo θ2: ")))
    i0 = float(input("Informe o valor de I0: "))
    i1 = i0/2
    i2 = i1*(cos(ang2-ang1))**2
    print(f"A Intensidade de I1 é: {i1:.2f} W/m2\n")
    print(f"A Intensidade de I2 é: {i2:.2f} W/m2\n")

def P_a2():
    ang1 = radians(float(input("Informe o ângulo θ1: ")))
    ang2 = radians(float(input("Informe o ângulo θ2: ")))
    i1 = float(input("Informe o valor de I1: "))
    i0 = i1*2
    i2 = i1*(cos(ang2-ang1))**2
    print(f"A Intensidade de I0 é: {i0:.2f} W/m2\n")
    print(f"A Intensidade de I2 é: {i2:.2f} W/m2\n")

def P_a3():
    ang1 = radians(float(input("Informe o ângulo θ1: ")))
    ang2 = radians(float(input("Informe o ângulo θ2: ")))
    i2 = float(input("Informe o valor de I2: "))
    i1 = i2/((cos(ang2-ang1))**2)
    i0 = i1*2
    print(f"A Intensidade de I0 é: {i0:.2f} W/m2\n" )
    print(f"A Intensidade de I1 é: {i1:.2f} W/m2\n")
#########estruturar P_b no mesmo modelo de P_a
def P_b():
    print("1 - Entrada θ1, θ2, θ3, I0 e saída em I1, I2 e I3")
    print("2 - Entrada θ1, θ2, θ3, I1 e saída em I0, I2 e I3")
    print("3 - Entrada θ1, θ2, θ3, I2 e saída em I0, I1 e I3")
    print("4 - Entrada θ1, θ2, θ3, I3 e saída em I0, I1 e I2")
    a = input("Insira o código do que você deseja calcular: ")
    if(a == "1"):
        P_b1()
    elif(a == "2"):
        P_b2()
    elif(a == "3"):
        P_b3()
    elif( a== "4"):
        P_b4()    
    else:
        print("Digite um comando válido")
        P_b()
def P_b1():
    ang1 = radians(float(input("Informe o ângulo θ1: ")))
    ang2 = radians(float(input("Informe o ângulo θ2: ")))
    ang3 = radians(float(input("Informe o ângulo θ3: ")))
    i0 = float(input("Informe o valor de I0: "))
    i1 = i0/2
    i2 = i1*(cos(ang2-ang1))**2
    i3 = i2*(cos(ang3-ang2))**2
    print(f"A Intensidade de I1 é: {i1:.2f} W/m2\n")
    print(f"A Intensidade de I2 é: {i2:.2f} W/m2\n")
    print(f"A Intensidade de I3 é: {i3:.2f} W/m2\n")

def P_b2():
    ang1 = radians(float(input("Informe o ângulo θ1: ")))
    ang2 = radians(float(input("Informe o ângulo θ2: ")))
    ang3 = radians(float(input("Informe o ângulo θ3: ")))
    i1 = float(input("Informe o valor de I1: "))
    i0 = i1*2
    i2 = i1*(cos(ang2-ang1))**2
    i3 = i2*(cos(ang3-ang2))**2
    print(f"A Intensidade de I0 é: {i0:.2f} W/m2\n")
    print(f"A Intensidade de I2 é: {i2:.2f} W/m2\n")
    print(f"A Intensidade de I3 é: {i3:.2f} W/m2\n")

def P_b3():
    ang1 = radians(float(input("Informe o ângulo θ1: ")))
    ang2 = radians(float(input("Informe o ângulo θ2: ")))
    ang3 = radians(float(input("Informe o ângulo θ3: ")))
    i2 = float(input("Informe o valor de I2: "))
    i1 = i2/((cos(ang2-ang1))**2)
    i0 = i1*2
    i3 = i2*(cos(ang3-ang2))**2
    print(f"A Intensidade de I0 é: {i0:.2f} W/m2\n")
    print(f"A Intensidade de I1 é: {i1:.2f} W/m2\n")
    print(f"A Intensidade de I3 é: {i3:.2f} W/m2\n")
def P_b4():
    ang1 = radians(float(input("Informe o ângulo θ1: ")))
    ang2 = radians(float(input("Informe o ângulo θ2: ")))
    ang3 = radians(float(input("Informe o ângulo θ3: ")))
    i3 = float(input("Informe o valor de I3: "))
    i2 = i3/(cos(ang3-ang2))**2
    i1 = i2/((cos(ang2-ang1))**2)
    i0 = i1*2
    print(f"A Intensidade de I0 é: {i0:.2f} W/m2\n")
    print(f"A Intensidade de I1 é: {i1:.2f} W/m2\n")
    print(f"A Intensidade de I2 é: {i2:.2f} W/m2\n")

def main():
    print("Autores do código:")
    print("Gabriel de Souza Scopel")
    print("Matheus Arcanjo")
    print("Kayque da Silva Fernandes")
    print("Murilo Carvalho Povoa da Silva")
    print()
    print("Estudo da polarização da luz.")
    print("Este programa realiza cálculos envolvendo 2 ou 3 polarizadores")
    print("sendo possível calcular a intesidade da luz antes e depois de passa pelos mesmo")
    print("a luz incidente é não polarizada")
    print("As unidades devem estar no sistema internacional")
    
    print("Todas as unidades de medida devem ser inseridas no sistemas internacional\n")
    
    print()
    while True:
        count = input("O cálculo envolve 2 ou 3 polarizadores? ")
        
        if count == '2':
            P_a()
        elif count == '3':
            P_b() 
        else:
            print("Você digitou um comando inválido.")
main()