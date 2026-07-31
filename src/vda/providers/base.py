from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def login(self):
        ...

    @abstractmethod
    def generate(self, scene):
        ...

    @abstractmethod
    def query(self, task):
        ...

    @abstractmethod
    def download(self, task):
        ...

    @abstractmethod
    def logout(self):
        ...
