from azure.identity import DefaultAzureCredential,InteractiveBrowserCredential
import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()


llm   = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                   model="gpt-4")


mail_iceriği = """

Dear,

Good day,

 

Kindly advise best rate for below:


- Pick up : Fon Group Teknoloji Telekomünikasyon San.ve Tic. A.Ş. Karpuzsekisi Mh.22/2 Cd. No:42 Hacılar/KAYSERİ

- POL: Mersin

- POD: Alexandria , Egypt

- 2x40HC

- Cables & Accessories.

- 21 days free at destination.
"""




prompt = f"find out if it is a sea land or air offer from the sentence in the {mail_iceriği} and output the container type, pickup and discharge location and output each information as a key value."



response = llm(prompt)

other_prompt= f"Show the offer, cargo weight, loading and unloading port in the {response} one by one and output them as a json file. Also show whether it is export or import according to turkey."


res = llm(other_prompt)
print(res)