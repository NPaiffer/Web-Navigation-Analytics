import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

diretorio_atual = os.getcwd()
# Mude o arquivo de dados_navegacao para dados_navegacao2 se quiser analisar outro resultado ou crie você mesmo o resultado utilizando a página em html do nosso projeto
caminho_arquivo = os.path.join(diretorio_atual, 'analise', 'dados_navegacao2.csv')

dados = pd.read_csv(caminho_arquivo)

print(dados.head())

plt.figure(figsize=(10, 6))
plt.scatter(dados['posX'], dados['posY'], alpha=0.5)
plt.title('Mapa de Calor da Navegação')
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.show()

print(dados.describe())
