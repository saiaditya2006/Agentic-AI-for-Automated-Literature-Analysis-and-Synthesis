from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import CodeInterpreterTool
from pathlib import Path

code_tool = CodeInterpreterTool()

@CrewBase
class SemanticScholarCrew():
    """SemanticScholarCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def semantic_scholar_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['semantic_scholar_agent'], 
            verbose=True,
            tools = [code_tool],
            output_file = "sem.json"
        )
    
    @agent
    def dataset_agent(self) -> Agent:
        return Agent(config=self.agents_config['dataset_agent'], verbose=True)
    
    @agent
    def intro_scope_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['intro_scope_agent'],
            verbose=True
        )

    @agent
    def methods_results_agent(self) -> Agent:
        return Agent(config=self.agents_config['methods_results_agent'], verbose=True)

    @agent
    def challenges_gaps_future_agent(self) -> Agent:
        return Agent(config=self.agents_config['challenges_gaps_future_agent'], verbose=True)

    @agent
    def conclusion_references_agent(self) -> Agent:
        return Agent(config=self.agents_config['conclusion_references_agent'], verbose=True)

    @agent
    def merger_agent(self) -> Agent:
        return Agent(config=self.agents_config['merger_agent'], verbose=True)

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], 
        )

    @task
    def intro_scope_task(self) -> Task:
        return Task(config=self.tasks_config['intro_scope_task'])

    @task
    def dataset_task(self) -> Task:
        return Task(config=self.tasks_config['dataset_task'])

    @task
    def methods_results_task(self) -> Task:
        return Task(config=self.tasks_config['methods_results_task'])

    @task
    def challenges_gaps_future_task(self) -> Task:
        return Task(config=self.tasks_config['challenges_gaps_future_task'])

    @task
    def conclusion_references_task(self) -> Task:
        return Task(config=self.tasks_config['conclusion_references_task'])

    @task
    def merge_task(self) -> Task:
        return Task(config=self.tasks_config['merge_task'])
    
    @crew
    def crew(self) -> Crew:
        """Creates the SemanticScholarCrew crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


#test
interest = "EEG-Based Schizophrenia Detection using Machine Learning"
guidelines_path = Path("/Users/saiadityapediredla/Downloads/Draft_1/semantic_scholar_crew/src/semantic_scholar_crew/semantic_scholar_guidelines.md")
guidelines_text = guidelines_path.read_text(encoding="utf-8")

num_papers = 30

crew = SemanticScholarCrew()

result = (SemanticScholarCrew().crew().kickoff(
    inputs={"guidelines": guidelines_text, 
    "interest": interest, 
    "num_papers": num_papers}))


print(result)

final_text = result.raw if hasattr(result, "raw") else str(result)

# Save to file
final_md_path = "outputs/final_survey.md"
with open(final_md_path, "w", encoding="utf-8") as f:
    f.write(final_text)

print(f"\n✅ Final survey saved to {final_md_path}")



