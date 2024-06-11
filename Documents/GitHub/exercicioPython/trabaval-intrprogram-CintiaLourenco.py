import random

# Gerar a chave do Euromilhões sorteada
numeros_sorteados = []  # Lista para armazenar os números sorteados
while len(numeros_sorteados) < 5:  # Loop para gerar 5 números sem repetição
    numero = random.randint(1, 50)  # Gerar um número aleatório entre 1 e 50
    if numero not in numeros_sorteados:  # Verificar se o número já foi sorteado
        numeros_sorteados.append(numero)  # Adicionar o número à lista de números sorteados
    #print(numeros_sorteados)
estrelas_sorteadas = []  # Lista para armazenar as estrelas sorteadas
while len(estrelas_sorteadas) < 2:  # Loop para gerar 2 estrelas sem repetição
    estrela = random.randint(1, 12)  # Gerar uma estrela aleatória entre 1 e 12
    if estrela not in estrelas_sorteadas:  # Verificar se a estrela já foi sorteada
        estrelas_sorteadas.append(estrela)  # Adicionar a estrela à lista de estrelas sorteadas
    #print(estrelas_sorteadas)
# Preencher a chave do Euromilhões pelo jogador
print("Digite 5 números entre 1 e 50:")
numeros_preenchidos = []  # Lista para armazenar os números escolhidos pelo jogador
while len(numeros_preenchidos) < 5:  # Loop para preencher 5 números sem repetição
    numero = int(input("Número: "))  # Solicitar ao jogador que insira um número
    if numero < 1 or numero > 50:  # Verificar se o número está dentro do intervalo válido
        print("Número inválido. Digite um número entre 1 e 50.")
    elif numero in numeros_preenchidos:  # Verificar se o número já foi escolhido
        print("Número repetido. Digite outro número.")
    else:
        numeros_preenchidos.append(numero)  # Adicionar o número à lista de números escolhidos

print("Digite 2 estrelas entre 1 e 12:")
estrelas_preenchidas = []  # Lista para armazenar as estrelas escolhidas pelo jogador
while len(estrelas_preenchidas) < 2:  # Loop para preencher 2 estrelas sem repetição
    estrela = int(input("Estrela: "))  # Solicitar ao jogador que insira uma estrela
    if estrela < 1 or estrela > 12:  # Verificar se a estrela está dentro do intervalo válido
        print("Estrela inválida. Digite uma estrela entre 1 e 12.")
    elif estrela in estrelas_preenchidas:  # Verificar se a estrela já foi escolhida
        print("Estrela repetida. Digite outra estrela.")
    else:
        estrelas_preenchidas.append(estrela)  # Adicionar a estrela à lista de estrelas escolhidas

# Verificar quantos números e estrelas foram acertados
acertos_numeros = 0  # Variável para contar os acertos de números
for numero in numeros_preenchidos:  # Loop para cada número escolhido pelo jogador
    if numero in numeros_sorteados:  # Verificar se o número escolhido está entre os sorteados
        acertos_numeros += 1  # Incrementar o contador de acertos de números

acertos_estrelas = 0  # Variável para contar os acertos de estrelas
for estrela in estrelas_preenchidas:  # Loop para cada estrela escolhida pelo jogador
    if estrela in estrelas_sorteadas:  # Verificar se a estrela escolhida está entre as sorteadas
        acertos_estrelas += 1  # Incrementar o contador de acertos de estrelas

# Imprimir o resultado dos acertos
print("Você acertou", acertos_numeros, "números e", acertos_estrelas, "estrelas.")

if acertos_numeros == 5 and acertos_estrelas == 2:
    print("Recompensa: 17.000.000€")
elif acertos_numeros == 5 and acertos_estrelas == 1:
    print("Recompensa: 200.738€")
elif acertos_numeros == 5 and acertos_estrelas == 0:
    print("Recompensa: 20.851€")
elif acertos_numeros == 4 and acertos_estrelas == 2:
    print("Recompensa: 1299€")
elif acertos_numeros == 3 and acertos_estrelas == 2:
    print("Recompensa: 57€")
elif acertos_numeros == 4 and acertos_estrelas == 0:
    print("Recompensa: 39€")
elif acertos_numeros == 2 and acertos_estrelas == 2:
    print("Recompensa: 14€")
elif acertos_numeros == 3 and acertos_estrelas == 1:
    print("Recompensa: 11€")
elif acertos_numeros == 3 and acertos_estrelas == 0:
    print("Recompensa: 9€")
elif acertos_numeros == 1 and acertos_estrelas == 2:
    print("Recompensa: 7€")
elif acertos_numeros == 2 and acertos_estrelas == 1:
    print("Recompensa: 6€")
elif acertos_numeros == 2 and acertos_estrelas == 0:
    print("Recompensa: 4€")
else:
    print("Não obteve prêmio")