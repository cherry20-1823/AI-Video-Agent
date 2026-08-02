from vda.builders.prompt_builder import PromptBuilder
from vda.llm.base import BaseLLM
from vda.models.asset_registry import AssetRegistry
from vda.models.context import (
    PipelineContext,
)
from vda.providers.image.base import BaseImageProvider
from vda.renderers.ffmpeg import (
    FFmpegRenderer,
)
from vda.services.composer import (
    Composer,
)
from vda.services.dispatcher import Dispatcher
from vda.services.planner import Planner
from vda.services.timeline_builder import TimelineBuilder
from vda.services.video_generator import (
    VideoGenerator,
)
from vda.storage.workspace import Workspace
from vda.workflow.render_workflow import (
    RenderWorkflow,
)


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
        self.asset_registry = AssetRegistry()
        self.timeline_builder = TimelineBuilder()

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

        context = PipelineContext(
            project=project,
            workspace=self.workspace,
            asset_registry=self.asset_registry,
        )

        self.render_workflow = RenderWorkflow(
            context,
            Composer(
                renderer=FFmpegRenderer(
                    self.asset_registry
                )
            ),
        )

        self.video_generator = VideoGenerator(
            video_provider=video_provider,
            context=context,
        )

        context = PipelineContext(
            project=project,
            workspace=self.workspace,
            asset_registry=self.asset_registry,
        )

        self.render_workflow = RenderWorkflow(
            context,
            Composer(
                renderer=FFmpegRenderer(
                    self.asset_registry
                )
            ),
        )

        self.video_generator = VideoGenerator(
            video_provider=video_provider,
            context=context,
        )
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

            self.video_generator.generate(
                project_id=project.id,
                scene_id=scene.id,
                prompt=prompt,
            )

        context.timeline = self.timeline_builder.build(
            context.asset_registry
        )

        render_result = self.render_workflow.run(
            task_id=project.id,
            timeline=context.timeline,
            output_path="final.mp4",
        )
        print()
        print("Project Finished")

        return render_result
