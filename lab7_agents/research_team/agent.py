from google.adk.agents.llm_agent import Agent
from google.adk.agents.parallel_agent import ParallelAgent

# Три незалежних дослідники — виконуються паралельно
ai_researcher = Agent(
    model='gemini-2.5-flash',
    name='ai_researcher',
    description="Досліджує тренди у штучному інтелекті.",
    instruction="""
    Ти дослідник у сфері AI. Надай короткий огляд останніх трендів
    у штучному інтелекті (3-5 пунктів). Відповідай українською мовою.
    """,
)

web_researcher = Agent(
    model='gemini-2.5-flash',
    name='web_researcher',
    description="Досліджує тренди у веб-розробці.",
    instruction="""
    Ти дослідник у сфері веб-розробки. Надай короткий огляд останніх
    трендів у веб-технологіях (3-5 пунктів). Відповідай українською мовою.
    """,
)

mobile_researcher = Agent(
    model='gemini-2.5-flash',
    name='mobile_researcher',
    description="Досліджує тренди у мобільній розробці.",
    instruction="""
    Ти дослідник у сфері мобільних технологій. Надай короткий огляд
    останніх трендів у мобільній розробці (3-5 пунктів).
    Відповідай українською мовою.
    """,
)

# Aggregator — збирає результати всіх досліджень
aggregator = Agent(
    model='gemini-2.5-flash',
    name='aggregator',
    description="Обʼєднує результати всіх досліджень.",
    instruction="""
    Ти аналітик. Обʼєднай результати трьох досліджень в один
    структурований звіт з висновками. Відповідай українською мовою.
    """,
)

# Parallel агент — запускає дослідників одночасно
root_agent = ParallelAgent(
    name='research_team',
    description="Паралельне дослідження трьох технологічних напрямків.",
    sub_agents=[ai_researcher, web_researcher, mobile_researcher],
)
