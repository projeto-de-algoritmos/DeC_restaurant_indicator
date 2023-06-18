ingredientes = {
    1: 'pimenta',
    2: 'legumes',
    3: 'carne',
    4: 'massas',
    5: 'arroz'
}

caracteristicas = {
    'mexicana': ['pimenta', 'legumes', 'carne', 'massas', 'arroz'],
    'japonesa': ['arroz', 'legumes', 'carne', 'massas', 'pimenta'],
    'italiana': ['massas', 'legumes', 'carne', 'pimenta', 'arroz'],
    'indiana': ['massas', 'arroz', 'legumes', 'carne', 'pimenta'],
    'brasileira': ['legumes', 'carne', 'massas', 'pimenta', 'arroz'],
    'churrascaria': ['carne', 'pimenta', 'legumes', 'massas', 'arroz']
}


##Transformando o dicionario em array de id
mexicana = [id for id in ingredientes if ingredientes[id] in caracteristicas['mexicana']]
brasileira = [id for id in ingredientes if ingredientes[id] in caracteristicas['brasileira']]
churrascaria = [id for id in ingredientes if ingredientes[id] in caracteristicas['churrascaria']]
italiana = [id for id in ingredientes if ingredientes[id] in caracteristicas['italiana']]
indiana = [id for id in ingredientes if ingredientes[id] in caracteristicas['indiana']]
japonesa = [id for id in ingredientes if ingredientes[id] in caracteristicas['japonesa']]

# print('Array da culinária mexicana:', mexicana)
# print('Array da culinária brasileira:', brasileira)
# print('Array da culinária churrascaria:', churrascaria)
# print('Array da culinária italiana:', italiana)
# print('Array da culinária indiana:', indiana)
# print('Array da culinária japonesa:', japonesa)
