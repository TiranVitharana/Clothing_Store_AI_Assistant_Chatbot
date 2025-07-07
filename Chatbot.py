import os 
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv (override = True)
google_api_key = os.getenv("GOOGLE_API_KEY")
model = "gemini-2.5-flash-preview-05-20"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

system_message = "You are a helpful assistant in a clothes store. You should try to gently encourage \
the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a hat', \
you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales event.'\
Encourage the customer to buy hats if they are unsure what to get. If customer asks about kids clothing, tell him that \
there are wide varities of kids cloths available and encourage him or her to try them out"

price_list = {
    "Classic Hat": "$12 (60% off)",
    "Wool Beanie": "$10 (60% off)",
    "Signature Trousers": "$20 (50% off)",
    "Denim Jacket": "$35 (50% off)",
    "Striped Shirt": "$15 (50% off)",
    "Casual Hoodie": "$25 (50% off)",
    "Summer Dress": "$22 (50% off)",
    "Kids T-Shirt": "$8 (50% off)",
    "Kids Jeans": "$14 (50% off)",
    "Kids Hoodie": "$16 (50% off)"
}

system_message += str(price_list)

system_message += "If user rasks about trousers you can say something like 'We have branded trousers just for you\
wanna take a look?', and if user agrees you can show the list of trosers with prices and discounted price according to the provided discounts above."

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    stream = gemini.chat.completions.create(
        model = model,
        messages = messages,
        stream = True 
    )

    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

gr.ChatInterface (fn = chat, type = "messages").launch()