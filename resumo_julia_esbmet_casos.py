###################################################################################################
# Script que monitora a relação dos CASOS de Dengue nas Cidades de Joinville, Blumenau e          #
#Florianópolis (Projeto Dengue)                                                                   #
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

url = "https://raw.githubusercontent.com/matheusf30/dados_dengue/refs/heads/main/casos_dive_pivot_total.csv" #raw
casos = pd.read_csv(url)
print(casos.head())
casos.head() # Diferença na apresentação gráfica

## Analisando Variáveis ##

casos["Semana"] = pd.to_datetime(casos["Semana"])
print(casos.dtypes)

municipios = casos.columns[1:]  #Extrai todos os nomes de colunas, exceto a primeira (presumivelmente, "Semana"), para que municipios contenha os nomes das cidades.
print(municipios)

cidades_desejadas = ["FLORIANÓPOLIS", "JOINVILLE", "BLUMENAU"]

for municipio in cidades_desejadas:    #Inicia um laço de repetição para iterar sobre todos os municípios.
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

max = {}
min = {}
soma = {}
for municipio in cidades_desejadas:
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

# Visualização Gráfica

## Barras

### Máximos








# Usando as cores especificadas para cada cidade
plt.plot(casos["Semana"], casos["FLORIANÓPOLIS"], label="Florianópolis", color="#1f77b4")  # Azul
plt.plot(casos["Semana"], casos["JOINVILLE"], label="Joinville", color="#ff7f0e")  # Laranja
plt.plot(casos["Semana"], casos["BLUMENAU"], label="Blumenau", color="#2ca02c")  # Verde

# Título e rótulos
plt.title(f"Preciptação no ano de 2023 para as cidades analisadas")
plt.xlabel("Preciptação acumulada de 2023")
plt.ylabel("Preciptação (mm)")

# Adicionando a legenda
plt.legend()

# Exibindo a grade
plt.grid(True)

# Altera o fundo do gráfico para a cor 'honeydew'
plt.gca().patch.set_facecolor("honeydew")  

# Exibe o gráfico
plt.show()








'''
plt.figure(figsize=(10, 6))
plt.bar(df_max["Município"], df_max["Máximo"])
plt.title("VALOR MÁXIMO DOS CASOS DE DENGUE EM SANTA CATARINA")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número Máximo de Casos de dengue")
plt.show()
'''

# principais_max = df_max.head(20)    #Seleciona os 20 municípios com os maiores valores máximos de casos.
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

### Acumulado

#### Ascendente

print(principais_max)

plt.figure(figsize=(10, 6))
plt.bar(principais_max["Município"], principais_max["Soma"])
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

"""#### Descendente"""
'''
plt.figure(figsize=(10, 6))
plt.bar(df_soma["Município"], df_soma["Soma"])
plt.title("SOMA HISTÓRICA DOS CASOS DE DENGUE EM SANTA CATARINA")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número de Casos de dengue")
plt.show()
'''

principais_soma = df_soma.head(20)
print(principais_soma)
plt.figure(figsize=(10, 6))
plt.bar(principais_soma["Município"], principais_soma["Soma"])
plt.title("SOMA HISTÓRICA DOS CASOS DE DENGUE EM SANTA CATARINA")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número de Casos de dengue")
plt.gca().patch.set_facecolor("honeydew")
plt.show()

"""## Série Temporal"""

for municipio in principais_max["Município"]:
    plt.figure(figsize=(10, 6))
    plt.plot(casos["Semana"], casos[municipio])
    plt.title(f"CASOS DE DENGUE, MUNICÍPIO DE {municipio}")
    plt.xlabel("Série Histórica (Semanas Epidemiológicas)")
    plt.ylabel("Número de Casos de dengue")
    plt.grid(True)
    plt.gca().set_ylim(0, sem_tempo.max().max())  # Ajuste do limite superior do eixo y
    plt.gca().patch.set_facecolor("honeydew")  # Cor de fundo dos gráficos
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

