import time

from vda.providers.base import BaseProvider


class MockProvider(BaseProvider):

    @property
    def name(self):
        return "mock"

    def login(self):
        print("Login Mock")

    def generate(self, scene):
        print(f"Generating: {scene.title}")
        time.sleep(2)
        return {
            "task_id": "mock-task-001",
            "status": "completed",
        }

    def query(self, task):
        return {
            "status": "completed",
        }

    def download(self, task):
        print("Download Fake Video")

    def logout(self):
        print("Logout Mock")
