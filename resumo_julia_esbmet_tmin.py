###################################################################################################
# Script que monitora a relação de TMIN nas Cidades de Joinville, Blumenau e Florianópolis        #
# (Projeto Dengue)                                                                                #
#                                                                                                 #
# Autor: Júlia Barreto da Silva                                                                   #
#                                                                                                 #
# LaCAC/Multlab/IFSC - Florianópolis  --- Data: 3 de abril de 2025                                # #                                                                                                 #
###################################################################################################

## Importando Bibliotecas ##

import pandas as pd                 
import matplotlib.pyplot as plt     
import seaborn as sns               
import numpy as np                  


## Abrindo Arquivos ##

url = "https://raw.githubusercontent.com/matheusf30/dados_dengue/refs/heads/main/tmed_se.csv" #raw
casos = pd.read_csv(url)
print(casos.head())
casos.head() # Diferença na apresentação gráfica
# Everton - TMIN
# Bia - TMED
# Júlia - CASOS TMED E PREC
# Domênica - PREC (GFS)
# Murilo - PREC (MERGE) / CASOS
# Carol - FOCOS

# Analisando Variáveis

print(casos.info())             #Exibe informações gerais sobre o DataFrame, como o número de entradas, colunas, e tipos de dados.
print("="*50)                   
print(casos.dtypes)             #Exibe os tipos de dados de cada coluna.
print("="*50)
print(casos.describe())         #Exibe estatísticas descritivas das colunas numéricas, como média, desvio padrão, valor mínimo e máximo, etc.

# Pré-processamento

casos["Semana"] = pd.to_datetime(casos["Semana"])
print(casos.dtypes)

municipios = casos.columns[1:]  #Extrai todos os nomes de colunas, exceto a primeira (presumivelmente, "Semana"), para que municipios contenha os nomes das cidades.
print(municipios)

# Lista das cidades que você deseja manter (todas em maiúsculas)
cidades_desejadas = ["FLORIANÓPOLIS", "JOINVILLE", "BLUMENAU"]

# Primeiro Laço: Série temporal para as cidades desejadas
for municipio in cidades_desejadas:
	#if municipio.upper() in [cidade.upper() for cidade in cidades_desejadas]:  # Verifica se o município está na lista de cidades desejadas
	print(f"Gerando gráfico para: {municipio}")  # Adicionando mensagem de depuração
	plt.figure(figsize=(10, 6))
	plt.plot(casos["Semana"], casos[municipio])
	plt.title(f"CASOS DE DENGUE, MUNICÍPIO DE {municipio}")
	plt.xlabel("Série Histórica (Semanas Epidemiológicas)")
	plt.ylabel("Número de Casos de dengue")
	plt.grid(True)  # Adiciona uma grade ao gráfico
	plt.gca().patch.set_facecolor("honeydew")  # Altera o fundo do gráfico para a cor 'honeydew'
	plt.show()

plt.figure(figsize=(10, 6))
plt.plot(casos["Semana"], casos["FLORIANÓPOLIS"], label= "Florianópolis")
plt.plot(casos["Semana"], casos["JOINVILLE"], label= "Joinville")
plt.plot(casos["Semana"], casos["BLUMENAU"], label= "Blumenau")
plt.title(f"Análise dos Casos de Dengue nas Cidades Catarinenses com Aumento Significativo")
plt.xlabel("Série Histórica (Semanas Epidemiológicas)")
plt.ylabel("Número de Casos de dengue")
plt.legend()
plt.grid(True)  # Adiciona uma grade ao gráfico
plt.gca().patch.set_facecolor("honeydew")  # Altera o fundo do gráfico para a cor 'honeydew'
plt.show()

'''
#for municipio in municipios:    #Inicia um laço de repetição para iterar sobre todos os municípios.
  max = casos[municipio].max()  #Calcula o valor máximo de casos de dengue para cada município.
  min = casos[municipio].min()  #Calcula o valor mínimo de casos de dengue para cada município.
  soma = casos[municipio].sum() #Calcula a soma total de casos de dengue para cada município.
  print("=" * 50)
  print(f"Analisando o município: {municipio}")
  print("~" * 50)
  print(f"O valor máximo é: {max}")
  print("~" * 50)
  print(f"O valor mínimo é: {min}")
  print("~" * 50)
  print(f"A soma da série histórica é: {soma}")
'''
max = {}
min = {}
soma = {}
for municipio in municipios:
  max[municipio] = casos[municipio].max()
  min[municipio] = casos[municipio].min()
  soma[municipio] = casos[municipio].sum()
print(max)
print(min)
print(soma)

df_max = pd.DataFrame(list(max.items()), columns=['Município', 'Máximo'])
df_min = pd.DataFrame(list(min.items()), columns=['Município', 'Mínimo'])
df_soma = pd.DataFrame(list(soma.items()), columns=['Município', 'Soma'])
print(df_max)
print(df_min)
print(df_soma)

df_max = df_max.sort_values(by = "Máximo", ascending = False)
df_min = df_min.sort_values(by = "Mínimo", ascending = True)
df_soma = df_soma.sort_values(by = "Soma", ascending = False)
df_soma_asc = df_soma.sort_values(by = "Soma", ascending = True)
print(df_max)
print(df_min)
print(df_soma)
print(df_soma_asc)

"""
# Visualização Gráfica

## Barras

### Máximos
"""

#plt.figure(figsize=(10, 6))
#plt.bar(df_max["Município"], df_max["Máximo"])
#plt.title("VALOR MÁXIMO DOS CASOS DE DENGUE EM SANTA CATARINA")
#plt.xlabel("Municípios Catarinenses")
#plt.xticks(rotation = 90)
#plt.ylabel("Número Máximo de Casos de dengue")
#plt.show()

#principais_max = df_max.head(20)    #Seleciona os 20 municípios com os maiores valores máximos de casos.
principais_max = df_max.head(3)      #Seleciona os 3 municípios com os maiores valores máximos de casos. (Joinville, Blumenau e Floripa)
print(principais_max)
plt.figure(figsize=(10, 6))
plt.bar(principais_max["Município"], principais_max["Máximo"])
plt.title("VALOR MÁXIMO DOS CASOS DE DENGUE EM SANTA CATARINA")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número Máximo de Casos de dengue")
plt.gca().patch.set_facecolor("honeydew")
plt.show()                           #Cria um gráfico de barras

# """### Mínimos"""

# plt.figure(figsize=(10, 6))
# plt.bar(df_min["Município"], df_min["Mínimo"])
# plt.title("VALOR MÍNIMO DOS CASOS DE DENGUE EM SANTA CATARINA")
# plt.xlabel("Municípios Catarinenses")
# plt.xticks(rotation = 90)
# plt.ylabel("Número Mínimo de Casos de dengue")
# plt.show()

# principais_min = df_min.head(20)
# print(principais_min)
# plt.figure(figsize=(10, 6))
# plt.bar(principais_min["Município"], principais_min["Mínimo"])
# plt.title("VALOR MÍNIMO DOS CASOS DE DENGUE EM SANTA CATARINA")
# plt.xlabel("Municípios Catarinenses")
# plt.xticks(rotation = 90)
# plt.ylabel("Número Mínimo de Casos de dengue")
# plt.gca().patch.set_facecolor("honeydew")
# plt.show()

# Adicionando visualização para Temperatura
# plt.figure(figsize=(10, 6))
# plt.bar(df_max["Município"], df_max["Max_Temperature"])
# plt.title("VALOR MÁXIMO DA TEMPERATURA MÉDIA")
# plt.xlabel("Municípios")
# plt.xticks(rotation = 90)
# plt.ylabel("Temperatura Máxima (°C)")
# plt.show()

# Adicionando visualização para Precipitação
# plt.figure(figsize=(10, 6))
# plt.bar(df_max["Município"], df_max["Max_Precipitation"])
# plt.title("VALOR MÁXIMO DA PRECIPITAÇÃO")
# plt.xlabel("Municípios")
# plt.xticks(rotation = 90)
# plt.ylabel("Precipitação Máxima (mm)")
#plt.show()


### Acumulado

#### Ascendente

'''
plt.figure(figsize=(10, 6))
plt.bar(df_soma_asc["Município"], df_soma_asc["Soma"])
plt.title("SOMA HISTÓRICA DOS CASOS DE DENGUE EM SANTA CATARINA (Menores Registros)")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número de Casos de dengue")
plt.show()

principais_soma_asc = df_soma_asc.head(50)
print(principais_soma_asc)
plt.figure(figsize=(10, 6))
plt.bar(principais_soma_asc["Município"], principais_soma_asc["Soma"])
plt.title("SOMA HISTÓRICA DOS CASOS DE DENGUE EM SANTA CATARINA (Menores Registros)")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número de Casos de dengue")
plt.gca().patch.set_facecolor("honeydew")
plt.show()
'''
#### Descendente

#plt.figure(figsize=(10, 6))
#plt.bar(df_soma["Município"], df_soma["Soma"])
#plt.title("SOMA HISTÓRICA DOS CASOS DE DENGUE EM SANTA CATARINA")
#plt.xlabel("Municípios Catarinenses")
#plt.xticks(rotation = 90)
#plt.ylabel("Número de Casos de dengue")
#plt.show()

#principais_soma = df_soma.head(20)
principais_soma = df_soma.head(3)
print(principais_soma)
plt.figure(figsize=(10, 6))
plt.bar(principais_soma["Município"], principais_soma["Soma"])
plt.title("SOMA HISTÓRICA DOS CASOS DE DENGUE EM SANTA CATARINA")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número de Casos de dengue")
plt.gca().patch.set_facecolor("honeydew")
plt.show()

## Série Temporal




'''
for municipio in municipios:
  plt.figure(figsize=(10, 6))
  plt.plot(casos["Semana"], casos[municipio])
  plt.title(f"CASOS DE DENGUE, MUNICÍPIO DE {municipio}")
  plt.xlabel("Série Histórica (Semanas Epidemiológicas)")
  plt.ylabel("Número de Casos de dengue")
  plt.show()

sem_tempo = casos.drop(columns = "Semana")
for municipio in municipios:
  plt.figure(figsize=(10, 6))
  plt.plot(casos["Semana"], casos[municipio])
  plt.title(f"CASOS DE DENGUE, MUNICÍPIO DE {municipio}")
  plt.xlabel("Série Histórica (Semanas Epidemiológicas)")
  plt.ylabel("Número de Casos de dengue")
  plt.grid(True)
  plt.gca().set_ylim(0, sem_tempo.max().max())
  plt.gca().patch.set_facecolor("honeydew")
  plt.show()

sem_tempo = casos.drop(columns = "Semana")
for municipio in principais_max["Município"]:
  plt.figure(figsize=(10, 6))
  plt.plot(casos["Semana"], casos[municipio])
  plt.title(f"CASOS DE DENGUE, MUNICÍPIO DE {municipio}")
  plt.xlabel("Série Histórica (Semanas Epidemiológicas)")
  plt.ylabel("Número de Casos de dengue")
  plt.grid(True)
  plt.gca().set_ylim(0, sem_tempo.max().max())
  plt.gca().patch.set_facecolor("honeydew")
  plt.show()

sem_tempo = casos.drop(columns = "Semana")
for municipio in principais_soma["Município"]:
  plt.figure(figsize=(10, 6))
  plt.plot(casos["Semana"], casos[municipio])
  plt.title(f"CASOS DE DENGUE, MUNICÍPIO DE {municipio}")
  plt.xlabel("Série Histórica (Semanas Epidemiológicas)")
  plt.ylabel("Número de Casos de dengue")
  plt.grid(True)
  plt.gca().set_ylim(0, sem_tempo.max().max())
  plt.gca().patch.set_facecolor("honeydew")
  plt.show()
'''
