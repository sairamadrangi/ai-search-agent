from dotenv import load_dotenv
load_dotenv()
from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.checkpoint.memory import MemorySaver
from langchain_groq import ChatGroq
from langchain.agents import create_agent

llm = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()
memory = MemorySaver()

agent = create_agent(
    model=llm,
    tools=[search.run],
    system_prompt="You are an agent that can search any question on Google.",
    checkpointer=memory
)

while True:
    query = input("user: ")
    if query.lower() == "quit":
        print("good bye")
        break

    response = agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}}
    )
    print("AI:", response["messages"][-1].content)
#question="which party won the elections of taminadu in 2026 ? "
#response = agent.invoke({"messages":[{"role":"user","content":query}]})
#print("AI",response["messages"][-1].content)