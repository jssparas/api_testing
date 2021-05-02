from os import environ as env
from dotenv import load_dotenv


load_dotenv('./.env', override=True)
BASE_URL = env.get('BASE_URL', 'http://localhost:8000')
