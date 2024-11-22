import streamlit as st
import disruption_generation
import time
from itinerary_calculator import ItineraryCalculator
from itinerary_data import Itinerary
from dataclasses import asdict

st.markdown("###")

st.title("IVoice")

### Fake functions:
def message_generation(itineraries: dict[str, list[Itinerary]]):
    it_dict = {k: [asdict(it) for it in v] for k, v in itineraries.items()}
    time.sleep(3)
    dico = {
        'Pont de sèvres': 'Prenez la ligne 8 pour aller à République',
        'Réaumur-Sébastopol': "Pour aller vers l'ouest prenez la 3",
        "Nation": "Pour aller vers l'ouest prenez la 1 vers l'ouest"
    }
    return dico


###
def itineraire_generation():
    it_calc = ItineraryCalculator()
    itineraries = it_calc.compute_alternate_itineraries(line_id="IDFM:C01379")
    return itineraries

def generation_incident():
    result = disruption_generation.create_disruption()
    st.markdown(result.message, unsafe_allow_html=True)

def loading_itineraire() -> dict[str, list[Itinerary]]:
    with st.spinner("Génération de l'itinéraire:"):
        itinerary = itineraire_generation()
    st.success("Itinéraire généré !")
    return itinerary

def loading_message(itinerary: dict[str, list[Itinerary]]) -> dict[str, str]:
    with st.spinner("Génération du message"):
        messages = message_generation(itinerary)
    st.success("Message généré !")
    return messages

def print_messages(messages: dict[str, str]):
    for key in messages.keys():
        result = f"{key}: {messages.get(key)}"
        st.write(result)


def print_results():
    generation_incident()
    st.write("\n")
    itinerary = loading_itineraire()
    st.write("\n")
    messages = loading_message(itinerary)
    st.write("\n")
    print_messages(messages)


with st.container():
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button('Générer un incident'):
        print_results()
    st.markdown('</div>', unsafe_allow_html=True)
