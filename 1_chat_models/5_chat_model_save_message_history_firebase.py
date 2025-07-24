# Example Source: https://python.langchain.com/v0.2/docs/integrations/memory/google_firestore/

from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

"""
Steps to replicate this example:
1. Create a Firebase account
2. Create a new Firebase project
    - Copy the project ID
3. Create a Firestore database in the Firebase project
4. Install the Google Cloud CLI on your computer
    - https://cloud.google.com/sdk/docs/install
    - Authenticate the Google Cloud CLI with your Google account
        - https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
    - Set your default project to the new Firebase project you created
5. Enable the Firestore API in the Google Cloud Console:
    - https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com&project=crewai-automation
"""


"""
The error you're seeing:

```
google.auth.exceptions.DefaultCredentialsError: Your default credentials were not found.
```

means that the Google Cloud SDK cannot find **Application Default Credentials (ADC)** to authenticate your Firebase/Firestore client.

### ✅ To fix this:

You need to set up your environment with proper credentials.

---

### 🔧 **Option 1: Use a service account key (recommended for development)**

1. Go to: [https://console.cloud.google.com/](https://console.cloud.google.com/)

2. Navigate to:

   ```
   IAM & Admin > Service Accounts
   ```

3. Select or create a **service account**, and then click:

   ```
   Keys > Add Key > Create new key (JSON)
   ```

4. Download the JSON file.

5. Set the environment variable to use that key:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
   ```

6. Run your script again:

   ```bash
   python 1_chat_models/5_chat_model_save_message_history_firebase.py
   ```

---

### ✅ **Option 2: Use `gcloud auth application-default login` (for user-based credentials)**

This is easier for quick development if you have `gcloud` CLI installed:

```bash
gcloud auth application-default login
```

It will open a browser for you to log in and create default user credentials locally.

Then try running your script again.

---

Let me know if you want me to walk you through either option step-by-step.

"""

load_dotenv()

# Setup Firebase Firestore
# PROJECT_ID = "langchain-demo-abf48"
PROJECT_ID ="langchainlearningproject-38d71"
SESSION_ID = "user_session_new"  # This could be a username or a unique ID
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize Chat Model
# model = ChatOpenAI()
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    client_options=None,
    transport=None,
    additional_headers=None,
    client=None,
    async_client=None
)
print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    # Ensure ai_response.content is a string before adding to chat history
    ai_message_content = ai_response.content
    if not isinstance(ai_message_content, str):
        ai_message_content = str(ai_message_content)
    chat_history.add_ai_message(ai_message_content)

    print(f"AI: {ai_response.content}")
