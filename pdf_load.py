#primeiro pressionamos ctrl + shift + p para mudar para o python 3.11
#py install -U langchain-community
#py install langchain==0.3.0 ok
#py install langchain-core==0.3.1
#py install langchain-groq==0.2.0 pypdf
#py install langchain-community==0.3.0

import os
from langchain_groq import ChatGroq 
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

# API KEY segura via Secrets
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
chat = ChatGroq(model = 'llama-3.3-70b-versatile')

pdf_path = r'C:\Users\caio_\OneDrive\Desktop\buscando_informacoes_no_pdf_com_IA\doc.pdf' #digitar a localização do arquivo em pdf

loader = PyPDFLoader(pdf_path)
lista_documentos = loader.load()

documentos = ''
for doc in lista_documentos:
    documentos += doc.page_content

template = ChatPromptTemplate.from_messages([
    ('system','Responda APENAS usando o conteúdo do PDF abaixo.\n'
     'Se a resposta não estiver no documento, diga exatamente: Desculpe, essa informação não está no documento.'
     'PDF:{informacao}'),
    ('user','{input}')
])

chain = template | chat

while True:
    duvida = input('\nQual sua Dúvida? (Digite X para sair!)')
    if duvida.lower() == 'x':
        break
    respostas = chain.invoke({'informacao': documentos, 'input': duvida})

    print(respostas.content)

    