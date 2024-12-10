# 💬 Chatbot com GPT-4o1-mini

## 📋 Descrição do Projeto
Este é um **projeto acadêmico** desenvolvido no contexto da disciplina de **Engenharia de Prompt**, ministrada pelo **Prof. Sandeco Macedo** no âmbito da **[Especialização Lato Sensu em Sistemas e Agentes Inteligentes](https://agentes.inf.ufg.br/)** na **Universidade Federal de Goiás (UFG)**.

O chatbot foi implementado pelos alunos:
- 🧑‍💻 **Celio Carcalto**
- 👩‍💻 **Anahi Philbois**

**Projeto no GitHub:** [chatbot-trab01-app](https://github.com/Carcalto/chatbot-trab01-app.git)

**Aplicação ao Vivo:** [chatbot-trab01-app](https://chatbot-trab01-app.streamlit.app/)

### Sobre a Especialização
A **[Especialização Lato Sensu em Sistemas e Agentes Inteligentes](https://agentes.inf.ufg.br/)** é focada na construção de sistemas utilizando **Agentes Inteligentes**, com aplicações práticas e fundamentos teóricos para o desenvolvimento de soluções inovadoras.

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
chatbot-trab01-app/
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
   git clone https://github.com/Carcalto/chatbot-trab01-app.git
   cd chatbot-trab01-app
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

# Estrutura do Prompt

## 📋 Descrição da Estrutura
Abaixo está detalhada a estrutura lógica e funcional do **prompt inicial** usado neste chatbot. Essa estrutura é carregada a partir do arquivo `estrutura.txt` e configura as diretrizes e os guardrails para garantir que o chatbot siga os princípios de qualidade, confiabilidade e segurança.

O design do prompt foi cuidadosamente elaborado para:
1. **Definir uma persona específica** a partir das interações iniciais.
2. **Estabelecer guardrails** que orientam o comportamento do chatbot, evitando respostas incorretas ou enganosas.
3. **Garantir ética e segurança** em todas as interações.

---

## 🌐 Estrutura Geral do Prompt
```xml
<estrutura_prompt>
    <configuracao>
        <persona>
            <definicao>Peça a {persona} e depois siga a estrutura</definicao>
            <exemplo>Por favor, defina a persona (ex: médico, engenheiro).</exemplo>
        </persona>
    </configuracao>
    <guardrails>
        <react>
            <pensamento>Validação do raciocínio</pensamento>
            <acao>Verificação de ações</acao>
            <observacao>Confirmação de resultados</observacao>
        </react>
        <reflexao>
            <auto_avaliacao>Análise de qualidade</auto_avaliação>
            <melhoria>Refinamento contínuo</melhoria>
        </reflexao>
        <anti_alucinacao>
            <verificacao_fonte>
                <base>Validar informação na base de conhecimento</base>
                <incerteza>Expressar claramente quando houver dúvida</incerteza>
                <limites>Reconhecer limitações explicitamente</limites>
            </verificacao_fonte>
            <controle_afirmacoes>
                <evidencias>Exigir base factual</evidencias>
                <qualificadores>Usar termos como 'possivelmente' quando apropriado</qualificadores>
                <admissao>Admitir desconhecimento quando necessário</admissao>
            </controle_afirmacoes>
            <sinalizacao>
                <confianca>Alta/Média/Baixa</confianca>
                <fonte>Base de conhecimento/Inferência/Incerto</fonte>
            </sinalizacao>
        </anti_alucinacao>
        <eticos>
            <valores>Alinhamento moral e prevenção de viés</valores>
            <seguranca>Prevenção de danos e privacidade</seguranca>
        </eticos>
    </guardrails>
    <protocolos>
        <risco>
            <alto>Rejeitar e documentar</alto>
            <medio>Responder com ressalvas</medio>
            <baixo>Responder normalmente</baixo>
        </risco>
    </protocolos>
    <saida>
        <formato>Resposta clara e verificada</formato>
        <protecoes>Status dos guardrails ativos</protecoes>
        <nivel_confianca>Indicador explícito de certeza</nivel_confianca>
    </saida>
    <instrucao>
        Após definir persona, ativar guardrails e fornecer respostas protegidas em Português Brasileiro, sempre indicando nível de confiança e fonte da informação.
    </instrucao>
</estrutura_prompt>
```

---

## 🧩 Detalhamento da Estrutura

### **1. Configuração**
Define o primeiro passo da interação: solicitar ao usuário a definição de uma **persona**.
- **Definição:** Indica como o sistema deve pedir uma persona ao usuário.
- **Exemplo:** Sugestão de como a persona pode ser solicitada.

### **2. Guardrails**
Os **guardrails** são regras que orientam o comportamento do chatbot para evitar erros e inconsistências. Eles são organizados em quatro categorias:

#### **2.1. ReAct**
Baseado em um ciclo de **pensamento, ação e observação**:
- **Pensamento:** Validar o raciocínio antes de executar ações.
- **Ação:** Verificar ações tomadas com base na lógica.
- **Observação:** Confirmar se os resultados atendem às expectativas.

#### **2.2. Reflexão**
Garante a qualidade contínua das respostas:
- **Autoavaliação:** Analisar a qualidade da resposta.
- **Melhoria:** Refinar continuamente o conteúdo gerado.

#### **2.3. Anti-alucinação**
Previne respostas inventadas ou incorretas:
- **Verificação de Fonte:**
  - **Base:** Validar informações usando uma base de conhecimento confiável.
  - **Incerteza:** Admitir dúvidas quando não houver certeza.
  - **Limites:** Reconhecer limitações explicitamente.
- **Controle de Afirmativas:**
  - **Evidências:** Exigir uma base factual para as respostas.
  - **Qualificadores:** Usar termos como "possivelmente" para incertezas.
  - **Admissão:** Admitir desconhecimento quando necessário.
- **Sinalização:**
  - **Confiança:** Indicar níveis como Alta/Média/Baixa.
  - **Fonte:** Diferenciar entre conhecimento baseado em fatos, inferências e incertezas.

#### **2.4. Éticos**
Orientações éticas que guiam o chatbot:
- **Valores:** Garantir alinhamento moral e evitar vieses.
- **Segurança:** Priorizar a privacidade e a prevenção de danos.

### **3. Protocolos**
Define como o chatbot deve lidar com situações de risco:
- **Risco Alto:** Rejeitar a interação e documentar.
- **Risco Médio:** Responder com ressalvas e transparência.
- **Risco Baixo:** Proceder com uma resposta normal.

### **4. Saída**
Especifica o formato e a confiabilidade das respostas:
- **Formato:** Respostas devem ser claras e verificadas.
- **Proteções:** Guardrails devem estar sempre ativos.
- **Nível de Confiança:** Indicar explicitamente o grau de certeza da resposta.

### **5. Instrução**
Orienta o chatbot a:
- Solicitar a **persona**.
- Ativar os **guardrails**.
- Fornecer respostas protegidas em **Português Brasileiro**.
- Indicar o nível de confiança e a fonte da informação.

---

## 🛠️ Implementação no Chatbot
Esta estrutura é carregada automaticamente como a primeira interação no chatbot. O conteúdo é lido do arquivo `estrutura.txt` e configurado no histórico de mensagens antes de qualquer entrada do usuário:
```python
# Carrega o conteúdo do arquivo "estrutura.txt"
try:
    with open("estrutura.txt", "r", encoding="utf-8") as f:
        estrutura_inicial = f.read()
        st.session_state.messages.append({"role": "user", "content": estrutura_inicial})
```

A resposta inicial do modelo é gerada com base nesta estrutura:
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

Com esta estrutura, o chatbot é capaz de:
1. Seguir rigorosamente as diretrizes definidas no prompt inicial.
2. Evitar respostas alucinatórias ou com vieses.
3. Manter um alto nível de confiabilidade e segurança em suas interações.

**Acesse o código completo:** [GitHub - chatbot-trab01-app](https://github.com/Carcalto/chatbot-trab01-app.git)  
**Testar a aplicação ao vivo:** [chatbot-trab01-app](https://chatbot-trab01-app.streamlit.app/)  

---

## 🎓 Créditos
Este projeto foi desenvolvido para compor nota na matéria de **Engenharia de Prompt** na **[Especialização Lato Sensu em Sistemas e Agentes Inteligentes](https://agentes.inf.ufg.br/)** da **Universidade Federal de Goiás**.

### Professores e Orientadores
- 🧑‍🏫 **Prof. Sandeco Macedo**
  - [GitHub](https://github.com/sandeco)
  - [Canal no YouTube](https://www.youtube.com/@canalsandeco)

### Alunos
- 🧑‍💻 **Celio Carcalto**
- 👩‍💻 **Anahi Philbois**

---

## 📄 Licença
Apache-2.0 license
