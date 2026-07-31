from vda.builders.prompt_builder import PromptBuilder
from vda.llm.base import BaseLLM
from vda.services.dispatcher import Dispatcher
from vda.services.planner import Planner


class Orchestrator:

    def __init__(
        self,
        dispatcher: Dispatcher,
        llm: BaseLLM,
    ):
        self.dispatcher = dispatcher
        self.planner = Planner(llm)
        self.prompt_builder = PromptBuilder()

    def run(self, topic: str):

        print("=================================")
        print(" Video Director Agent")
        print("=================================")

        project = self.planner.create_project(topic)

        provider = self.dispatcher.select_provider()

        provider.login()

        for scene in project.scenes:

            print()
            print(f"Scene {scene.id}: {scene.title}")

            prompt = self.prompt_builder.build(scene)

            print()
            print("Prompt:")
            print(prompt)

            task = provider.generate(
    prompt=prompt,
    duration=scene.duration,
    aspect_ratio=project.aspect_ratio,
)

            provider.download(task)

        provider.logout()

        print()
        print("Project Finished")

        return project
