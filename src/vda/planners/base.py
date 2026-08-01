from abc import ABC, abstractmethod


class BaseProjectPlanner(ABC):

    @abstractmethod
    def plan(
        self,
        request: str,
    ) -> dict:
        """Return a ProjectPlan-compatible dictionary."""
        raise NotImplementedError
