from abc import ABC, abstractmethod

from vda.models.timeline import Timeline


class BaseRenderer(ABC):

    @abstractmethod
    def render(
        self,
        timeline: Timeline,
        output_path: str,
    ) -> str:
        pass
