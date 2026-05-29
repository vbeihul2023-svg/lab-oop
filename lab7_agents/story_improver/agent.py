from google.adk.agents.llm_agent import Agent
from google.adk.agents.loop_agent import LoopAgent
from google.adk.tools.tool_context import ToolContext

MAX_ITERATIONS = 3


def exit_loop(tool_context: ToolContext) -> dict:
    """
    Завершує цикл покращення історії.

    Returns:
        dict: підтвердження завершення
    """
    tool_context.actions.escalate = True
    return {"status": "done", "message": "Історія досягла потрібної якості"}


# Агент-письменник — покращує історію кожну ітерацію
story_writer = Agent(
    model='gemini-2.5-flash',
    name='story_writer',
    description="Покращує історію ітеративно.",
    instruction=f"""
    Ти талановитий письменник. Покращуй або створюй історію за темою.
    З кожною ітерацією роби її більш деталізованою та цікавою.
    Якщо це вже {MAX_ITERATIONS}-та ітерація або історія достатньо гарна,
    викличи функцію exit_loop щоб завершити цикл.
    Відповідай українською мовою.
    """,
    tools=[exit_loop],
)

# Loop агент — повторює покращення до виклику exit_loop
root_agent = LoopAgent(
    name='story_improver',
    description="Ітеративно покращує історію до досягнення якості.",
    sub_agents=[story_writer],
    max_iterations=MAX_ITERATIONS,
)
