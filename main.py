from typing import Optional

import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File

import uvicorn

from PIL import Image
from io import BytesIO

genai.configure(api_key="AIzaSyA0gMN7n2qkJqU6Owoxx55rZJkWNiiOQbA")

app = FastAPI()

model = genai.GenerativeModel("gemini-pro-vision")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate_response")
async def generate_response(image: UploadFile = File(...)):

    image_contents = await image.read()
    image_pil = Image.open(BytesIO(image_contents))
    input_text = 'Crie uma descrição de anúncio em pt-BR irresistível para o produto na imagem, focando em: Que problema ele resolve? Quais são seus 3 principais benefícios? Quais características o tornam único? Inclua detalhes específicos sobre materiais, dimensões, cores, etc. Termine com uma chamada para ação persuasiva.'
    response = model.generate_content((input_text, image_pil))
    return response.text
