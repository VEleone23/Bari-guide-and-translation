# translator_debug.py
import requests
import json
import sys
import traceback

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "bari-translator"

def translate_raw(text: str):
    prompt = f"<input>\n{text.strip()}\n</input>"
    try:
        resp = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=30
        )
    except Exception as e:
        print("NETWORK ERROR:", e)
        raise

    print("HTTP status:", resp.status_code)
    try:
        j = resp.json()
    except Exception as e:
        print("RESPONSE JSON PARSE ERROR:", e)
        print("Raw response text:", resp.text[:2000])
        raise

    print("Full JSON keys:", list(j.keys()))
    raw_output = j.get("response", None)
    print("Raw model output (first 2000 chars):\n", (raw_output or "")[:2000])
    return raw_output

def extract_translations(output: str):
    import re
    if not output:
        return {"english": "", "russian": ""}
    en_pat = re.compile(r"English\s*[:\-]\s*(.*?)(?=\n\s*Russian\s*[:\-]|\Z)", re.IGNORECASE | re.DOTALL)
    ru_pat = re.compile(r"Russian\s*[:\-]\s*(.*?)(?=\n\s*English\s*[:\-]|\Z)", re.IGNORECASE | re.DOTALL)
    en = en_pat.search(output)
    ru = ru_pat.search(output)
    english = en.group(1).strip() if en else ""
    russian = ru.group(1).strip() if ru else ""
    print("Parsed English (first 500 chars):", english[:500])
    print("Parsed Russian (first 500 chars):", russian[:500])
    return {"english": english, "russian": russian}

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Il lungomare di Bari è bello al tramonto."
    try:
        raw = translate_raw(text)
        parsed = extract_translations(raw)
        print("\nFINAL RETURNED (formatted):\n")
        print("=== English ===\n", parsed["english"])
        print("\n=== Russian ===\n", parsed["russian"])
    except Exception:
        traceback.print_exc()
