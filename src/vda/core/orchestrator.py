from vda.builders.prompt_builder import PromptBuilder
from vda.llm.base import BaseLLM
from vda.providers.image.mock.provider import MockImageProvider
from vda.services.dispatcher import Dispatcher
from vda.services.planner import Planner
from vda.storage.workspace import Workspace


class Orchestrator:

    def __init__(
        self,
        dispatcher: Dispatcher,
        llm: BaseLLM,
    ):
        self.dispatcher = dispatcher
        self.planner = Planner(llm)
        self.prompt_builder = PromptBuilder()
        self.workspace = Workspace()
        self.image_provider = MockImageProvider()

    def run(self, topic: str):

        print("=================================")
        print(" Video Director Agent")
        print("=================================")

        project = self.planner.create_project(topic)

        self.workspace.create_project(project)

        provider = self.dispatcher.select_provider()

        provider.login()

        for scene in project.scenes:

            print()
            print(f"Scene {scene.id}: {scene.title}")

            prompt = self.prompt_builder.build(scene)

            prompt_file = self.workspace.save_prompt(
                project=project,
                scene=scene,
                prompt=prompt,
            )

            scene_dir = self.workspace.create_scene(
                project=project,
                scene=scene,
            )

            image_file = scene_dir / "image.txt"

            print()
            print("Prompt:")
            print(prompt)

            print()
            print(f"Saved Prompt: {prompt_file}")

            image_task = self.image_provider.generate(
                prompt=prompt,
                output_path=str(image_file),
            )

            print()
            print("Image Task")
            print("----------")
            print(image_task)

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
