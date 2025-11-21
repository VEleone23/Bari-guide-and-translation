import gradio as gr
from translator import translate, ask_about_bari

def ui_translate(text):
    result = translate(text)
    return result["english"], result["russian"]

def ui_bari_info(question):
    return ask_about_bari(question)


# Tema compatibile con tutte le versioni di Gradio installate
THEME = gr.themes.Soft().set(
    body_background_fill="#f5f7fa",
    block_background_fill="#ffffff",
    button_primary_background_fill="#bb999f",
    button_primary_background_fill_hover="#4580c3",
    button_primary_text_color="#ffffff",
)

with gr.Blocks(theme=THEME) as demo:

    # HEADER 
    gr.Markdown(
        """
        <div style="text-align:center; 
                    font-size: 30px; 
                    font-weight: bold; 
                    padding: 15px;">
            ⛪🏰🌊🐙  Traduttore & Guida di Bari  🐙🌊🏰⛪
        </div>
        """,
    )

    # -----------------------
    # SEZIONE TRADUZIONE
    # -----------------------
    gr.Markdown(
        """
        ### 🌐 Traduzione Italiano → Inglese / Russo
        """,
    )

    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(label="Testo in italiano", lines=4)
            translate_button = gr.Button("🌍 Traduci")

        with gr.Column(scale=1):
            output_en = gr.Textbox(label="Inglese", lines=3)
            output_ru = gr.Textbox(label="Russo", lines=3)

    translate_button.click(
        fn=ui_translate,
        inputs=input_text,
        outputs=[output_en, output_ru]
    )


    # -----------------------
    # SEZIONE INFO SU BARI
    # -----------------------
    gr.Markdown(
        """
        ### 🐙 Informazioni sulla città di Bari
        """,
    )

    with gr.Row():
        with gr.Column(scale=1):
            bari_question = gr.Textbox(label="Domanda sulla città", lines=3)
            info_button = gr.Button("📘 Chiedi alla guida")

        with gr.Column(scale=1):
            bari_answer = gr.Textbox(label="Risposta", lines=5)

    info_button.click(
        fn=ui_bari_info,
        inputs=bari_question,
        outputs=bari_answer
    )

demo.launch(server_name="127.0.0.1", server_port=7865, inbrowser=False)

