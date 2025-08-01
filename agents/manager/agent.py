from google.adk import Agent
from tools import gmail_auth

model_id = "gemini-2.5-flash"

#get_profle sub-agent
get_profile_agent = Agent(

)

root_agent = Agent(
    name="manager",
    global_instruction= """You are a helpful virtual assistant for a company. Always respond politely.""",
    description="Manager agent that coordinates tasks and manages sub-agents.",
    instruction="""You are the main agent that is responsible for overseeing the work of other agents.
    Your role is to understand spoken commands, extract necessary details,  validate them, and delegate the task to required sub-agent.
    IMPORTANT: Always delegate the task to the appropriate agent. Use your best judgement to determine
    which agent to delegate to.
    You have access to following sub-agent:
    -get_profile_agent
    You have access to following tools:
    -
    -get_current_time
    """,
    model=model_id,
    sub_agents = [get_profile_agent]
)