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


    response = execute_graph(user_message)


    history.append({
        "role": "assistant",
        "content": response
    })

    return history, ""




with gr.Blocks(title="Chamikara Personal Assistant") as ui:
    gr.Markdown(
        """
        # 🤖 My Personal Assistant

        A multi-agent AI assistant that can:
        -  Answer general questions
        -  Help with writing
        -  Summarize news
        -  Detect scams

        Type your message below 
        """
    )

    chatbot = gr.Chatbot(
        label="Conversation",
        height=400
    )

    with gr.Row():
        user_input = gr.Textbox(
            placeholder="Write a professional email | Is this a scam? | Latest news",
            lines=2
        )
        send_btn = gr.Button("Send")

    send_btn.click(
        chat,
        inputs=[user_input, chatbot],
        outputs=[chatbot, user_input]
    )

    user_input.submit(
        chat,
        inputs=[user_input, chatbot],
        outputs=[chatbot, user_input]
    )

ui.launch()
