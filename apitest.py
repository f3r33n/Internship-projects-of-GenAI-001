from google import genai

client_creation = genai.Client
the_response = client_creation.models.generate_content(
model = "gemini-2.5-flash",
config = {"temperature" :2.0},
contents = "tell me a fact about sleep in one sentence"
)
answer =the_response.text
print(answer)