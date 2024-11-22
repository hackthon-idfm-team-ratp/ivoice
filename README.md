# IVoice

Ivoice is a demonstration tool illustrating how during an incident on the metro network. Customised messages can be generated for each station on the impacted line.

The tool provides a streamlit frontend to simulate the occurence of an incident and display the generated messages for each station on a map.

## Installation

In addition to the libraries provided in the Onyxia environment the project requires extra dependencies to run.

Install the dependencies using:
```
pip install -r requirements.txt
```

Certain environment variables must be provided as well these variables are listed in the .env.template file.
Copy the .env.template file to a file names .env and replace the "XXX" for each variable with the appropriate value.

## Run

To run the project, simply run
```
streamlit run src/front.py
```