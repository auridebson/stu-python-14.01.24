import random
from db import *
import re

while True:
    cpf = input("Digite o CPF: ")
    cpff = re.sub(r'[^0-9]', '', cpf)
    print(type(cpf))
    if len(cpf) < 11 and len(cpf) > 14:
        print("Digite um CPF válido!")
    elif cpf is not int:
        print("Digite um número inteiro válido!")
    else:
        int(cpf)
        break