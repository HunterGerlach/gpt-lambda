import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):

    # Set up the OpenAI API client
    openai.api_key = os.environ.get('API_KEY')

    # Set the input string and additional context
    input_string = "Say hello to " + event["first_name"] + " " + event["last_name"]
    context = "Famous movie character"

    # Use the OpenAI API client to generate a response from GPT-3
    engines=["text-ada-001", "text-babbage-001", "text-curie-001", "text-davinci"]
    
    response = openai.Completion.create(
        engine=engines[0],
        prompt=input_string + context,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the response from GPT-3
    print(response["choices"][0]["text"])
     
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'input': input_string,
        'context': context,
        'response': response
    }
