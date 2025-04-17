from langchain.llms import OpenAI
from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
import yfinance as yf
import warnings
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
load_dotenv()
 
# Bu kısım ilk temel agent kullanımı örneği
"""
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define a simple prompt for the agent
template = 
You are an AI assistant with expertise in data analysis and automation. Answer the following question:
Question: {question}


# Set up the prompt and LLM chain
prompt = PromptTemplate(template=template, input_variables=["question"])
chain = LLMChain(prompt=prompt, llm=llm)

# Example query
query = input("Write your text")
response = chain.run(question=query)
print(f"Agent Response: {response}")
"""

llm = ChatOpenAI(model = "gpt-4")


response = llm.invoke("Hello! What's your name  ?")

print(response.content)