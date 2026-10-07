boletim = {}
while True:
    adicionar_aluno = input("Deseja adicionar um aluno? (s/n): ")
    if adicionar_aluno.lower() == 's':
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        boletim[nome] = nota
    elif adicionar_aluno.lower() == 'n':
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")

for nome, nota in boletim.items():
    if nota >= 6.0:
        print(f"{nome} está Aprovado(a) com nota {nota}.")
    else:
        print(f"{nome} está Reprovado(a) com nota {nota}.")