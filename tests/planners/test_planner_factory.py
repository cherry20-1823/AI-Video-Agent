from vda.config.settings import Settings
from vda.factories.planner_factory import PlannerFactory
from vda.planners.base import BaseProjectPlanner
from vda.planners.mock_project_planner import MockProjectPlanner


def test_mock_project_planner_implements_base_interface():
    planner = MockProjectPlanner()

    assert isinstance(planner, BaseProjectPlanner)


def test_planner_factory_returns_mock_planner():
    factory = PlannerFactory(
        Settings()
    )

    planner = factory.planner()

    assert isinstance(planner, MockProjectPlanner)
