import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = os.environ['OPENAI_ORGANISATION_ID']
openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.Image.create(
    prompt="A beautiful image of a painting to be used on a birthday card",
    n=2,
    size=os.environ['OPENAI_IMAGE_SIZE_1024_1024']
)

# response = openai.Completion.create(
#     model="text-davinci-003", prompt="write a beautiful birthday message to be printed on a birthday card")

print(response.data[0].url)
