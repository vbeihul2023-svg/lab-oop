from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent

# Крок 1 — генерація коду
code_writer = Agent(
    model='gemini-2.5-flash',
    name='code_writer',
    description="Пише Python код за запитом.",
    instruction="""
    Ти Python розробник. Напиши чистий робочий код за запитом користувача.
    Збережи результат у змінну 'generated_code' в контексті.
    Відповідай лише кодом без пояснень.
    """,
)

# Крок 2 — рев'ю коду
code_reviewer = Agent(
    model='gemini-2.5-flash',
    name='code_reviewer',
    description="Робить рев'ю коду та знаходить помилки.",
    instruction="""
    Ти досвідчений code reviewer. Перевір код з попереднього кроку.
    Вкажи що добре і що можна покращити.
    Відповідай українською мовою.
    """,
)

# Крок 3 — рефакторинг
code_refactorer = Agent(
    model='gemini-2.5-flash',
    name='code_refactorer',
    description="Покращує та рефакторить код.",
    instruction="""
    Ти експерт з рефакторингу. На основі рев'ю покращ код.
    Додай docstrings, типізацію та виправ зауваження.
    Відповідай українською мовою та покажи фінальний код.
    """,
)

# Sequential агент — виконує кроки по порядку
root_agent = SequentialAgent(
    name='code_pipeline',
    description="Pipeline: написання → рев'ю → рефакторинг коду.",
    sub_agents=[code_writer, code_reviewer, code_refactorer],
)
