import Estatisticas as es

notas_alunos =  {
    'Rodrigo': [10, 7, 8],
    'João': [5, 6, 9],
    'Maria': [10, 9, 10],  
    'Julia': [10, 10, 10],
    'Rogéria': [10, 7, 8],
    'Joana': [6, 6, 9],
    'Mariana': [0, 9, 10],
    'Juliana': [1, 10, 10],
    'Roberto': [10, 7, 8],
    'Joaquim': [4, 6, 9],
    'Maria Lúcia': [6, 9, 10],
    'Josiane': [7, 10, 10],
}

lista_notas = []
lista_notas_por_aluno = []
labels_alunos = []


for alunos, notas in notas_alunos.items():
    lista_notas_por_aluno.append(notas)
    labels_alunos.append(alunos)
    for x in notas:
        lista_notas.append(x)


media_por_aluno = []

for i in lista_notas_por_aluno:
    media_por_aluno.append(es.calc_media(i))

#print ('Média_Alunos', media_por_aluno)

#print ('Lista de Notas', lista_notas)

# Média Geral da Turma
print (f'\nMedia Geral             : {es.calc_media(lista_notas):.2f}')
print (f'\nMediana Geral           : {es.calc_mediana(lista_notas):.2f}')
print (f'\nModa Geral              : {es.calc_moda(lista_notas):.2f}')
print (f'\nAmplitude Geral         : {es.calc_amplitude(lista_notas):.2f}')
print (f'\nVariancia Geral         : {es.calc_varianca(lista_notas):.2f}')
print (f'\nDesvio Padrão           : {es.calc_desvio_padrao(lista_notas):.2f}')

# Aluno com Maior Média

maior_media         = max(media_por_aluno)
aluno_maior_media   = media_por_aluno.index(maior_media)
menor_media         = min(media_por_aluno)
aluno_menor_media   = media_por_aluno.index(menor_media)


#print ('Info ',labels_alunos)

print (f'\nMaior Media {maior_media:.2f} foi do Aluno {labels_alunos[aluno_maior_media]}')
print (f'\nMenor Media {menor_media:.2f} foi do Aluno {labels_alunos[aluno_menor_media]}')
