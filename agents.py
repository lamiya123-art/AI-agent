import asana
from asana.rest import ApiException
from OpenAI import OpenAI
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

def create_asana_task( task_name, due_on = "today"):
   """
   reates a task in Asana given the name of the task and when it is due.

    Example call:

    create_asana_task("Test Task", "2024-06-24")

    Args:
        task_name (str): The name of the task in Asana
        due_on (str): The date the task is due in the format YYYY-MM-DD.
                      If not given, the current day is used.

    Returns:
        str: The API response of adding the task to Asana or an error message
             if the API call throws an error.
   """
   if due_on == "today":
        due_on = str(datetime.now().date())

   task_body = {
        "data" : {
        "name" : task_name,
        "due_on" : due_on,
        "projects" : [os.getenv("ASANA_PROJECT_ID", "")]

    }
    }

   try :
        api_reponses = tasks_api_instances.create_task(task_body, {})
        return json.dumps(api_reponses, indent = 2)
   except apiException as e:
        return f"Exception when calling TaskApi: {e}"
   
def get_tools():
    tools = [
            {
                "type": "function",
                "function": {
                    "name": "create_asana_task",
                    "description": "Creates a task in Asana given the name of the task and when it is due",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task_name": {
                            "   type": "string",
                                "description": "The name of the task in Asana"
                        },
                        "due_on": {
                            "type": "string",
                            "description": "The date the task is due in the format YYYY-MM-DD. If not given, the current day is used"
                    }
                },
                "required": ["task_name"]
            },
        },
    }
]
   
#set up a configuration

   

def prompt_ai(messages):
   #prompt the ai  with the user's latest messages
    completion = client.chat.completions.create(
       model = model,
       messages = messages,
       tools = get_tools()
    )
   
    response_messages = completion.choices[0].message
    tool_calls = response_message.tool_calls

    #see if the ai needs to invoke a tool
    if tool_calls:
        #if the ai decides to invoke a tool invoke it 
        available_functions = {
            "create_task_asana" : create_asana_task
        }
        #add a response so that the ai knows 
        messages.append(response_messages)

        #for each tool the ai wants to call, add them and then result to the list of messages 
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            funtion_response = function_to_call(**function_args)
        messages.append({
            "tool_call_id" : tool_call.id,
            "role": tool,
            "name" : function_name,
            "content": funtion_response

        })




        # call the ai again so that it can produce a response with the result of calling tools
        second_response = client.chat.completion.create(
            model = model,
            messages = messages,

        )  

        return second_response.choices [0] .message.content     
    return response_message.content





def main():
    messages = [ {
       "role" : "system",
       "content" : f" You are a personal assistant that helps manage tasks in Asana. The current data is: {datetime.now().data()}"
    }
    ]

    
while True:
    user_input = input("Chat with me( q to quit): ").strip()
    if user_input == "q":
       break

    messages.append({ "role" : "user", "content" : user_input})
    ai_response = prompt_ai(messages)

    print(ai_response)
    messages.append({"role":"assistant","content" :ai_response})


if __name__ == "__main__":
     
     main()