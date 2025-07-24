# LangChain Crash Course - Gemini Edition

**Why does this repo exist?**

Many AI APIs like OpenAI require payment, which can be a barrier for learners and open source enthusiasts. This repo solves that by focusing on Gemini, Google's free API, so anyone can run all the code examples without hitting a paywall. Everything here is open source and runnable out of the box—no credit card required!

Our goal is to provide a fully open source, community-driven resource for:
- Learning how to use LangChain with Gemini step-by-step
- Building your own AI chatbots, RAG systems, and agents
- Sharing and expanding free, practical examples for the community
- Lowering the barrier to entry for AI development

Whether you're a beginner or an experienced developer, this repo is designed to help you get started quickly and contribute back to the ecosystem.

Welcome to the LangChain Crash Course repository! This repo contains all the code examples you'll need to follow along with the LangChain Master Class for Beginners video. By the end of this course, you'll know how to use LangChain to create your own AI agents, build RAG chatbots, and automate tasks with AI.

## Course Outline

1. **Setup Environment**
2. **Chat Models**
3. **Prompt Templates**
4. **Chains**
5. **RAG (Retrieval-Augmented Generation)**
6. **Agents & Tools**

## Getting Started

### Poetry Installation (Step-by-Step)

Poetry is a tool for dependency management and packaging in Python. Follow these steps to install Poetry on your system:

1. **Install Poetry using the official installer:**

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Add Poetry to your PATH:**
   
   By default, Poetry is installed to `$HOME/.local/bin`. Make sure this directory is in your `PATH`.
   
   Add the following line to your `~/.bashrc`, `~/.zshrc`, or equivalent shell config file:
   
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```
   Then reload your shell:
   ```bash
   source ~/.bashrc  # or source ~/.zshrc
   ```

3. **Verify the installation:**

   ```bash
   poetry --version
   ```
   You should see the installed Poetry version.

---

- For more details, see the [Poetry installation guide](https://python-poetry.org/docs/#installation).

### Prerequisites

- Python 3.10 or 3.11
- Poetry (Follow this [Poetry installation tutorial](https://python-poetry.org/docs/#installation) to install Poetry on your system)

### Installation

1. Clone the repository:

   ```bash
   <!-- TODO: UPDATE TO MY  -->
   git clone https://github.com/bhancockio/langchain-crash-course
   cd langchain-crash-course
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install --no-root
   ```

3. Collect your Gemini API key and set up environment variables:

   - Go to the [Google AI Studio](https://aistudio.google.com/app/apikey) and sign in with your Google account.
   - Click "Create API Key" and copy your new Gemini API key.
   - Rename the `.env.example` file to `.env` and update the `GEMINI_API_KEY` variable inside with your key. Example:

   ```bash
   mv .env.example .env
   # Then edit .env and set GEMINI_API_KEY=your-key-here
   ```

4. Activate the Poetry shell to run the examples:

   ```bash
   poetry shell
   ```

5. Run the code examples:

   ```bash
    python 1_chat_models/1_chat_model_basic.py
   ```

## Repository Structure

This project is fully open source and aims to provide a free, community-driven resource for learning LangChain with Gemini. Contributions, suggestions, and new Gemini-based examples are welcome!

Here's a breakdown of the folders and what you'll find in each:

### 1. Chat Models

- `1_chat_model_basic.py`
- `2_chat_model_basic_conversation.py`
- `3_chat_model_alternatives.py`
- `4_chat_model_conversation_with_user.py`
- `5_chat_model_save_message_history_firestore.py`

Learn how to interact with models like ChatGPT, Claude, and Gemini.

### 2. Prompt Templates

- `1_prompt_template_basic.py`
- `2_prompt_template_with_chat_model.py`

Understand the basics of prompt templates and how to use them effectively.

### 3. Chains

- `1_chains_basics.py`
- `2_chains_under_the_hood.py`
- `3_chains_extended.py`
- `4_chains_parallel.py`
- `5_chains_branching.py`

Learn how to create chains using Chat Models and Prompts to automate tasks.

### 4. RAG (Retrieval-Augmented Generation)

- `1a_rag_basics.py`
- `1b_rag_basics.py`
- `2a_rag_basics_metadata.py`
- `2b_rag_basics_metadata.py`
- `3_rag_text_splitting_deep_dive.py`
- `4_rag_embedding_deep_dive.py`
- `5_rag_retriever_deep_dive.py`
- `6_rag_one_off_question.py`
- `7_rag_conversational.py`
- `8_rag_web_scrape_firecrawl.py`
- `8_rag_web_scrape.py`

Explore the technologies like documents, embeddings, and vector stores that enable RAG queries.

### 5. Agents & Tools

- `1_agent_and_tools_basics.py`
- `agent_deep_dive/`
  - `1_agent_react_chat.py`
  - `2_react_docstore.py`
- `tools_deep_dive/`
  - `1_tool_constructor.py`
  - `2_tool_decorator.py`
  - `3_tool_base_tool.py`

Learn about agents, how they work, and how to build custom tools to enhance their capabilities.

## How to Use This Repository

1. **Watch the Video:** Start by watching the LangChain Master Class for Beginners video on YouTube at 2X speed for a high-level overview.

2. **Run the Code Examples:** Follow along with the code examples provided in this repository. Each section in the video corresponds to a folder in this repo.

3. **Join the Community:** If you get stuck or want to connect with other AI developers, join the FREE Skool community [here](https://www.skool.com/ai-developer-accelerator/about).

## Comprehensive Documentation

Each script in this repository contains detailed comments explaining the purpose and functionality of the code. This will help you understand the flow and logic behind each example.

## FAQ

**Q: What is LangChain?**  
A: LangChain is a framework designed to simplify the process of building applications that utilize language models.

**Q: How do I set up my environment?**  
A: Follow the instructions in the "Getting Started" section above. Ensure you have Python 3.10 or 3.11 installed, install Poetry, clone the repository, install dependencies, rename the `.env.example` file to `.env`, and activate the Poetry shell.

**Q: I am getting an error when running the examples. What should I do?**  
A: Ensure all dependencies are installed correctly and your environment variables are set up properly. If the issue persists, seek help in the Skool community or open an issue on GitHub.

**Q: Can I contribute to this repository?**  
A: Yes! Contributions are welcome. Please open an issue or submit a pull request with your changes.

**Q: Where can I find more information about LangChain?**  
A: Check out the official LangChain documentation and join the Skool community for additional resources and support.

## Support

If you encounter any issues or have questions, feel free to open an issue on GitHub or ask for help in the Skool community.

## License

This project is licensed under the MIT License.
