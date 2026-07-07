import asana
from asana.rest import apiException
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import json
import os

load_dotenv()
client = OpenAI()
model = os.getenv('OPENAI_MODEL', 'gpt-4o')

configuration = asana.Configuration()
configuration.access_token = os.getenv('ASANA_ACCESS_TOKEN', ' ')
api_client = asana.ApiClient(configuration)

tasks_api_instances = asana.TasksApi(api_client)



def main():
    if __name__ == "__main__":
     main()