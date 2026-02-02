import gradio as gr
from app import execute_graph


def chat(user_message, history):
    if history is None:
        history = []

    if not user_message.strip():
        return history, ""


    history.append({
        "role": "user",
        "content": user_message
    })

    # Temporary feedback message
    history.append({
        "role": "assistant",
        "content": "🤖 Thinking..."
    })


    response = execute_graph(user_message)


    history[-1] = {
        "role": "assistant",
        "content": response
    }

    return history, ""


with gr.Blocks(title="Personal AI Assistant") as ui:

    # 🔹 HEADER
    gr.Markdown(
        """
        ## 🤖 Personal AI Assistant  

        Ask questions, improve writing, summarize news, or check suspicious messages.
        """
    )

    with gr.Row():
        gr.Markdown(
            "✍️ **Writing help** "
        )
        gr.Markdown(
            "📰 **News summaries**  "
        )
        gr.Markdown(
            "🛡️ **Scam detection**  "
        )

    gr.Markdown("---")


    chatbot = gr.Chatbot(
        label="Conversation",
        height=410
    )

    with gr.Row():
        user_input = gr.Textbox(
            placeholder="Type your message here…",
            lines=2,
            scale=4
        )

        send_button = gr.Button(
            "Send ",
            scale=1,
            elem_id="send-button"
        )

    send_button.click(
        chat,
        inputs=[user_input,chatbot],
        outputs=[chatbot, user_input]
    )

    user_input.submit(
        chat,
        inputs=[user_input, chatbot],
        outputs=[chatbot,user_input]
    )


ui.launch(
    css="""
    #send-button {
        background-color: #ff7a00 !important;
        color: white !important;
        font-weight: 600;
        border-radius: 10px !important;
        min-height: 48px !important;
    }
    h2 {
    text-align: center !important;
    }
    h2 + p {
    text-align: center;
    }
    
    
    strong {
        font-weight: 500;
    }

    #send-button:hover {
        background-color: #e66f00 !important;
    }

    textarea {
        background-color: #1f1f1f !important;
        border: 1px solid #444 !important;
        font-size: 1rem !important;
    }

    textarea:focus {
        border-color: #ff7a00 !important;
        box-shadow: 0 0 0 1px #ff7a00;
    }
    
    """
)
