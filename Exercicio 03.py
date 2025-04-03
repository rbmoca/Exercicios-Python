# A empresa de cartões de crédito enfrenta uma crescente perda de clientes e 
# deseja compreender os fatores que levam ao cancelamento dos cartões. 
# Para isso, realize uma análise de dados a partir de uma planilha contendo informações dos clientes, 
# com o objetivo de identificar padrões e traçar e possivel motivo da perda dos clientes.

# Utilize media moda mediana desvio padrão.

import Estatisticas as es

clientes = [
{"Idade": 45, "Limite": 12691, "Meses_cliente": 39, "Taxa_utilizacao": 0.061},
{"Idade": 49, "Limite": 8256, "Meses_cliente": 44, "Taxa_utilizacao": 0.105},
{"Idade": 51, "Limite": 3418, "Meses_cliente": 36, "Taxa_utilizacao": 0},
{"Idade": 40, "Limite": 3313, "Meses_cliente": 34, "Taxa_utilizacao": 0.76},
{"Idade": 40, "Limite": 4716, "Meses_cliente": 21, "Taxa_utilizacao": 0},
{"Idade": 44, "Limite": 4010, "Meses_cliente": 36, "Taxa_utilizacao": 0.311},
{"Idade": 51, "Limite": 34516, "Meses_cliente": 46, "Taxa_utilizacao": 0.066},
{"Idade": 32, "Limite": 29081, "Meses_cliente": 27, "Taxa_utilizacao": 0.048},
{"Idade": 37, "Limite": 22352, "Meses_cliente": 36, "Taxa_utilizacao": 0.113},
{"Idade": 48, "Limite": 11656, "Meses_cliente": 36, "Taxa_utilizacao": 0.144},
{"Idade": 42, "Limite": 6748, "Meses_cliente": 31, "Taxa_utilizacao": 0.217},
{"Idade": 65, "Limite": 9095, "Meses_cliente": 54, "Taxa_utilizacao": 0.174},
]

lista_idades    = []
lista_limites   = []
lista_meses     = []
taxa_utilizacao = []

# Extração das Listas
for i in clientes:
    lista_idades.append(i.get("Idade"))
    lista_limites.append(i.get("Limite"))
    lista_meses.append(i.get("Meses_cliente"))
    taxa_utilizacao.append(i.get("Taxa_utilizacao"))


# Análise das Informações

print(f'\nMédia de Idade    - {es.calc_media(lista_idades):.2f}')
print(f'Média de Limite   - {es.calc_media(lista_limites):.2f}')
print(f'Média de Meses    - {es.calc_media(lista_meses):.2f}')
print(f'Média de Taxa Uso - {es.calc_media(taxa_utilizacao):.2f}')

print(f'\n\nModa Idade    - {es.calc_moda(lista_idades):.2f}')
print(f'Moda de Limite   - {es.calc_moda(lista_limites):.2f}')
print(f'Moda de Meses    - {es.calc_moda(lista_meses):.2f}')
print(f'Moda de Taxa Uso - {es.calc_moda(taxa_utilizacao):.2f}')

print(f'\n\nMediana de Idade    - {es.calc_mediana(lista_idades):.2f}')
print(f'Mediana de Limite   - {es.calc_mediana(lista_limites):.2f}')
print(f'Mediana de Meses    - {es.calc_mediana(lista_meses):.2f}')
print(f'Mediana de Taxa Uso - {es.calc_mediana(taxa_utilizacao):.2f}')

print(f'\n\nDesvio Padrão de Idade    - {es.calc_desvio_padrao(lista_idades):.2f}')
print(f'Desvio Padrão de Limite   - {es.calc_desvio_padrao(lista_limites):.2f}')
print(f'Desvio Padrão de Meses    - {es.calc_desvio_padrao(lista_meses):.2f}')
print(f'Desvio Padrão de Taxa Uso - {es.calc_desvio_padrao(taxa_utilizacao):.2f}')
