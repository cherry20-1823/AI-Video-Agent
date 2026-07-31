from vda.services.dispatcher import Dispatcher
from vda.services.planner import Planner


class Orchestrator:

    def __init__(
        self,
        dispatcher: Dispatcher,
    ):
        self.dispatcher = dispatcher
        self.planner = Planner()

    def run(
        self,
        topic: str,
    ):

        print("=================================")
        print(" Video Director Agent")
        print("=================================")

        project = self.planner.create_project(topic)

        provider = self.dispatcher.select_provider()

        provider.login()

        for scene in project.scenes:

            print()

            print(f"Scene {scene.id}: {scene.title}")

            task = provider.generate(scene)

            provider.download(task)

        provider.logout()

        print()

        print("Project Finished")

        return project
