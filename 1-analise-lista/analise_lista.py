def analisar_lista(numeros):
    if not numeros:
        raise ValueError("A lista não pode estar vazia")
    
  
    maior = max(numeros)
    menor = min(numeros)
    soma = sum(numeros)
    media = soma / len(numeros)


    lista_ordenada = numeros[:]
    for i in range(len(lista_ordenada)):
        for j in range(i + 1, len(lista_ordenada)):
            if lista_ordenada[i] > lista_ordenada[j]:
                lista_ordenada[i], lista_ordenada[j] = lista_ordenada[j], lista_ordenada[i]
    
    return {
        'maior': maior,
        'menor': menor,
        'media': media,
        'lista_ordenada': lista_ordenada
    }

numeros = [10, 20, 30, 40, 50]


resultado = analisar_lista(numeros)

print("\n" + "="*40)
print("🌟 ANÁLISE COMPLETA DA LISTA NUMÉRICA 🌟")
print("="*40)
print(f"🔢 Lista original: {numeros}")
print(f"🔺 Maior número: {resultado['maior']}")
print(f"🔻 Menor número: {resultado['menor']}")
print(f"📊 Média calculada: {resultado['media']:.2f}")
print(f"🔼 Lista ordenada: {resultado['lista_ordenada']}")
print("="*40 + "\n")