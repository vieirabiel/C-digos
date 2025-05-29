altura=float(input("Adcione sua altura: "))
peso=float(input("Adcione seu peso: "))
imc=peso/(altura*altura)
print("Resultado: ")
print(f"O seu IMC é: {imc:.2f}")
if imc<18.5:
    print("Classificação: Abaixo do peso")
elif imc>=18.5 and imc<=24.9:
    print("Classificação: Peso normal")
elif imc>=25.0 and imc<=29.9:
    print("Classificação: Sobrepeso")
elif imc>=30.0:
    print("Classificação: Obesidade")
