from vda.models.project import Project
from vda.models.scene import Scene
from vda.services.dispatcher import Dispatcher


class Orchestrator:

    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher

    def run(self):

        print("=================================")
        print(" Video Director Agent")
        print("=================================")

        project = Project(
            id="project-001",
            title="Black Hole",
            description="Introduction",
            duration=60,
            aspect_ratio="16:9",
        )

        scene = Scene(
            id=1,
            title="Black Hole",
            narration="A black hole in deep space.",
            duration=5,
        )

        project.scenes.append(scene)

        provider = self.dispatcher.select_provider()

        provider.login()

        task = provider.generate(scene)

        provider.download(task)

        provider.logout()

        print()
        print("Project Finished")

        return project
