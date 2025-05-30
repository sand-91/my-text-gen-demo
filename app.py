import gradio as gr
from transformers import pipeline

# Load a text-generation model
generator = pipeline("text-generation", model="gpt2")

# Define the function for the Gradio interface
def generate_text(prompt):
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return result[0]["generated_text"]

# Create Gradio interface
interface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Textbox(label="Generated Text"),
    title="Text Generation App",
    description="Enter a prompt to generate text using GPT-2."
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
