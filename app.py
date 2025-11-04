import os
from dotenv import load_dotenv  
from groq import Groq  

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        },
    ],
    model="llama-3.3-70b-versatile",  # Changed from llama-3-3-70b to llama-3.3-70b
    max_tokens=500,
    temperature=0.3,
    top_p=1,
)

print(chat_completion.choices[0].message.content)


