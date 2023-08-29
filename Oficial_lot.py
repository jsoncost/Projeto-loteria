import random

contador_listas = 0

while True:
    Diga = input('tecle "Enter" para ver a lista ou tecle "s" para [s]air')

    if Diga == 's':
        print('Saindo do Programa')
        break

    lista_numeros = list(range(1, 26))

    # Permitir que o usuário exclua números da lista
    numeros_excluidos = input('Digite os números para excluir da lista separados por vírgula: ')
    numeros_excluidos = numeros_excluidos.split(',')
    numeros_excluidos = [int(num) for num in numeros_excluidos if num.isdigit()]

    for num in numeros_excluidos:
        if num in lista_numeros:
            lista_numeros.remove(num)
        else:
            print('Número inválido ou não encontrado na lista.')

    # Definir a quantidade de números que podem se repetir
    quantidade_repeticao = 0

    # Inicializar a lista de números aleatórios
    numeros_aleatorios = []

    # Gerar números aleatórios permitindo que alguns se repitam e outros não
    for i in range(15):
        if i < quantidade_repeticao:
            # Permitir que os primeiros n números gerados possam se repetir
            numero_aleatorio = random.choice(lista_numeros)
        else:
            # Garantir que os próximos números gerados não se repitam
            numeros_disponiveis = list(set(lista_numeros) - set(numeros_aleatorios))
            if len(numeros_disponiveis) == 0:
                break
            numero_aleatorio = random.choice(numeros_disponiveis)
        numeros_aleatorios.append(numero_aleatorio)

    # Ordenar a lista de números aleatórios em ordem crescente
    numeros_aleatorios.sort()

    # Imprimir os números aleatórios gerados
    print(numeros_aleatorios)

    # Gerar o padrão baseado nas diferenças entre os números gerados
    diferencas = [numeros_aleatorios[i+1] - numeros_aleatorios[i] for i in range(len(numeros_aleatorios)-1)]
    padrao = ','.join(str(d) for d in diferencas)
    print(f"Padrão: {padrao}")

    # Permitir que o usuário edite o padrão antes de gerar a próxima lista de números aleatórios
    novo_padrao = input('Digite o novo padrão ou pressione Enter para manter o mesmo padrão: ')
    if novo_padrao:
        novo_padrao = novo_padrao.split(',')
        novo_padrao = [int(num) for num in novo_padrao if num.isdigit()]
        if len(novo_padrao) == len(diferencas):
            numeros_aleatorios = [numeros_aleatorios[0]]
            for i in range(len(novo_padrao)):
                novo_numero = numeros_aleatorios[i] + novo_padrao[i]
                numeros_aleatorios.append(novo_numero)
            print(numeros_aleatorios)
        else:
            print('O novo padrão deve ter o mesmo número de elementos que o padrão anterior.')

    contador_listas += 1
    if contador_listas % 5 == 0:
        pausa = input('geradas 5 listas. Pressione Enter para continuar.')


