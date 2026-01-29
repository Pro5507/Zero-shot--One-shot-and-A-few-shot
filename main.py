from google import genai
from google.genai import types
import config

client = genai.Client(api_key=config.GEMINI_API_KEY)

def generate_response(prompt, temperature=0.3):
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
category = input("Enter a categort (e.g., animal, food, city): ")
item = input(f"Enter a specific {category} to classify: ")
print("\n---ZERO-SHOT LEARNING---")
zero_shot = f"Is {item} a {category}? Answer yes or no."
print(f"Prompt: {zero_shot}")
print(f"Response: {generate_response(zero_shot)}")
print("\n---ONE-SHOT LEARNING---")
one_shot = f"""Determine if the item belongs to the category.

Example:
Category: fruit
Item: Apple
Answer: Yes, apple is a fruit.

Now you try:
Category: {category}
Item: {item}
answer:"""
print(f"Response: {generate_response(one_shot)}")

print("\n---FEW-SHOT LEARNING---")
few_shot = f"""Determine if the item belongs to the category.

Example1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Example 2:
"""