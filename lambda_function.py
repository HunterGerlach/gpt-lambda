import json
import openai
from api_secrets import API_KEY


# Needed to become lambda
#def lambda_handler(event, context):

# Set up the OpenAI API client
openai.api_key = API_KEY

# Set the input string and additional context
input_string = "The quick brown fox jumps over the lazy dog"
context = "The fox is cunning and the dog is sleepy."

# Use the OpenAI API client to generate a response from GPT-3
response = openai.Completion.create(
    engine="text-ada-001",
    prompt=input_string + context,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response from GPT-3
print(response["choices"][0]["text"])
     
    
    # Needed to become lambda
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!'),
    #     'input': input_string,
    #     'context': context,
    #     'response': response
    # }
