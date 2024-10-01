menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
valor_limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input (menu)

    if opcao == "d":
        valor = float(input("Quanto você quer depositar?  "))

        if valor >0:        #valor do deposito somente positivo
            saldo += valor  #armazenando valor digitado
            extrato += f"Deposito: R$ {valor:10.2f}\n"
            print ("Deposito realizado com sucesso!")
    
        else:              #caso o valor digitado seja negativo
            print ("Operacao invalida! Digite um valor positivo")
    
    elif opcao == "s":
        valor = float(input("Quanto voce quer sacar?  "))

        excedeu_saldo =  valor > saldo
        excedeu_limite = valor > valor_limite_saque
        excedeu_saque = numero_saques >=LIMITE_SAQUES

        if excedeu_saldo:
            print ("Falha! Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Falha! O valor do saque excede o limite!")
        
        elif excedeu_saque:
            print("Falha! Numero maximo de saques diarios excedidos!")
                  
        elif valor > 0:
            saldo -=valor
            extrato += f"Saque:    R$ {valor:10.2f}\n"
            numero_saques +=1  #contador para o numero de vezes que ocorreu o saque

        else:
            print("Falha! O valor informado e invalido!")

    elif opcao == "e":
        print ("\n=======Meu extrato======")
        print("Nao foram realizadas movimentacoes" if extrato=="" else extrato)
        print(f"\nSaldo:    R$ {saldo:10.2f}")
        print ("=========Fim do extrato========")

    elif opcao == "q":
        print("Obrigado por usar nosso sistema!")
        break
              
    else:
        print ("Operacao invalida, por favor selecione novamente a operacao desejada:")






















                          

