print("Conversor de temperatura")
print("Escolha qual ocê quer transformar: ")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
opcao=int(input("Ecolha uma opção: "))
temp_inicial=float(input("Digite a temperatura inicial (C): "))
if opcao ==1 or opcao ==2:
    if opcao==1:
        resultado=(temp_inicial*9/5)+32
        print(f"{resultado} Fahrenheit")
    elif opcao==2:
        resultado=temp_inicial+273.15
        print(f"{resultado} Kelvin")
else:
    print("Opção inválida")