# Exercicio 01 da Aula 07

import Estatisticas as es

empresa1 = [2500, 2800, 3000, 9500, 12000]

empresa2 = [5000, 5200, 5300, 5400, 5500]

empresa3 = [1000, 2000, 8000, 15000, 20000]

empresa4 = [3500, 4000, 4200, 4300, 6000]

empresa5 = [1200, 1500, 1800, 2500, 10000]


lista_empresas = []

lista_empresas.append(empresa1)
lista_empresas.append(empresa2)
lista_empresas.append(empresa3)
lista_empresas.append(empresa4)
lista_empresas.append(empresa5)
cont = len(lista_empresas)

j = 1

for i in lista_empresas:
   print (f'\nEmpresa {j}')
   print (f'Media Salários        : {es.calc_media(i):.2f}')
   print (f'Moda                  : {es.calc_moda(i):.2f}')
   print (f'Amplitude             : {es.calc_amplitude(i):.2f}')
   print (f'Variancia             : {es.calc_varianca(i):.2f}')
   print (f'Desvio Padrão         : {es.calc_desvio_padrao(i):.2f}')
   j += 1

media_empresas = []
moda_empresas = []
mediana_empresas = []
desvio_padrao_empresas = []


# Resultados das Empresa 1

print ('\nEmpresas 1')
print (f'Media Salários        : {es.calc_media(empresa1):.2f}')
print (f'Moda                  : {es.calc_moda(empresa1):.2f}')
print (f'Amplitude             : {es.calc_amplitude(empresa1):.2f}')
print (f'Variancia             : {es.calc_varianca(empresa1):.2f}')
print (f'Desvio Padrão         : {es.calc_desvio_padrao(empresa1):.2f}')


# Resultados das Empresa 2
print ('\nEmpresas 2')
print (f'Media Salários        : {es.calc_media(empresa2):.2f}')
print (f'Moda                  : {es.calc_moda(empresa2):.2f}')
print (f'Amplitude             : {es.calc_amplitude(empresa2):.2f}')
print (f'Variancia             : {es.calc_varianca(empresa2):.2f}')
print (f'Desvio Padrão         : {es.calc_desvio_padrao(empresa2):.2f}')

# Resultados das Empresa 3
print ('\nEmpresas 3')
print (f'Media Salários        : {es.calc_media(empresa3):.2f}')
print (f'Moda                  : {es.calc_moda(empresa3):.2f}')
print (f'Amplitude             : {es.calc_amplitude(empresa3):.2f}')
print (f'Variancia             : {es.calc_varianca(empresa3):.2f}')
print (f'Desvio Padrão         : {es.calc_desvio_padrao(empresa3):.2f}')


# Resultados das Empresa 4
print ('\nEmpresas 4')
print (f'Media Salários        : {es.calc_media(empresa4):.2f}')
print (f'Moda                  : {es.calc_moda(empresa4):.2f}')
print (f'Amplitude             : {es.calc_amplitude(empresa4):.2f}')
print (f'Variancia             : {es.calc_varianca(empresa4):.2f}')
print (f'Desvio Padrão         : {es.calc_desvio_padrao(empresa4):.2f}')

# Resultados das Empresa 5
print ('\nEmpresas 5')
print (f'Media Salários        : {es.calc_media(empresa5):.2f}')
print (f'Moda                  : {es.calc_moda(empresa5):.2f}')
print (f'Amplitude             : {es.calc_amplitude(empresa5):.2f}')
print (f'Variancia             : {es.calc_varianca(empresa5):.2f}')
print (f'Desvio Padrão         : {es.calc_desvio_padrao(empresa5):.2f}')
