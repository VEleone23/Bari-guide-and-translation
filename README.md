🇮🇹 Bari Translator & Info App

Un progetto che utilizza Ollama, LLM locali, Python e Gradio per tradurre testi su Bari e rispondere a domande sulla città.

📌 Descrizione del progetto

Questa applicazione fornisce:

Traduzione automatica dall’italiano verso inglese e russo (cirillico)

Informazioni sulla città di Bari basate su un modello LLM locale

Interfaccia web semplice e moderna tramite Gradio

Il progetto funziona totalmente offline, usando un modello LLM ospitato in locale tramite Ollama.

⚙️ Tecnologie utilizzate
Tecnologia	Ruolo
Python 3.11	Linguaggio principale
Gradio	Interfaccia web
Ollama	Server locale per LLM
Modelli Llama 3.1 locali	Traduzione e risposte
Docker (opzionale)	Distribuzione facilitata
📁 Struttura del progetto
progetto/
│── webapp.py          # Interfaccia Gradio + routing
│── translator.py      # Comunicazione con Ollama
│── Dockerfile         # (Opzionale) containerizzazione
│── README.md

🧠 Come funziona
1️⃣ Traduzione

Il file translator.py invia un prompt controllato al modello:

prompt = f"""
Translate the following Italian text into English and Russian.
Italian:
{text}

Output format:
English: <eng>
Russian: <rus>
"""


Ollama risponde e il programma estrae le traduzioni in maniera affidabile e senza inventare contenuti.

2️⃣ Informazioni su Bari

La funzione ask_about_bari() usa un prompt dedicato e fornisce risposte brevi e corrette, sempre basate su un modello locale.

3️⃣ Interfaccia Gradio

webapp.py costruisce un’interfaccia moderna:

casella di input

pulsante "Traduci"

pulsante "Info su Bari"

output in box separati

tema personalizzato

emoticon “in stile Bari” 🐙⛵🌊

▶️ Avvio dell’app

Assicurati che Ollama sia avviato e che il modello sia disponibile:

ollama run bari-translator
ollama run bari-guide


Poi esegui:

python webapp.py


Apri il browser su:

http://127.0.0.1:7860

🐳 (Opzionale) Avvio con Docker

Costruire l’immagine:

docker build -t bari-app .


Eseguire il container:

docker run -p 7860:7860 -e OLLAMA_HOST="host.docker.internal:11434" bari-app

📝 Requisiti

Python ≥ 3.10

Ollama installato

Un modello locale, es.:

bari-translator

bari-guide

pip install gradio requests