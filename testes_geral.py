# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Abrindo Arquivo
url = "https://raw.githubusercontent.com/matheusf30/dados_dengue/refs/heads/main/casos_dive_pivot_total.csv" #raw
casos = pd.read_csv(url)
print(casos.head())

# Garantir que a coluna "Semana" seja do tipo datetime
casos["Semana"] = pd.to_datetime(casos["Semana"])
print(casos.dtypes)

# Extrair os nomes das cidades (exceto a primeira coluna "Semana")
municipios = casos.columns[1:]
print(municipios)

# Lista das cidades desejadas
cidades_desejadas = ["FLORIANÓPOLIS", "JOINVILLE", "BLUMENAU"]

# Inicializando os dicionários para armazenar os resultados
max = {}
min = {}
soma = {}

# Processando apenas as cidades desejadas
for municipio in cidades_desejadas:
    if municipio in municipios:  # Verifica se o município está no DataFrame
        max[municipio] = casos[municipio].max()  # Calcula o valor máximo de casos de dengue
        min[municipio] = casos[municipio].min()  # Calcula o valor mínimo de casos de dengue
        soma[municipio] = casos[municipio].sum()  # Calcula a soma dos casos de dengue
        print("=" * 50)
        print(f"Analisando o município: {municipio}")
        print("~" * 50)
        print(f"O valor máximo é: {max[municipio]}")
        print("~" * 50)
        print(f"O valor mínimo é: {min[municipio]}")
        print("~" * 50)
        print(f"A soma da série histórica é: {soma[municipio]}")

# Criando os DataFrames com os dados das cidades desejadas
df_max = pd.DataFrame(list(max.items()), columns=['Município', 'Máximo'])
df_min = pd.DataFrame(list(min.items()), columns=['Município', 'Mínimo'])
df_soma = pd.DataFrame(list(soma.items()), columns=['Município', 'Soma'])

# Verificando a estrutura do DataFrame df_soma
print(df_soma.head())  # Verifica se a coluna 'Soma' está presente

# Exibindo os DataFrames
print(df_max)
print(df_min)
print(df_soma)

# Ordenando os DataFrames
df_max = df_max.sort_values(by="Máximo", ascending=False)
df_min = df_min.sort_values(by="Mínimo", ascending=True)
df_soma = df_soma.sort_values(by="Soma", ascending=False)
df_soma_asc = df_soma.sort_values(by="Soma", ascending=True)

# Exibindo os DataFrames após ordenação
print(df_max)
print(df_min)
print(df_soma)
print(df_soma_asc)

# Gerando o gráfico com a soma histórica dos casos
principais_soma = df_soma.head(3)  # Seleciona os 3 primeiros municípios com maior soma de casos
plt.figure(figsize=(10, 6))
plt.bar(principais_soma["Município"], principais_soma["Soma"])
plt.title("SOMA HISTÓRICA DOS CASOS DE DENGUE EM SANTA CATARINA (Menores Registros)")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation=90)
plt.ylabel("Número de Casos de dengue")
plt.show()

# Visualização de outros gráficos, se necessário
principais_max = df_max.head(3)      # Seleciona os 3 municípios com os maiores valores máximos de casos. (Joinville, Blumenau e Floripa)
plt.figure(figsize=(10, 6))
plt.bar(principais_max["Município"], principais_max["Máximo"])
plt.title("VALOR MÁXIMO DOS CASOS DE DENGUE EM SANTA CATARINA")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número Máximo de Casos de dengue")
plt.gca().patch.set_facecolor("honeydew")
plt.show()

'''
# Série Temporal - Gráfico de cada município
for municipio in principais_max["Município"]:
    plt.figure(figsize=(10, 6))
    plt.plot(casos["Semana"], casos[municipio])
    plt.title(f"CASOS DE DENGUE, MUNICÍPIO DE {municipio}")
    plt.xlabel("Série Histórica (Semanas Epidemiológicas)")
    plt.ylabel("Número de Casos de dengue")
    plt.grid(True)
    plt.gca().set_ylim(0, casos[municipio].max())  # Ajuste do limite superior do eixo y
    plt.gca().patch.set_facecolor("honeydew")  # Cor de fundo dos gráficos
    plt.show()

# Caso você precise visualizar a soma de casos de outros municípios em ordem crescente
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
# Plotando gráfico da soma histórica em ordem decrescente
# '''
plt.figure(figsize=(10, 6))
plt.bar(df_soma["Município"], df_soma["Soma"])
plt.title("SOMA HISTÓRICA DOS CASOS DE DENGUE EM SANTA CATARINA")
plt.xlabel("Municípios Catarinenses")
plt.xticks(rotation = 90)
plt.ylabel("Número de Casos de dengue")
plt.show()
# '''

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

'''
# A seguir, código para plotar a série temporal de todos os municípios
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
# '''

# Série Temporal para os 3 principais municípios (com base no valor máximo)
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

# Série Temporal para os 3 municípios com maior soma histórica
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

