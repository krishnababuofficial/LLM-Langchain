# tools.py - Providing the Agents with Resources
# Tool Initialization: You initialize a SerperDevTool object named Tool, which is essential for your agents to perform internet searches using the Serper API. 
#                      You also set the SERPER_API_KEY environment variable from your .env file to authenticate with the Serper API.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# To get Serper API KEY - singup = https://serper.dev/

# Import load_dotenv to load environment variables, os for operating system interaction, and SerperDevTool from the crewai_tools library.
from dotenv import load_dotenv
load_dotenv()
from crewai_tools import SerperDevTool
import os
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the tool for internet searching capabilities
Tool = SerperDevTool()                                      


# Can get the code from documentation - https://docs.crewai.com/tools/SerperDevTool/#description
# W.R.To tool this is one of the example you can use any tool that you want again from the Crew Documentation

# we are going to use this specific tool which is Seper Dev 
# now the same tool i have call in the agent.py
