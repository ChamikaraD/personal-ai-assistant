import gradio as gr
from app import execute_graph


def chat(query: str):
    return execute_graph(query)


ui = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask about news, scams, or anything else..."
    ),
    outputs=gr.Textbox(
        lines=10,
        label="Assistant Response"
    ),
    title="Chamikara Personal Assistant",
    description="Type anything you like. News queries are summarized automatically."
)

ui.launch()
