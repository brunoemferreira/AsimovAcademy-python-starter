import os

print("=======")
operations = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponenciação",
}

while True:
    os.system("clear") # Limpa a Tela
    i = 0
    for op, name in operations.items(): # Carrega o dicionario na tela mostrando as opçoes
        print(i, ":", name)
        i += 1
    print("")
    print("Escolha a operação que deseja realizar:")    
    op = int(input()) # Recebee o que for digitado no terminal ( e converte para inteiro)
    op_string = list(operations.keys())[op] # armazena na string o que está na posição do dicionario

    print("")
    print("{} escolhida.".format(op_string))
    print("")
    print("Qual o primeiro valor?")
    v1 = float(input())
    print("Qual o segundo valor?")
    v2 = float(input())

    # chaveia a operaçao que vai ser feitaa partir do valor escolhido
    if op == 0:
        result = v1 + v2
    elif op == 1:  
         result = v1 - v2 
    elif op == 2:  
         result = v1 * v2 
    elif op == 3:  
         result = v1 / v2           
    elif op == 4:  
         result = v1 ^ v2      

    print("")
    print("{} {} {} = {}".format(v1, op_string,v2, result))     
    print("")
    print("=======")

    print("Deseja fazer mais alguma operação? (Digite 1 para Sair)")
    comando = int(input())
    if comando == 1:
         break