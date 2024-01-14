from db import *

# Ordena o dicionário por valores calóricos em ordem decrescente
frutas_calorias_ordenadas = dict(sorted(frutas_calorias.items(), key=lambda item: item[1], reverse=True))

# Exibe as frutas ordenadas
for fruta, calorias in frutas_calorias_ordenadas.items():
    print(f"{fruta}: {calorias} calorias por 100g")
