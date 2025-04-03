#  Crie um dicionário com valores de 30 produtos

import Estatisticas as es

produtos = {
   "Produto_1": 10.00,
   "Produto_2": 11.00,
   "Produto_3": 12.00,
   "Produto_4": 13.00,
   "Produto_5": 14.00,
   "Produto_6": 15.00,
   "Produto_7": 15.00,
   "Produto_8": 14.00,
   "Produto_9": 13.00,
   "Produto_10":12.00,
   "Produto_11":10.00,
   "Produto_12":21.00,
   "Produto_13":12.00,
   "Produto_14":23.00,
   "Produto_15":24.00,
   "Produto_16":25.00,
   "Produto_17":26.00,
   "Produto_18":23.00,
   "Produto_19":30.00,
   "Produto_20":12.00,
   "Produto_21":30.00,
   "Produto_22":31.00,
   "Produto_23":32.00,
   "Produto_24":43.00,
   "Produto_25":54.00,
   "Produto_26":5.00,
   "Produto_27":15.00,
   "Produto_28":24.00,
   "Produto_29":23.00,
   "Produto_30":12.00
}

lista_valores    = []
# print ('Dicionario', produtos)

for valor in produtos.values():
    lista_valores.append(valor)


print ('Lista de Valors', lista_valores)

# Análise das Informações

print(f'\nMédia de Valores     - {es.calc_media(lista_valores):.2f}')
print(f'\nMediana de Valores   - {es.calc_mediana(lista_valores):.2f}')
print(f'\nModa de Valores      - {es.calc_moda(lista_valores):.2f}')
print(f'\nVariância de Valores - {es.calc_varianca(lista_valores):.2f}')
print(f'\nDesvio Padrão        - {es.calc_desvio_padrao(lista_valores):.2f}')
print(f'\nAmplitude de Valores - {es.calc_amplitude(lista_valores):.2f}')


# 1 - Qual é a diferença entre a média e mediana?
# A média é a soma de todos os valores de um conjunto de dados dividido 
# pelo número total de valores, 
# enquanto a mediana é o valor que está no meio do conjunto de dados ordenado

# 2 - Por que a moda é importante?
# porque representa o valor mais frequente num conjunto de dados, 
# fornecendo uma visão útil da tendência central, 
# especialmente em dados categóricos ou quando há valores extremos que influenciam a média. 

# 3 - Qual é o significado da variância?
# Diz respeito à distância que um valor médio apresenta do demais valores 
# de um conjunto de dados.
#
# 4 - Como o desvio padrão relaciona-se com a variância?
# O desvio padrão é a raiz quadrada da variância, ou seja, a variância é o quadrado do desvio padrão. 
# Ambos são medidas de dispersão que indicam quão espalhados os dados estão em relação à média. 

