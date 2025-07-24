# # Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# # OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI

# # Load environment variables from .env
# load_dotenv()

# # Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o")

# # Invoke the model with a message
# result = model.invoke("What is 81 divided by 9?")
# print("Full result:")
# print(result)
# print("Content only:")
# print(result.content)


# Chat Model Documents:
# Gemini Pro: https://python.langchain.com/v0.2/docs/integrations/chat/google_palm/
# OpenAI: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI GPT-4o
openai_model = ChatOpenAI(model="gpt-4o")

# Initialize Gemini Pro
gemini_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Prompt
prompt = "What is 81 divided by 9? Explain the steps in detail."

# OpenAI result
# openai_result = openai_model.invoke(prompt)
# print("OpenAI Result:")
# print(openai_result)
# print("OpenAI Content:")
# print(openai_result.content)

# Gemini Pro result
gemini_result = gemini_model.invoke(prompt)
print("\nGemini Pro Result:")
print(gemini_result)
print("Gemini Pro Content:")
print(gemini_result.content)
