# Import required libraries
from swarm import Swarm, Agent
import os 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Swarm client
client = Swarm()

# Define specialized financial agents

# 1. Risk Management Agent
risk_management_agent = Agent(
    name="Risk Management Agent",
    instructions="""
        This agent focuses on protecting the user's financial well-being.
        Using the insurance and asset information provided by the Orchestrator,
        it evaluates overall financial risks, analyzes existing coverage,
        and identifies any protection gaps.
        
        The Risk Management Agent recommends appropriate insurance products,
        suggests asset protection strategies, and advises on contingency planning.
        It helps ensure financial stability in the face of unexpected events,
        regularly updating the Orchestrator with risk assessments and mitigation strategies.
    """,
)

# 2. Investment Strategy Agent
investment_strategy_agent = Agent(
    name="Investment Strategy Agent",
    instructions="""
        This agent handles all aspects of the user's investment portfolio.
        Based on the current investment information received from the Orchestrator,
        it assesses risk tolerance, sets investment goals, and recommends asset allocation strategies.
        
        The Investment Strategy Agent monitors market trends, suggests portfolio adjustments,
        and analyzes various investment opportunities across different asset classes.
        It aims to optimize returns while managing risk,
        consistently updating the Orchestrator with its findings and recommendations.
    """,
)

# 3. Budget Analysis Agent
budget_analysis_agent = Agent(
    name="Budget Analysis Agent",
    instructions="""
        This agent focuses on day-to-day financial management.
        Using the income and expense data provided by the Orchestrator,
        it analyzes spending patterns and creates detailed budgets.
        
        The Budget Analysis Agent identifies potential savings opportunities,
        suggests ways to optimize cash flow, and provides accurate financial projections.
        It continually monitors transactions to ensure alignment with the user's budget and financial goals,
        feeding updates back to the Orchestrator for comprehensive planning.
    """,
)

# Define transfer functions for agent-specific tasks

def transfer_to_budget_agent():
    """
    Transfer to questions/information related to Budget/Expense management.
    """
    return budget_analysis_agent

def transfer_to_investment_agent():
    """
    Transfer to questions/information related to Investment strategy management.
    """
    return investment_strategy_agent

def transfer_to_risk_agent():
    """
    Transfer to questions/information related to Insurance/Risk management.
    """
    return risk_management_agent

# Orchestrator Agent - central hub for managing all other agents
financial_planning_orchestrator_agent = Agent(
    name="Financial Planning Orchestrator Agent",
    instructions="""
        This agent serves as the system's central hub and initial point of contact.
        It begins by thoroughly gathering information about the user's current financial situation,
        including investments, income sources, expenses, and existing insurance policies.
        
        Once a comprehensive financial profile is established, the agent distributes relevant data
        to the specialized agents for detailed analysis.
        
        After receiving insights from other agents, it synthesizes the information to provide cohesive,
        personalized financial advice. The Orchestrator prioritizes tasks, manages inter-agent communication,
        and translates complex financial data into actionable, easy-to-understand guidance for the user.
    """,
    functions=[transfer_to_budget_agent, transfer_to_investment_agent, transfer_to_risk_agent]
)
