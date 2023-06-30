import os
import openai
from dotenv import load_dotenv

load_dotenv()

# openai initial set up with organisation id and api keys
openai.organization = os.environ['OPENAI_ORGANISATION_ID']
openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.Image.create(
    prompt="An abstract image for a birthday card",
    n=2,
    size=os.environ['OPENAI_IMAGE_SIZE_1024_1024']
)

print(response)
