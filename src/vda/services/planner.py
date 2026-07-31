from vda.llm.base import BaseLLM
from vda.models.project import Project
from vda.models.scene import Scene


class Planner:

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def create_project(self, topic: str) -> Project:

        data = self.llm.generate_plan(topic)

        project = Project(
            id="project-001",
            title=data["title"],
            description=topic,
            duration=data["duration"],
            aspect_ratio="16:9",
        )

        for index, item in enumerate(data["scenes"], start=1):
            project.scenes.append(
                Scene(
                    id=index,
                    title=item["title"],
                    narration=item["narration"],
                    duration=item["duration"],
                )
            )

        return project
