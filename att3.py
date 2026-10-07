numero = int(input("Digite um número de 1 a 10: "))

if 1 <= numero <= 10:
    for multiplicador in range(1, 11):
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
else:
    print("Número inválido. Digite um valor de 1 a 10.")
