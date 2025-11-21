import requests  # usiamo requests per inviare il prompt a Ollama tramite HTTP

# URL del server locale di Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

# Modello da usare (installato tramite Ollama)
MODEL = "llama3"


def translate(text: str) -> dict:
    """Traduce testo italiano in inglese e russo restituendo un dizionario."""

    # Prompt per ottenere due traduzioni pulite
    prompt = f"""
Translate this Italian text into:

1) English
2) Russian (Cyrillic)

Italian text:
{text}

Answer in this format:

English: <translation>
Russian: <translation>
"""

    # Invia il prompt a Ollama no temperartura per essere più precisi
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=30  # evita che l'app si blocchi se Ollama non risponde arrestando il processo entro 30secondi
    )

    # Se Ollama dà errore → ritorna vuoto
    if response.status_code != 200:
        return {"english": "", "russian": ""}

    # Testo generato dal modello
    output = response.json().get("response", "")

    # Variabili per le due traduzioni
    english = ""
    russian = ""

    # Cerchiamo le righe che iniziano con "English:" o "Russian:"
    for line in output.splitlines():
        l = line.strip()

        if l.lower().startswith("english:"):
            english = l.split(":", 1)[1].strip()

        if l.lower().startswith("russian:"):
            russian = l.split(":", 1)[1].strip()

    # Restituiamo le due traduzioni 
    return {"english": english, "russian": russian}

#INFO POINT

def ask_about_bari(question: str) -> str:
    """Risponde a domande sulla città di Bari, in italiano."""

    # Prompt che rende il modello in una "guida turistica di Bari"
    prompt = f"""
Sei una guida turistica esperta della città di Bari.
Rispondi SOLO in italiano.
Usa un linguaggio semplice e corretto.

Domanda:
{question}

Risposta:
"""

    # Chiediamo la risposta a Ollama
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=30  # protezione 
    )

    # Se c'è un problema con Ollama → ritorna messaggio di errore
    if response.status_code != 200:
        return "Errore nel modello."

    # Restituiamo direttamente il testo generato dal modello
    return response.json().get("response", "").strip()
