from langchain_community.document_loaders import WebBaseLoader, DirectoryLoader
from langchain_community.document_loaders import PyMuPDFLoader
import bs4
import glob

class FileLoader:
  
  @staticmethod
  def get_web_loader(url):
    web_loader = WebBaseLoader(
      url,
      bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
          class_=("turtle")
        )
      )                             
    )

    return web_loader.load()
  

  @staticmethod
  def get_pdf_loader(folder_name):
    files = glob.glob(f"{folder_name}/*.pdf")
    docs = []
    for file in files:
      text_loader = PyMuPDFLoader(file)
      docs.append(text_loader.load()[0])
    return docs
  
  
  @staticmethod
  def get_txt_loader(folder_name):
    text_loader = DirectoryLoader(f".\{folder_name}", glob="**\*.txt")
    docs = text_loader.load()
    return docs
  