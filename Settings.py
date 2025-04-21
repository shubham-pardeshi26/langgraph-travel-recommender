from decouple import config
from tavily import TavilyClient
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser

class Settings():
    def __init__(self):
        self.tavily_api_key = config("TAVILY_API_KEY")
        self.langsmith_api_key = config("LANGSMITH_API_KEY")
        self.ls_project_name = config("LANGSMITH_PROJECT")
        self.openai_api_key = config("OPENAI_API_KEY")
        self.langsmith_tracing = config("LANGSMITH_TRACING")
        self.langsmith_endpoint = config("LANGSMITH_ENDPOINT")
        self.travily_client = TavilyClient(api_key=self.tavily_api_key)
        self.llm = ChatOpenAI(temperature=0.3)
        self.parser = JsonOutputParser()
        
env_creds = Settings()