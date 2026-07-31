from vda.models.project import Project
from vda.models.scene import Scene


class Planner:

    def create_project(
        self,
        topic: str,
    ) -> Project:

        project = Project(
            id="project-001",
            title=topic,
            description=f"Video about {topic}",
            duration=60,
            aspect_ratio="16:9",
        )

        scenes = [
            ("什么是黑洞", "介绍黑洞是什么"),
            ("事件视界", "解释事件视界"),
            ("吸积盘", "介绍吸积盘"),
            ("霍金辐射", "介绍霍金辐射"),
        ]

        for index, (title, narration) in enumerate(scenes, start=1):
            project.scenes.append(
                Scene(
                    id=index,
                    title=title,
                    narration=narration,
                    duration=15,
                )
            )

        return project
