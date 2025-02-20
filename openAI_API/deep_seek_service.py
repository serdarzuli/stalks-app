from openai import OpenAI
from .config import BASE_URL_ROUTER_API, OPENROUTER_API_KEY


class DeepSeekService:
    async def chat_deep_seek(self):
        client = OpenAI(api_key=OPENROUTER_API_KEY, base_url=BASE_URL_ROUTER_API)

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",   
            messages=[
                {
                   "role": "user",
                   "content": "What is the meaning of life?"
                }
            ]
        )

        print(response.choices[0].message.content)