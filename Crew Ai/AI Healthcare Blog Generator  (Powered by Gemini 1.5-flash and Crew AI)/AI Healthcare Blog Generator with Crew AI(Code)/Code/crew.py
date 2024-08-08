# Understanding Crew AI
  # Crew AI is a framework designed to build "crews" of intelligent agents, each with specific roles and skills, to work together on complex tasks.
  # The agents are powered by large language models (LLMs) like Gemini, enabling them to understand natural language, access information, and reason.
# ----------------------------------------------------------------------------------------------------------------------------------------------------


#  import the Crew, Process classes from crewai, the tasks (research_task, write_task), and the agents (News_researcher, News_writer).
from crewai import Crew, Process
from task import research_task, write_task
from agents import News_researcher, News_writer

## Forming the tech focused crew with some enhanced configuration
# create a Crew object named crews, which combines the agents and tasks.
crews = Crew(
    agents =  [News_researcher, News_writer],                       # 1st parameter[agents] :  A list of agents that will participate in the crew.(requierd is need all the agent)
    tasks = [research_task, write_task],                            # 2nd parameter[task] : requier is kind of task that we want to execute based on the agents( A list of tasks that need to be completed.)
    process = Process.sequential,                                   # 3rd parameter[Process]Process.sequential : Specifies how the agents and tasks will interact. In this case, Process.sequential means that the agents will perform tasks one after another in the order they are defined.
)


## starting the task execution process with enhanced feedback
# Crew Kickoff: Finally, you kick off the crew's work by calling crews.kickoff(). This starts the execution process. You provide an input dictionary {'topic':'AI In Healthcare'} that specifies the topic for the crew to work on.
results = crews.kickoff(inputs={'topic':'AI In Healthcare'})
print(results)


