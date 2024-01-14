from db import *

# Exemplo de acesso aos valores do dicionário
for fruta, info_nutricional in frutas.items():
    ln(30)
    for valor in fruta:
        print(valor.nome)
    print(f"{fruta}: {info_nutricional}")
