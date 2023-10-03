# Import os to set API key
import os
# Import OpenAI as main LLM service
# Bring in streamlit for UI/app interface
import streamlit as st
import string


# Import PDF document loaders...there's other ones as well!
from langchain.document_loaders import PyPDFLoader
# Import chroma as the vector store 
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from IPython.display import display, HTML
from langchain import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import SequentialChain
import re 
import inputWidgets as inputs
import outputWidgets as output
import apikey as key
import ParsePdf as pdfparser

# Create API Key
llm,embeddings = key.llmKeySetup()
pdfname ='Timetable.pdf'
response=""
#Parse PDF
docsearch=  pdfparser.returnDocEmbeddings(pdfname)
chain = load_qa_chain(OpenAI(), chain_type="stuff")

# Create a text input box for the user
st,prompt = inputs.returnTextboxInput()


#Check the Course code pattern before entering the prompt
pattern = r"^[A-Za-z]{4}-\d{4}$"

if re.match(pattern, prompt):
        # Then pass the prompt to the LLM
        docs = docsearch.similarity_search(prompt)
        response = "enter the dragon"
        prompt= "Format your section information for the course "+prompt +" HTML table.\
              If the information isn't present, use \" Not available in graduate timetable. \" \ as Html table."
        response=chain.run(input_documents=docs, question=prompt)
       
elif(prompt != "" and re.match(pattern, prompt) is None):
     response = "Error!! Incorrect course code. Please check the course code.Format Example:: ABCD-0888"

# ...and write it out to the screen 
output.outputToScreen(st,response)
