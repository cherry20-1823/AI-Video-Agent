from abc import ABC, abstractmethod


class BaseVideoProvider(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def generate(
        self,
        prompt: str,
        duration: int,
        aspect_ratio: str,
    ):
        pass

    @abstractmethod
    def query(self, task):
        pass

    @abstractmethod
    def download(self, task):
        pass

    @abstractmethod
    def logout(self):
        pass
