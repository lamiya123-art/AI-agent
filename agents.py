import asana
from asana.rest import ApiException

from google import genai
from google.genai import types

from dotenv import load_dotenv
from datetime import datetime

import os
import json


# ---------------- LOAD ENV ----------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = "gemini-2.5-flash-lite"

print("connected successfully")


# ---------------- ASANA SETUP ----------------

configuration = asana.Configuration()
configuration.access_token = os.getenv("ASANA_ACCESS_TOKEN")

api_client = asana.ApiClient(configuration)

tasks_api = asana.TasksApi(api_client)



# ---------------- ASANA FUNCTION ----------------

def create_asana_task(task_name, due_on="today"):
    """
    Create task inside Asana
    """

    if due_on == "today":
        due_on = str(datetime.now().date())


    task_body = {
        "data": {
            "name": task_name,
            "due_on": due_on,
            "projects": [
                os.getenv("ASANA_PROJECT_ID")
            ]
        }
    }


    try:
        response = tasks_api.create_task(
            task_body,
            {}
        )
        task = response
        return (
        f"✅ Task created successfully!\n\n"
        f"📌 Task: {task['name']}\n"
        f"📅 Due Date: {task['due_on']}\n"
        f"🔗 Link: {task['permalink_url']}"
    )


    except ApiException as e:
        return f"Asana Error: {e}"



# ---------------- GEMINI TOOL ----------------

asana_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="create_asana_task",
            description="Creates a task in Asana",
            parameters={
                "type": "OBJECT",
                "properties": {
                    "task_name": {
                        "type": "STRING",
                        "description": "Task name"
                    },

                    "due_on": {
                        "type": "STRING",
                        "description":
                        "Due date YYYY-MM-DD"
                    }
                },

                "required": [
                    "task_name"
                ]
            }
        )
    ]
)



# ---------------- AI FUNCTION ----------------

def prompt_ai(messages):

    try:
        response = client.models.generate_content(
            model=model,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[asana_tool]
            )
        )

    except Exception as e:
        return f"AI service error: {e}"


    candidate = response.candidates[0]

    parts = candidate.content.parts


    # check function call
    for part in parts:

        if part.function_call:


            function_name = (
                part.function_call.name
            )

            args = (
                part.function_call.args
            )


            if function_name == "create_asana_task":

                result = create_asana_task(
                    **args
                )


                return (
                    "Task created successfully\n\n"
                    + result
                )


    return response.text




# ---------------- MAIN CHAT ----------------

def main():

    messages = []


    system_prompt = (
        "You are a personal assistant "
        "that manages Asana tasks. "
        f"Today's date is {datetime.now().date()}"
    )


    messages.append(
        {
            "role": "user",
            "parts": [
                {
                    "text": system_prompt
                }
            ]
        }
    )



    while True:

        user_input = input(
            "Chat with me( q to quit): "
        ).strip()


        if user_input.lower() == "q":
            break



        messages.append(
            {
                "role": "user",
                "parts": [
                    {
                        "text": user_input
                    }
                ]
            }
        )



        ai_response = prompt_ai(
            messages
        )


        print(
            ai_response
        )



        messages.append(
            {
                "role": "model",
                "parts": [
                    {
                        "text": ai_response
                    }
                ]
            }
        )



if __name__ == "__main__":
    main()