# 💬 Chatbot com GPT-4o1-mini

## 📋 Descrição do Projeto
Este é um **projeto acadêmico** desenvolvido no contexto da disciplina de **Engenharia de Prompt**, ministrada pelo **Prof. Sandeco Macedo** no âmbito da **Pós-Graduação em Sistemas e Agentes Inteligentes** da **Universidade Federal de Goiás (UFG)**.

O chatbot foi implementado pelos alunos:
- 🧑‍💻 **Celio Carcalto**
- 👩‍💻 **Anahi Philbois**

**Projeto no GitHub:** [trab01-pos-UFG-chatbot](https://github.com/Carcalto/trab01-pos-UFG-chatbot.git)

**Aplicação ao Vivo:** [chatbot-trab01-app](https://chatbot-trab01-app.streamlit.app/)

### Objetivo
O objetivo do projeto é criar um chatbot funcional que utilize a API da **OpenAI** para gerar respostas inteligentes e estruturadas, baseando-se em um **prompt inicial** definido em um arquivo externo. O projeto faz uso do modelo **GPT-4o1-mini** e foi desenvolvido com o framework **Streamlit**.

---

## 🛠️ Estrutura do Código

### 1. **Dependências e Configurações**
As principais bibliotecas utilizadas são:
- **Streamlit**: Framework para criar aplicações web interativas em Python.
- **OpenAI**: Biblioteca para interagir com a API da OpenAI.
- **dotenv**: Para carregar variáveis de ambiente de um arquivo `.env`.

```python
# Importa as bibliotecas necessárias
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
```

O arquivo `.env` armazena a chave da API da OpenAI. O código carrega esta chave:
```python
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave de API da OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
```

### 2. **Verificação da Chave da API**
Caso a chave não seja encontrada, o chatbot exibe um erro:
```python
if not openai_api_key:
    st.error("Erro: A chave de API da OpenAI não foi encontrada no arquivo .env.")
```

---

### 3. **Interface do Chatbot**
O chatbot exibe:
- **Título do projeto**: `st.title("💬 Chatbot")`
- **Mensagem para reinício**: `st.info("Para iniciar um novo chat, recarregue a página no navegador.")`
- **Descrição do projeto**:
```python
st.write(
    "Chatbot simples implementado pelos alunos Celio Carcalto e Anahi Philbois que utiliza o modelo GPT-4o1-mini da OpenAI para gerar respostas estruturadas por guardrails predefinidos."
)
```

---

### 4. **Inicialização do Chat**
O código utiliza o `st.session_state` para armazenar o histórico de mensagens. Caso não exista histórico, ele é inicializado:
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

O chatbot utiliza um arquivo externo `estrutura.txt` como prompt inicial:
```python
# Carrega o conteúdo do arquivo "estrutura.txt"
try:
    with open("estrutura.txt", "r", encoding="utf-8") as f:
        estrutura_inicial = f.read()
        st.session_state.messages.append({"role": "user", "content": estrutura_inicial})
```

A resposta inicial é gerada usando a API da OpenAI:
```python
response = client.chat.completions.create(
    model="o1-mini",
    messages=st.session_state.messages,
    stream=False,
)
resposta_modelo = response.choices[0].message.content
st.session_state.messages.append({"role": "assistant", "content": resposta_modelo})
```

---

### 5. **Exibição de Mensagens**
As mensagens trocadas são exibidas no chat:
```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

---

### 6. **Interação do Usuário**
O campo de entrada `st.chat_input` permite que o usuário envie novas mensagens:
```python
if prompt := st.chat_input("Digite sua mensagem:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
```

A resposta do modelo é gerada e exibida:
```python
response = client.chat.completions.create(
    model="o1-mini",
    messages=st.session_state.messages,
    stream=False,
)
resposta_modelo = response.choices[0].message.content
st.session_state.messages.append({"role": "assistant", "content": resposta_modelo})
with st.chat_message("assistant"):
    st.markdown(resposta_modelo)
```

---

## 🗂️ Estrutura de Arquivos
```plaintext
trab01-pos-UFG-chatbot/
│
├── streamlit_app.py          # Código principal do chatbot
├── estrutura.txt             # Arquivo com o prompt inicial
├── .env                      # Variáveis de ambiente (contém a chave da API)
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do projeto
```

---

## ⚙️ Dependências
As dependências estão listadas em `requirements.txt`:
```plaintext
streamlit
openai
python-dotenv
```

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/Carcalto/trab01-pos-UFG-chatbot.git
   cd trab01-pos-UFG-chatbot
   ```
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure o arquivo `.env`:
   ```plaintext
   OPENAI_API_KEY=sua_chave_de_api_aqui
   ```

### Executando o Chatbot Localmente
Inicie o Streamlit:
```bash
streamlit run streamlit_app.py
```

---

## 🚀 Funcionalidades
- **Prompt Inicial:** Usa o conteúdo de `estrutura.txt` como base para o primeiro diálogo.
- **Armazenamento de Mensagens:** Utiliza `st.session_state` para armazenar o histórico de conversas.
- **API da OpenAI:** Gera respostas inteligentes com o modelo `GPT-4o1-mini`.
- **Interface Simples:** Desenvolvida com **Streamlit**, ideal para prototipação.

---

## 🧩 Possíveis Melhorias
1. **Autenticação:** Permitir que o usuário insira sua própria chave da API.
2. **Customização:** Adicionar configurações para escolher o modelo ou ajustar o comportamento do chatbot.
3. **Persistência:** Salvar o histórico de mensagens em um banco de dados ou arquivo.

---

## 🎓 Créditos
Este projeto foi desenvolvido para compor nota na matéria de **Engenharia de Prompt** na **UFG**.

### Professores e Orientadores
- 🧑‍🏫 **Prof. Sandeco Macedo**
  - [GitHub](https://github.com/sandeco)
  - [Canal no YouTube](https://www.youtube.com/@canalsandeco)

### Alunos
- 🧑‍💻 **Celio Carcalto**
- 👩‍💻 **Anahi Philbois**

---

## 📄 Licença
Este projeto é de uso educacional e não possui fins comerciais.

---

Acesse o projeto ao vivo em [chatbot-trab01-app](https://chatbot-trab01-app.streamlit.app/). 🚀

