# Importa as bibliotecas necessárias
import streamlit as st  # Framework para criação de aplicações web interativas
from openai import OpenAI  # Biblioteca para interagir com a API da OpenAI
from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente de um arquivo .env
import os  # Biblioteca para interagir com o sistema operacional

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave de API da OpenAI a partir das variáveis de ambiente
openai_api_key = os.getenv("OPENAI_API_KEY")

# Verifica se a chave de API foi encontrada
if not openai_api_key:  # Caso a chave não tenha sido configurada no arquivo .env
    st.error("Erro: A chave de API da OpenAI não foi encontrada no arquivo .env.")
else:  # Caso a chave esteja disponível

    # Define o título e a descrição da aplicação
    st.title("💬 Chatbot")  # Adiciona um título no topo da aplicação
    st.write(
        "Chatbot simples implementado pelos alunos Celio Carcalto e Anahi Philbois que utiliza o modelo GPT-4o1-mini da OpenAI para gerar respostas estruturadas por guardrails predefinidos."
    )  # Adiciona um texto explicativo sobre o funcionamento do chatbot

    # Cria um cliente OpenAI utilizando a chave de API fornecida
    client = OpenAI(api_key=openai_api_key)

    # Inicializa a variável de estado da sessão para armazenar as mensagens do chat
    # Isso garante que as mensagens sejam preservadas mesmo após recarregamentos
    if "messages" not in st.session_state:
        st.session_state.messages = []  # Lista para armazenar as mensagens trocadas no chat
        
        # Carrega o conteúdo do arquivo "estrutura.txt" como a mensagem inicial
        try:
            with open("estrutura.txt", "r", encoding="utf-8") as f:
                estrutura_inicial = f.read()  # Lê o conteúdo do arquivo

                # Envia a estrutura inicial como a primeira mensagem do "usuário"
                st.session_state.messages.append({"role": "user", "content": estrutura_inicial})

                # Gera a resposta inicial do modelo
                response = client.chat.completions.create(
                    model="o1-mini",  # Modelo a ser utilizado
                    messages=st.session_state.messages,
                    stream=False,
                )
                resposta_modelo = response.choices[0].message.content  # Acessa o atributo `content`

                # Adiciona a resposta do modelo como a primeira mensagem visível
                st.session_state.messages.append({"role": "assistant", "content": resposta_modelo})

                # Remove a mensagem inicial do "usuário" para que não seja exibida
                st.session_state.messages.pop(0)
        except FileNotFoundError:
            st.error("Erro: O arquivo 'estrutura.txt' não foi encontrado na raiz do projeto.")
            st.stop()  # Interrompe a execução se o arquivo não for encontrado

    # Exibe as mensagens existentes no chat, começando pela resposta inicial
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):  # Define o estilo da mensagem com base no remetente
            st.markdown(message["content"])  # Exibe o texto da mensagem no formato Markdown

    # Adiciona um campo de entrada para o usuário digitar uma nova mensagem
    if prompt := st.chat_input("Digite sua mensagem:"):

        # Armazena e exibe a mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Gera uma resposta usando a API da OpenAI
        try:
            response = client.chat.completions.create(
                model="o1-mini",
                messages=st.session_state.messages,
                stream=False,
            )
            resposta_modelo = response.choices[0].message.content  # Acessa o atributo `content`
        except Exception as e:
            st.error(f"Erro ao gerar a resposta: {e}")
            st.stop()

        # Armazena e exibe a resposta do modelo
        st.session_state.messages.append({"role": "assistant", "content": resposta_modelo})
        with st.chat_message("assistant"):
            st.markdown(resposta_modelo)
