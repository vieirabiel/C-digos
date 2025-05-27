nome=str(input("Digite o nome do vendedor: "))
salarioFixo=float(input("Digite o sálario fixo do vendedor: "))
totalVendas=float(input("Digite o total de vendas efetuadas: "))
bonus=salarioFixo*0.15
salarioRecebido=salarioFixo+bonus
if totalVendas>=20: 
    print("Meta atingida!")
    print(f"Nome do vendedor: {nome}")
    print(f"Salário fixo:R$ {salarioFixo}")
    print(f"Bônus:R$ {bonus}")
    print(f"Sálario total com comissão:R$ {salarioRecebido}")
else:
    print("Meta não atingida.")
    print(f"Nome do vendedor: {nome}")
    print(f"Salário fixo:R$ {salarioFixo}")