from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.task_result import (
    TaskResult,
)
from vda.services.timeline_builder import (
    TimelineBuilder,
)
from vda.workflow.render_workflow import (
    RenderWorkflow,
)


class VideoPipeline:

    def __init__(
        self,
        timeline_builder: TimelineBuilder,
        render_workflow: RenderWorkflow,
    ):
        self.timeline_builder = (
            timeline_builder
        )

        self.render_workflow = (
            render_workflow
        )

    def run(
        self,
        task_id: str,
        registry: AssetRegistry,
        output_path: str,
    ) -> TaskResult:

        timeline = (
            self.timeline_builder.build(
                registry
            )
        )

        return (
            self.render_workflow.run(
                task_id,
                timeline,
                output_path,
            )
        )
