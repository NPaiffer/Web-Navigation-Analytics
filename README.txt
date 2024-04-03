ALUNOS: Clara de Fonte Almeida RM554321 e Nicolas Paiffer do Carmo RM554145

*Instale as bibliotecas pandas, matplotlib e seaborn*

Manual de Utilização do Programa de Coleta de Dados de Navegação

1. Sobre o Programa:
   Este programa é usado para coletar dados de navegação do usuário em uma página da web. Ele coleta informações como cliques do mouse e posição na página e salva esses dados em um arquivo CSV para análise posterior.

2. Como Utilizar:
   - Abra o arquivo "index.html" em qualquer navegador da web.
   - Clique em qualquer lugar na página para coletar dados de navegação.
   - Após coletar dados suficientes, clique no botão "Exportar Dados para CSV" para salvar os dados em um arquivo CSV chamado "dados_navegacao.csv".
   - Os dados coletados podem então ser analisados usando um software de análise de dados, como Python com as bibliotecas Pandas e Matplotlib.

3. Análises e Explicações dos Resultados:
   Após coletar os dados de navegação e salvá-los em um arquivo CSV, é possível realizar diversas análises e gerar visualizações para compreender o comportamento dos usuários na página. Alguns exemplos de análises que podem ser realizadas incluem:
   - Análise da quantidade de cliques realizados em diferentes áreas da página.
   - Análise da posição média dos cliques ao longo do tempo.
   - Identificação de padrões de navegação dos usuários.
   - Criação de gráficos de dispersão, histogramas ou mapas de calor para visualizar os dados de forma mais intuitiva.

4. Requisitos do Sistema:
   - Um navegador da web moderno (por exemplo, Chrome, Firefox, Safari) instalado no computador.
   - Se o usuário desejar realizar análises avançadas dos dados com Python, é necessário ter o Python instalado no sistema, juntamente com as bibliotecas Pandas e Matplotlib e Seaborn.


Descrição do arquivo grafico.py:

O arquivo grafico.py contém um script em Python que lê os dados de navegação de um arquivo CSV, realiza uma análise exploratória básica desses dados e gera um gráfico de calor da navegação. Aqui está uma descrição detalhada do que o código faz:

Leitura dos dados: Utiliza a biblioteca Pandas para ler os dados de navegação de um arquivo CSV.

Análise exploratória dos dados:

Imprime as primeiras linhas dos dados para uma visualização inicial.
Verifica as informações sobre as colunas do DataFrame, incluindo o tipo de dados de cada coluna e o número de valores não nulos.
Calcula estatísticas descritivas sobre os dados, como média, desvio padrão, mínimo, máximo, etc.
Produção do gráfico de calor:

Utiliza a biblioteca Matplotlib para plotar um gráfico de calor da navegação com base nas coordenadas (posX, posY) dos cliques na página.
O gráfico de calor visualiza a densidade de cliques em diferentes áreas da página, onde áreas com mais cliques são representadas por cores mais intensas.

*
*

Descrição do arquivo load.py:

O arquivo load.py contém um script em Python que lê os dados de navegação de um arquivo CSV, realiza uma análise exploratória básica desses dados e calcula a contagem de cliques por timestamp. Aqui está uma descrição detalhada do que o código faz:

Leitura dos dados: Utiliza a biblioteca Pandas para ler os dados de navegação de um arquivo CSV.

Análise exploratória dos dados:

Imprime as primeiras linhas dos dados para uma visualização inicial.
Verifica as informações sobre as colunas do DataFrame, incluindo o tipo de dados de cada coluna e o número de valores não nulos.
Calcula estatísticas descritivas sobre os dados, como média, desvio padrão, mínimo, máximo, etc.
Contagem de cliques por timestamp:

Agrupa os dados pelo timestamp e conta o número de cliques para cada timestamp.
O resultado é uma série de dados que representa a contagem de cliques para cada momento em que um clique foi registrado.
Produção de visualizações:

Plota um histograma da contagem de cliques por timestamp para visualizar a distribuição dos cliques ao longo do tempo.
Plota um gráfico de dispersão dos cliques na página para visualizar a posição dos cliques (posX, posY) em relação à página.