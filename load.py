import pandas as pd
import matplotlib.pyplot as plt

# Mude o arquivo de dados_navegacao para dados_navegacao2 se quiser analisar outro resultado ou crie você mesmo o resultado utilizando a página em html do nosso projeto
caminho_arquivo = './analise/dados_navegacao.csv' 
dados = pd.read_csv(caminho_arquivo)
print("Primeiras linhas dos dados:")
print(dados.head())
print()

print("Colunas do DataFrame:")
print(dados.columns)
print()

print("Informações sobre os dados:")
print(dados.info())
print()

print("Estatísticas descritivas:")
print(dados.describe())
print()

contagem_cliques = dados.groupby('timestamp').size()
print("Contagem de cliques por timestamp:")
print(contagem_cliques)
print()


plt.figure(figsize=(10, 6))
plt.hist(contagem_cliques, bins=range(1, max(contagem_cliques)+2), align='left', color='skyblue', edgecolor='black')
plt.xlabel('Número de Cliques')
plt.ylabel('Número de Timestamps')
plt.title('Histograma da Contagem de Cliques por Timestamp')
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(dados['posX'], dados['posY'], alpha=0.5)
plt.title('Gráfico de Dispersão dos Cliques na Página')
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.grid(True)
plt.show()
