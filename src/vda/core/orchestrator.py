from vda.builders.prompt_builder import PromptBuilder
from vda.llm.base import BaseLLM
from vda.providers.image.base import BaseImageProvider
from vda.services.dispatcher import Dispatcher
from vda.services.planner import Planner
from vda.storage.workspace import Workspace


class Orchestrator:
    def __init__(
        self,
        dispatcher: Dispatcher,
        llm: BaseLLM,
        image_provider: BaseImageProvider,
    ):
        self.dispatcher = dispatcher
        self.planner = Planner(llm)
        self.prompt_builder = PromptBuilder()
        self.workspace = Workspace()
        self.image_provider = image_provider

    def run(
        self,
        topic: str,
    ):
        print("=================================")
        print(" Video Director Agent")
        print("=================================")

        project = self.planner.create_project(
            topic
        )

        self.workspace.create_project(
            project
        )

        video_provider = (
            self.dispatcher.select_provider()
        )

        video_provider.login()

        for scene in project.scenes:
            print()
            print(
                f"Scene {scene.id}: {scene.title}"
            )

            prompt = self.prompt_builder.build(
                scene
            )

            prompt_file = (
                self.workspace.save_prompt(
                    project=project,
                    scene=scene,
                    prompt=prompt,
                )
            )

            scene_dir = (
                self.workspace.create_scene(
                    project=project,
                    scene=scene,
                )
            )

            image_file = (
                scene_dir / "image.png"
            )

            print()
            print(
                f"Saved Prompt: {prompt_file}"
            )

            image_task = (
                self.image_provider.generate(
                    prompt=prompt,
                    output_path=str(
                        image_file
                    ),
                )
            )

            print()
            print("Image Task")
            print("----------")
            print(image_task)

            video_task = (
                video_provider.generate(
                    prompt=prompt,
                    duration=scene.duration,
                    aspect_ratio=(
                        project.aspect_ratio
                    ),
                )
            )

            video_provider.download(
                video_task
            )

        video_provider.logout()

        print()
        print("Project Finished")

        return project
