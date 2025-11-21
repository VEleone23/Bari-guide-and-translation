import jsonlines
import time
from translator import translate

italian_texts = [
    "Il Borgo Antico di Bari è il cuore storico della città.",
    "La Basilica di San Nicola è un luogo di pellegrinaggio internazionale.",
    "Il lungomare di Bari è famoso per le sue viste panoramiche.",
    "La focaccia barese è una delle specialità gastronomiche più amate.",
    "Il Castello Svevo è una fortezza medievale vicino al mare."
]

output_file = "bari_dataset.jsonl"

with jsonlines.open(output_file, mode='w') as writer:
    for idx, text in enumerate(italian_texts):
        print(f"[{idx+1}/{len(italian_texts)}] Traduco...")

        result = translate(text)

        writer.write({
            "id": f"sample_{idx+1}",
            "italian": text,
            "english": result["english"],
            "russian": result["russian"]
        })

        time.sleep(0.5)

print("💾 Dataset generato:", output_file)
