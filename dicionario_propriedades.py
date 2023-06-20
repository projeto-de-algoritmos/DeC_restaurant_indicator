ingredientes = {
    'A': 'pimenta',
    'B': 'legumes',
    'C': 'carne',
    'D': 'massas',
    'E': 'arroz'
}

caracteristicas = {
    'mexicana': ['pimenta', 'legumes', 'carne', 'massas', 'arroz'],
    'japonesa': ['arroz', 'legumes', 'carne', 'massas', 'pimenta'],
    'italiana': ['massas', 'legumes', 'carne', 'pimenta', 'arroz'],
    'indiana': ['massas', 'arroz', 'legumes', 'carne', 'pimenta'],
    'brasileira': ['legumes', 'carne', 'massas', 'pimenta', 'arroz'],
    'churrascaria': ['carne', 'pimenta', 'legumes', 'massas', 'arroz']
}

arrays_ingredientes = {}

for restaurante, ingredientes_restaurante in caracteristicas.items():
    array_indices = []
    for ingrediente in ingredientes_restaurante:
        for indice, nome_ingrediente in ingredientes.items():
            if nome_ingrediente == ingrediente:
                array_indices.append(indice)
                break
    arrays_ingredientes[restaurante] = array_indices

print(arrays_ingredientes['mexicana'])  # Saída: ['A', 'B', 'C', 'D', 'E']
print(arrays_ingredientes['japonesa'])  # Saída: ['E', 'B', 'C', 'D', 'A']
print(arrays_ingredientes['italiana'])  # Saída: ['D', 'B', 'C', 'A', 'E']
print(arrays_ingredientes['indiana'])  # Saída: ['D', 'E', 'B', 'C', 'A']
print(arrays_ingredientes['brasileira'])  # Saída: ['B', 'C', 'D', 'A', 'E']
print(arrays_ingredientes['churrascaria'])  # Saída: ['C', 'A', 'B', 'D', 'E']
