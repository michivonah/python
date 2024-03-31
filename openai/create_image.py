from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

response = client.images.generate(
  model="dall-e-2",
  prompt="a picture with two mammoths, one with light fur and the other with brown fur, 3d art",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)