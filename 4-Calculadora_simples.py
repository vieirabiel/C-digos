opcao=int
while opcao !=0:
    print("Calculadora")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    opcao=int(input("Escolha uma opção: "))
    if opcao>=1 and opcao<=4:
        numero1=float(input("Digite o primeiro número: "))
        numero2=float(input("Digite o segundo número: "))
    if opcao==1:
        resultado=numero1+numero2
        print(f"Resiltado da soma: {resultado}")
    elif opcao==2:
        resultado=numero1-numero2
        print(f"Resultado da subtração: {resultado}")
    elif opcao==3:
        resultado=numero1*numero2
        print(f"Resultado da multiplicação: {resultado}")
    elif opcao==4:
        if numero2 !=0:
            resultado=numero1/numero2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: não é possivel dividir por zero.")
    elif opcao==0:
        print("Encerrando a calculadora...")
    else:
        print("Erro: opção inválida.")