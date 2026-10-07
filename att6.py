
dicionario notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}
soma = 0
for nota in dicionario.values():
    soma += nota
media = soma / len(dicionario)
print(f"A média geral da turma é: {media:.2f}")
