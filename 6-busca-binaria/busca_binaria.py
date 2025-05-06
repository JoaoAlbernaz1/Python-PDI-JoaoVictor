def busca_binaria(lista, alvo):
    esq, dir = 0, len(lista) - 1
    
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        if lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return -1

numeros = [2, 4, 6, 8, 10]
print(busca_binaria(numeros, 8))  
print(busca_binaria(numeros, 5))  