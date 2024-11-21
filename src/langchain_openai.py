import openai
import json
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

from langchain import LLMChain
from langchain import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Appeler API du LLM
openai_api_version=os.getenv('AZURE_OPENAI_API_VERSION')
deployment_name=os.getenv('AZURE_OPENAI_MODELS')
openai_api_type="azure"

# Initialisation du LLM

llm = AzureChatOpenAI(
    openai_api_version=openai_api_version,
    deployment_name=deployment_name,
    openai_api_type=openai_api_type
)
reponse = llm([HumanMessage(content="Write me a poem")])

print(reponse.content)

# Prompt pour le LLM

template = """


"""

prompt = PromptTemplate(
    input_variables=["product_type", "customer_request"],
    template=template,
)

llm([HumanMessage(content="Write me a poem")])
