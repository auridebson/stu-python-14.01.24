from db import *
import random

# # Ordena o dicionário por valores calóricos em ordem decrescente
# frutas_ordenadas = dict(sorted(frutas.items(), key=lambda item: item[1], reverse=True))

# # Exibe as frutas ordenadas
# print("""
# -------------------
# Calorias por 100g
# -------------------
# """)
# for item, fruta in enumerate(frutas_ordenadas):
#     print(f"{item+1}º {fruta} : {frutas_ordenadas[fruta]} calorias")

def AddCart():
    nome = str(input("Digite o nome do cliente: "))
    cpf = int(input("Digite o CPF: "))
    valor = float(input("Digite o valor da compra: "))
    compra = {"Nome":nome, "CPF":cpf, "Valor":valor}
    clientes.append(compra)


def sorteia():
    sorteado = random(clientes)
    return sorteado

while True:
    menu = int(input(""""
    Escolha uma opção:
        1 - Inserir nova venda
        2 - Sair
    """))
    match menu:
        case 1:
            AddCart()
        case 2:
            break

cliSorteado = random.randint(0,len(clientes)-1)

ln(50)
print(f"""
    PARABÉNS {clientes[cliSorteado]["Nome"]}, 
    você que tem o CPF {clientes[cliSorteado]["CPF"]} e 
    última compra no valor de R$ {clientes[cliSorteado]["Valor"]} foi o grande felizardo!""")
ln(50)

i = 0
for cliente in clientes:
    if cliente["Valor"] > i:
        nomeMax = cliente["Nome"]
        valorMax = cliente["Valor"]


print(f"""
    A maior compra foi de {nomeMax} no valor de R$ {valorMax}.
    """)
ln(50)