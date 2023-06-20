ingredientes = {
    '1': 'pimenta',
    '2': 'legumes',
    '3': 'carne',
    '4': 'massas',
    '5': 'arroz'
}

caracteristicas = {
    'mexicana': ['pimenta', 'legumes', 'carne', 'massas', 'arroz'],
    'japonesa': ['arroz', 'legumes', 'carne', 'massas', 'pimenta'],
    'italiana': ['massas', 'legumes', 'carne', 'pimenta', 'arroz'],
    'indiana': ['arroz', 'massa', 'legumes', 'carne', 'pimenta'],
    'brasileira': ['legumes', 'carne', 'massas', 'arroz', 'pimenta'],
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

print(arrays_ingredientes['mexicana'])  # Saída: ['1', '2', '3', '4', '5']
print(arrays_ingredientes['japonesa'])  # Saída: ['5', '2', '3', '4', '1']
print(arrays_ingredientes['italiana'])  # Saída: ['4', '2', '3', '1', '5']
print(arrays_ingredientes['indiana'])  # Saída: ['5', '4', '2', '3', '1']
print(arrays_ingredientes['brasileira'])  # Saída: ['2', '3', '4', '5', '1']
print(arrays_ingredientes['churrascaria'])  # Saída: ['3', '1', '2', '4', '5']
