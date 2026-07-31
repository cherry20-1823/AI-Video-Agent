from vda.models.task_result import TaskResult
from vda.providers.base import BaseProvider


class MockProvider(BaseProvider):

    @property
    def name(self):
        return "mock"

    def login(self):
        print("Login Mock")

    def generate(
        self,
        prompt: str,
        duration: int,
        aspect_ratio: str,
    ):

        print("Generating Video")
        print("----------------")
        print(prompt)

        print()
        print(f"Duration : {duration}s")
        print(f"Aspect   : {aspect_ratio}")

        return TaskResult(
            task_id="mock-task-001",
            provider="mock",
            status="completed",
            progress=100,
        )

    def query(self, task):
        return task

    def download(self, task: TaskResult):

        print()

        print("Task")

        print("----")

        print(task)

        print()

        print("Download Fake Video")

    def logout(self):
        print("Logout Mock")
