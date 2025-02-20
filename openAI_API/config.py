import os
from dotenv import load_dotenv

#.env load file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL_GPT_API = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL_ROUTER_API = "https://openrouter.ai/api/v1"
