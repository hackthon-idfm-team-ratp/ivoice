import streamlit as st
import disruption_generation
import time

st.markdown("###")

st.title("IVoice")

### Fake functions:
def message_generation():
    dico = {
        'Pont de sèvres': 'Prenez la ligne 8 pour aller à République',
        'Réaumur-Sébastopol': "Pour aller vers l'ouest prenez la 3",
        "Nation": "Pour aller vers l'ouest prenez la 1 vers l'ouest"
    }
    time.sleep(3)
    return dico

def itineraire_generation():
    time.sleep(5)

###

def generation_incident():
    result = disruption_generation.create_disruption()
    st.write(result.message)

def loading_itineraire():
    with st.spinner("Génération de l'itinéraire:"):
        itineraire_generation()
    st.success("Itinéraire généré !")

def loading_message():
    with st.spinner("Génération du message"):
        message_generation()
    st.success("Message généré !")

def print_messages():
    dico = message_generation()
    for key in dico.keys():
        result = f"{key}: {dico.get(key)}"
        st.write(result)


def print_results():
    generation_incident()
    st.write("\n")
    loading_itineraire()
    st.write("\n")
    loading_message()
    st.write("\n")
    print_messages()


with st.container():
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button('Générer un incident'):
        print_results()
    st.markdown('</div>', unsafe_allow_html=True)
