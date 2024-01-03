from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import openai
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']



llm = OpenAI()
chat_model = ChatOpenAI()

llm.predict("hi!")

chat_model.predict("hi!")