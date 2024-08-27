import os
from groq import Groq

# Acessa a API Key da variável de ambiente
api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Ta no Git HUB PROFESSOR",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
