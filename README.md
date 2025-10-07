# Covid-19 Dashboard 🦠

Um dashboard interativo para visualização de dados da Covid-19, construído com Streamlit, Pandas e Plotly.

## 📜 Sobre o Projeto

Este projeto apresenta um dashboard web que permite aos usuários explorar dados globais da Covid-19. É possível filtrar os dados por país e visualizar diferentes métricas, como casos confirmados, mortes, recuperados, entre outros, de forma simples e intuitiva.

## ✨ Funcionalidades

- **Visualização Interativa:** Gráfico de barras dinâmico que se atualiza com base nas seleções do usuário.
- **Filtro por País/Região:** Permite selecionar um país específico ou visualizar dados globais.
- **Seleção de Métricas:** Escolha entre diversas métricas como "Confirmados", "Mortes", "Recuperados", "Casos Ativos", etc.
- **Ranking Top 20:** Ao selecionar "All" (Todos), o gráfico exibe os 20 países com os maiores números para a métrica escolhida.

## 🚀 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python:** Linguagem de programação principal.
- **Streamlit:** Framework para a criação rápida de aplicações web de dados.
- **Pandas:** Biblioteca para manipulação e análise dos dados a partir do arquivo CSV.
- **Plotly Express:** Biblioteca para a criação de gráficos interativos e de alta qualidade.

## 🖼️ Telas da Aplicação

### Visão Geral (Top 20 Países para uma Métrica)
A tela principal exibe o ranking dos 20 países com mais casos para a métrica selecionada.

![Visão Geral do Dashboard](imgs/dashboard_geral.png)

### Visão Filtrada por País
Ao selecionar um país, o gráfico foca nos dados daquela região específica.

![Visão por País](imgs/dashboard_pais.png)

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para executar o projeto em sua máquina local.

### Pré-requisitos

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)

### Passos para Instalação

1. **Clone o repositório** (se estiver usando git):
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd covid_dashboard
   ```

2. **Instale as dependências** a partir do arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação Streamlit:**
   ```bash
   streamlit run src/covid_dashboard.py
   ```

Após executar o último comando, o dashboard será aberto automaticamente no seu navegador padrão.
