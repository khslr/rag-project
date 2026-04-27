from openai import OpenAI
from dotenv import load_dotenv
import os

# .env laden
load_dotenv()

# Client erstellen
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
Du bist ein präziser Assistent.
Fasse den folgenden Text in 5 Bulletpoints auf Deutsch zusammen:

Künstliche Intelligenz wird in Unternehmen zunehmend eingesetzt, um repetitive
Aufgaben zu automatisieren, Wissen schneller zugänglich zu machen und Analysen
zu beschleunigen. Gleichzeitig steigen die Anforderungen an Governance,
Datenschutz und Nachvollziehbarkeit.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)
