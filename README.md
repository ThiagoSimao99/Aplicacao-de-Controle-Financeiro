# 💰 MyFinance - Controle de Contas por Espaços

Bem-vindo ao **MyFinance**, uma aplicação web simples e eficiente para gerenciamento de contas a pagar, organizada por contextos (Espaços).

Ideal para quem quer separar as contas pessoais, da casa, ou de dependentes em um único lugar, com uma interface limpa e foco no que importa: **quanto eu tenho que pagar este mês?**

## ✨ Funcionalidades

- **🏠 Espaços (Grupos)**: Crie ambientes separados para organizar suas contas (ex: "Minhas Contas", "Casa de Praia", "Filho na Faculdade").
- **📅 Navegação Temporal**: Visualize suas contas por mês/ano. Navegue facilmente para ver o histórico ou planejar o futuro.
- **📊 Resumo Financeiro**: Dashboards automáticos em cada espaço mostrando:
  - **Total Previsto**: Quanto você tem de boletos para o mês.
  - **Total Pago**: Quanto já foi quitado.
  - **Total Pendente**: O que ainda falta sair do bolso.
- **📝 Gestão de Contas**: Adicione contas com vencimento, valor e descrição. Marque como "Pago" com um clique.
- **🌍 Localização**: Configurado para o fuso horário brasileiro (America/Sao_Paulo).

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem base.
- **Django 5+**: Framework web robusto.
- **Bootstrap 5**: Estilização responsiva e moderna.
- **PostgreSQL**: SGBD avançado e escalável, utilizado para o ambiente de produção.
- **HTML5/CSS3**: Estrutura e layout.

## 🚀 Como Rodar o Projeto

Siga estes passos para rodar a aplicação em sua máquina local.

### Pré-requisitos

- Python instalado.
- Git (opcional, para clonar).

### Instalação

1. **Clone o repositório** (ou baixe os arquivos):

   ```bash
   git clone https://github.com/ThiagoSimao99/Aplicacao-de-Controle-Financeiro.git
   cd Aplicação_Contas_Financeiras
   ```

2. **Crie e ative um ambiente virtual** (Recomendado):

   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare o Banco de Dados**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o Servidor**:

   ```bash
   python manage.py runserver
   ```

6. **Acesse**:
   Abra o navegador em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📂 Estrutura do Projeto

- `config/`: Configurações principais do projeto Django (settings, urls).
- `financeiro/`: Aplicativo principal.
  - `models.py`: Definição de `Grupo` e `ContaPagar`.
  - `views.py`: Lógica de negócio (CRUDs e filtros de data).
  - `urls.py`: Rotas da aplicação.
- `templates/financeiro/`: Arquivos HTML (Listas, Formulários, Detalhes).

---

Desenvolvido com foco em simplicidade e produtividade.
