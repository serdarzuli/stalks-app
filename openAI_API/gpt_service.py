"""from openai import OpenAI
from OpenAI.config import HEADERS, OPENAI_API_KEY
import json

class GptService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        # self.headers = HEADERS
    
    async def get_response_from_gpt(self):
        
        client = OpenAI()
        prompt = "hey gpt how are you, what is today?"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": prompt,
            }],
            temperature=0,
        )
        content = response.choices[0].message.content
        response_data = json.loads(content)
        print(response_data)
        print(response._request_id)"""