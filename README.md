# python-plotly-data-analysis



Análise de Uso Global da Internet

Este projeto realiza a extração de dados da web (web scraping) para coletar informações sobre o uso de internet e população mundial. Em seguida, os dados são limpos, unificados e utilizados para gerar visualizações de dados interativas com a biblioteca Plotly.



🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto localmente.



Clone o repositório:



Bash



git clone https://github.com/SEU-USUARIO/global-internet-usage-analysis.git

cd global-internet-usage-analysis

Crie e ative o ambiente virtual:



Bash



# Criar o ambiente

python -m venv venv



# Ativar (Windows)

.\venv\Scripts\activate



# Ativar (macOS/Linux)

source venv/bin/activate

Instale as dependências:

(Certifique-se de que seu arquivo requirements.txt está atualizado com o comando: pip freeze > requirements.txt)



Bash



pip install -r requirements.txt

Execute os scripts na ordem correta:



Bash



# 1. Obter dados de usuários de internet

python get_internet_data.py



# 2. Obter dados de população

python get_population_data.py



# 3. Gerar os gráficos

python src/main.py

Visualize os resultados:

Os gráficos interativos (.html) estarão disponíveis na pasta /output.

