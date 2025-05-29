nome=input("Digite seu nome: ")
print("======IMPORTANTE======")
print("R$ 90,00 por dia alugado!")
print("R$ 0,20 por km rodado!")

dias=int(input("Informe quantos dias o carro ficou alugado: "))
km=int(input("Informe quantos quilometros rodados: "))

total=(dias*90)+(km*0.20)
print("================")
print(f"Dias alugados: {dias}")
print(f"Kms rodados: {km}")
print("================")
print(f"Total a pagar: R$ {total}")
