from db import *

# Ordena o dicionário por valores calóricos em ordem decrescente
frutas_ordenadas = dict(sorted(frutas.items(), key=lambda item: item[1], reverse=True))

# Exibe as frutas ordenadas
print("""
-------------------
Calorias por 100g
-------------------
""")
for item, fruta in enumerate(frutas_ordenadas):
    print(f"{item+1}º {fruta} : {frutas_ordenadas[fruta]} calorias")
