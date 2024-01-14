from db import *

for i in range(3):
    aluno = {
        "Nome": str(input("Digite o nome do novo aluno:")),
        "Idade": int(input("Digite a idade do novo aluno: ")),
        "Turma": str(input("Digite a turma: ")),
        "CPF": int(input("Digite o CPF: "))
    }
    alunos.append(aluno)
    ln(30)



for aluno in alunos:
    print(f"""
    Nome: {aluno["Nome"]}
    Idade: {aluno["Idade"]}
    """)
    ln(30)