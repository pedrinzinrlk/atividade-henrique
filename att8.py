lista_produtos = [
    {"nome": "Produto A", "preco": 30.0},
    {"nome": "Produto B", "preco": 60.0},
    {"nome": "Produto C", "preco": 80.0}
]
for produto in lista_produtos:
    if produto["preco"] > 50.0:
        print(produto["nome"]) 