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
#reponse = llm([HumanMessage(content="Write me a poem")])

#print(reponse.content)

# Prompt pour le LLM

ligne_incident = "Métro 9"
trajets_alternatifs = {"Fake_station": [{"itinary_type": "centre Paris", 
                                        "routes" : [{"start" : "Démocrate", "end" : "Balna", "ligne": "1"}]}],
                       "Fake_station_2": [{"itinary_type" : "Paris Nord-Est", 
                                        "routes" : [{"start" : "Longitude", "end" : "Voltour", "ligne": "10"}]}],
                        }


template = f"""
Ta mission est d'informer et de rassurer de manière concise, précise, exhaustive, polie et joyeuse.
 
Tu commences par énoncer la nature de l'incident et la station qui est touchée. Par exemple :
Bonjour chers voyageurs, un bagage oublié demande l'intervention d'une équipe spécialisée. La ligne 9 est bloquée entre les stations Belle Vue et Pouvoir pendant un temps indéterminé.
 
Puis, rassure-les en indiquant que tu vas les aider à trouver le meilleur itinéraire. Par exemple :
Nous sommes désolés pour cet incident, mais nous sommes là pour vous guider jusqu’à votre destination.
 
Situe dans quelle station les voyageurs se trouvent. Par exemple :
Vous êtes actuellement à la station Démocrate de la ligne 9. Voici les itinéraires possibles selon votre destination.
 
Maintenant, tu vas expliquer, itinéraire par itinéraire, comment se déplacer. Tu vas utiliser la même structure d'explication pour chacun d’eux.
 
Énonce la direction de l’itinéraire pour les voyageurs concernés. Par exemple :
Pour tous les voyageurs en direction du Nord-Ouest de Paris.
 
Énonce la station et le numéro de ligne recommandé. Par exemple :
Empruntez la ligne 1 à la station Démocrate jusqu'à la station Balna.

Pour générer ces itinéraires, utilise les données suivantes :
- ligne impacté : {ligne_incident}
- liste des trajets alternatifs par station : {trajets_alternatifs}

Fournis les résultats au format JSON, avec comme clé la station, et comme la valeur le message qui lui est destiné. Par exemple :
{{"Démocrate" : "Bonjour chers voyageurs, un bagage oublié demande l'intervention d'une équipe spécialisée. La ligne 9 est bloquée entre les stations Belle Vue et Pouvoir pendant un temps indéterminé. Vous êtes actuellement à la station Démocrate. Voici les itinéraires possibles selon votre destination. Pour tous les voyageurs en direction du Nord-Ouest de Paris. Emprunter la ligne 9 en rejoignant la station Balna."}}

"""

llm_var = llm([HumanMessage(content=template)])
print(llm_var)