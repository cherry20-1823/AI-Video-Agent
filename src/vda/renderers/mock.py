from vda.models.timeline import Timeline
from vda.renderers.base import BaseRenderer


class MockRenderer(BaseRenderer):

    def render(
        self,
        timeline: Timeline,
        output_path: str,
    ) -> str:
        return output_path
