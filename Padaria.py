opcao=frances=integral=doceLiso=doceFarofa=forma=0
valorFrances=valorIntegral=valorDoceLiso=valorDoceFarofa=valorForma=valorTotal=0
while opcao !=6:
    print("PADARIA")
    print("1-Pão francês")
    print("2-Pão integral")
    print("3-Pão doce Liso")
    print("4-Pão doce Farofa")
    print("5-Pão de Forma")
    print("6- Fim da compra")
    opcao=int(input("Escolha sua opção: "))
    if opcao==1:
        frances=int(input("Digite a quantidade de pão francês: "))
        valorFrances=frances*1.04
    elif opcao==2:
        integral=int(input("Digite a quantidade de pão interal: "))
        valorIntegral=integral*1.04
    elif opcao==3:
        doceLiso=int(input("digite a quantidade de pão doce: "))
        ValorDoceLiso=doceLiso*1.08
    elif opcao==4:
        doceFarofa=int(input("Digite a quantidade de pão farofa: "))
        ValorDoceFarofa=doceFarofa*1.11
    elif opcao==5:
        forma=int(input("Digite a quantidade de pão de Forma: "))
        valorForma=forma*0.95
    elif opcao==6:
        print("Fim da compra.")
    else:
        print("opção inválida")
print ("====RECIBO=====")
if frances>0:
    print (f"Pão francês - quantidade: {frances} Total: R$ {valorFrances: }")
if integral>0:
    print (f"Pão integral - quantidade: {integral}Total: R$ {valorIntegral}")
if doceLiso>0:
    print (f"Pão doce Liso - quantidade: {doceLiso} Total: R$ {valorDoceLiso}")
if doceFarofa>0:
    print (f"Pão doce farora - quantidade: {doceFarofa} Total: R$ {valorDoceFarofa}")
if forma>0:
    print (f"Pão de forma - quantidade: {forma} Total: R$ {valorForma}")
valorTotal=valorFrances+valorIntegral+valorDoceLiso+valorDoceFarofa+valorForma
print(f"Valor total a pagar: R$ {valorTotal}")   
