# Tasks: task.py - Defining the Jobs for Your Agents : 
  # research_task: This task is assigned to the News_researcher. It describes the task of identifying the next big trend in a specific topic, analyzing its pros and cons, and providing a comprehensive report.
    #              It also specifies the tools and the expected output.
  # write_task: This task is assigned to the News_writer. It describes the task of composing an insightful article based on the research findings, focusing on the latest trends and the impact on the industry. 
    #           It includes details about the output format and file name.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tasks : 
  # Each agent is given a specific task to perform.
  # For every Agent we have to create some kind of task
  # task is also similar like how we done the agents 
# -------------------------------------------------------------------------------------------------------------------------------------------


# import the Task class from crewai, your custom tools (Tool), and the agents you defined (News_researcher, News_writer).
from crewai import Task
from tools import Tool
from agents import News_researcher, News_writer

# Research task
research_task = Task(          # Used Task Class
  description=(                # description: This is the core of the task. It provides detailed instructions for the assigned agent on what to do. It's written in a way that the AI can understand, similar to how you'd give instructions to a human.
    #                          # In the research_task, the description tells the researcher to:                                                                             
    "Identify the next big trend in {topic}."                                                  # Identify the next big trend in the specified topic.
    "Focus on identifying pros and cons and the overall narrative."                            # Focus on identifying both the pros and cons of the trend.
    "Your final report should clearly articulate the key points,"                         
    "its market opportunities, and potential risks."                                           # Present a comprehensive report outlining the key points, market opportunities, and potential risks.
  ),

  # expected_output: This parameter defines what the agent is expected to produce. It provides a clear guide for the agent on the format and content of the output.
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',       # The research_task expects: A comprehensive report, 3 paragraphs long, about the latest AI trends.
  
  tools=[Tool],                   # This parameter specifies the tools that the assigned agent can use to complete the task. Both tasks have [Tool], which means they can access the SerperDevTool to search the internet.
  
  agent=News_researcher,          # This parameter directly assigns the task to a specific agent.
  # research_task is assigned to News_researcher, making the researcher responsible for fulfilling this task.
)



# Writing task with language model configuration
write_task = Task(
  description=(                                  # In the write_task, the description instructs the writer to:
    "Compose an insightful article on {topic}."                                                             # Compose an insightful article about the topic.
    "Focus on the latest trends and how it's impacting the industry."                                       # Focus on the latest trends and how they are impacting the industry.
    "This article should be easy to understand, engaging, and positive."                                    # Ensure the article is easy to understand, engaging, and positive.
  ),

  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',                  # The write_task anticipates: A 4 paragraph article on the topic advancements, formatted as Markdown.
  tools=[Tool],
  agent=News_writer,

  async_execution=False,            # This parameter (only used in write_task) controls whether the task should be executed asynchronously (in parallel with other tasks) or sequentially.
#                                     False means the task will be executed one after the other, which is how the code is set up.

  output_file='new-blog-post.md'    # This parameter (only used in write_task) specifies the name of the file where the agent should save its output.
#                                     'new-blog-post.md' means the output will be written to a file named "new-blog-post.md" in the same directory as your code.
#                                    Example of output customization
)