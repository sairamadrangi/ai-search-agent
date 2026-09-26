# Search-Enabled AI Agent with Memory

An autonomous AI agent that combines **real-time web search** with **persistent conversational memory**, built using **LangChain**, **LangGraph**, and **Groq**.

## Features
- Autonomous tool-use: agent decides when to search the web
- Real-time Google search via Serper API
- Persistent memory across conversation turns using LangGraph's `MemorySaver`
- Fast inference using Groq-hosted `gpt-oss-20b`

## Tech Stack
- Python
- LangChain (`create_agent`)
- LangGraph (`MemorySaver`)
- Groq API
- Google Serper API

## Setup

1. Install dependencies
```bash
   pip install langchain-groq langchain-community langgraph python-dotenv
```

2. Create a `.env` file:
    GROQ_API_KEY=your_groq_key
    GOOGLE_SERPER_API_KEY=serper_api
   Run the agent
```bash
   python app.py
```

3. Run the agent
```bash
   python app.py
```

## Usage
Ask any question in the terminal. The agent will decide whether to use the search tool and will remember context within the same thread. Type `quit` to exit.

## How It Works
The agent is built with LangChain's `create_agent`, given access to a Serper-powered search tool, and wrapped with a `MemorySaver` checkpointer so conversation state persists across turns within a `thread_id`.

## License
MIT
