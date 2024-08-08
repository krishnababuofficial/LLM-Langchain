# Agents: agents.py - Creating the AI Workers. 
  # The foundation of Crew AI is the creation of agents. Agents are like specialized AI workers, each with a defined role, a set of tools, and an LLM to help them reason and act.
  # News_researcher: This agent focuses on research, uncovering the latest trends in a given topic (in this case, "AI in Healthcare"). It uses tools like Serper Dev to search the internet, gathers information, and then analyzes it to draw conclusions.
  # News_writer: This agent is tasked with crafting engaging blog posts based on the information provided by the researcher.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



from crewai import Agent                                      # Imports the Agent class from crewai to define your AI agents
from dotenv import load_dotenv
load_dotenv()                                                 # load environment variables from a .env file for security. (like your Google API key).
import os                                                     # for interacting with the operating system and environment variables
from tools import Tool                                        # tools for your custom tools (Tool, which is SerperDevTool in this case).
from langchain_google_genai import ChatGoogleGenerativeAI   # to access Google's Gemini LLM.

## Call Gemini model (Google's Large Language Model)
# With help of this entier llm model we will be using this while we create our Agents.

llm = ChatGoogleGenerativeAI(                          # create a ChatGoogleGenerativeAI instance called llm, which is your primary AI model (Gemini-1.5-flash). You configure the model settings:
    model = "gemini-1.5-flash",                           # model: The specific Gemini model to use.
    verbose = True,                                       # verbose: Whether to print detailed LLM interactions.
    temperature = 0.5,                                    # temperature: Controls the creativity and randomness of the LLM's responses.
    google_api_key = os.getenv("GOOGLE_API_KEY"))         # google_api_key: Your Google API key for authentication.


# Agents: Here we define two agents:
# Creating a Senior Researcher Agent
    # News_researcher: This agent is designed to conduct research. Its role is "Senior Researcher," its goal is to uncover groundbreaking technologies, and it has tools like Tool (SerperDevTool) to help it search and analyze information.
    # It's set to verbose so you can see its steps, memory so it remembers past interactions, and it has a backstory to give it a persona. It can also delegate tasks to other agents.
    # or i can say this will be a news reporter which will be responsible in getting all the news details.

News_researcher = Agent(
    role = "Senior Researcher",                                       # The agent's role
    goal = "Unccover ground breaking technologies in {topic}",        # The agent's objective     
    verbose = True,                                                   # Show detailed agent actions
    memory=True,                                                      # Store past interactions for context
    backstory=(                                            # Give the agent a personality/context
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools = [Tool],                                   # The tools the agent can use (SerperDevTool)
    llm=llm,                                          # The LLM powering the agent
    allow_delegation = True   # Because i want this agent to communicate with other agent /  # Can this agent delegate tasks? - [True] (Yes)

)
# This person is responsible fore creating the New we will create another Agent(Person)


## creating a write agent with custom tools responsible in writing news blog
    # News_writer: This agent focuses on writing. Its role is "Writer," its goal is to create compelling tech stories, and it has similar settings as the researcher.
    # Importantly, allow_delegation is set to False because writers generally don't delegate tasks.

# Writer Agent
News_writer = Agent(
  role = 'Writer',
  goal = 'Narrate compelling tech stories about {topic}',
  verbose = True,
  memory = True,
  backstory = (
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools = [Tool],               # SerperDevTool
  llm = llm,
  allow_delegation = False      # False, Because once the research is done and come to the writer, its responsible of writer to probably write the entire blog
)
