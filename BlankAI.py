Main module = 0
Therapy module = 1
Counter-Argument Module =  2

import openai

import sys
import time
import datetime

def chat_openai(prompt) -> dict:
    description = " "
    conversation = [{'role': 'system', 'content': description}, 
                    {'role': 'user', 'content': prompt}]
    response, answer = None, ''
    api_key = 'API Key'  # Replace with your actual API key

    while True:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model='', # ChatGPT Model
                messages=conversation,
                temperature=0.7,
                max_tokens=500,
                n=1,
                stop=None
            )
            answer = response.choices[0].message.content
            conversation.append({'role': 'System', 'content': answer})
            break  
        except openai.error.TooManyRequestsError as e:
            print("API rate limit reached. Waiting for a moment...")
            time.sleep(10)  
        except Exception as e:
            print(f"Error with API key {api_key}: {e}")
            break

    if response:
        return {'answer': answer, 'conversation': conversation, 'response': response}
    else:
        raise Exception("API request failed")

def safe_print(data):
def AI_Print:
    user_prompt = input("")
    print()


    while True:
        test = chat_openai(user_prompt)
        response = test['answer']

        if response:
            safe_print(response)



            user_prompt = input("User: ")  # Get user input to continue the conversation
                break
        else:
            break

    log_file.close()  # Close the log file


AI_Print()


