from vda.models.context import PipelineContext


class PipelineRunner:

    def __init__(
        self,
        steps: list,
    ):
        self.steps = steps

    def run(
        self,
        context: PipelineContext,
    ) -> PipelineContext:

        for step in self.steps:
            context = step.execute(
                context
            )

        return context
