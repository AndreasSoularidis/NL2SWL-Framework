from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from PromptTempates import CustomPromptTemplates
from FileLoaders import FileLoader

load_dotenv()


# PARAMETERS
ALL_COMPONENTS = True
ONTOLOGY_ONLY = False
MODEL = "gpt-4o"
TEMPERATURE = 0.0
RAG_DATA = "data_SWRL/Ontology"
CHUNK_SIZE = 750
CHUNK_OVERLAP = 0
SEARCH_TYPE = "similarity"
K = 3

llm = ChatOpenAI(model=MODEL, temperature=TEMPERATURE)

def format_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)

if ALL_COMPONENTS or ONTOLOGY_ONLY:
  docs = FileLoader.get_txt_loader(RAG_DATA)

  text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
  splits = text_splitter.split_documents(docs)

  vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
  retriever = vectorstore.as_retriever(search_type=SEARCH_TYPE, search_kwargs={"k": K})

  if ALL_COMPONENTS: 
    custom_prompt = PromptTemplate.from_template(CustomPromptTemplates.RAG_template)
  else:
    custom_prompt = PromptTemplate.from_template(CustomPromptTemplates.ontology_template)
  
  chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | custom_prompt
    | llm
    | StrOutputParser()
  )
else:
  custom_prompt = PromptTemplate.from_template(CustomPromptTemplates.simple_template)
  chain = custom_prompt | llm | StrOutputParser()

prompts = CustomPromptTemplates.rules()

for prompt in prompts:
  for chunk in chain.stream(prompt):
    print(chunk, end="", flush=True)
  print()