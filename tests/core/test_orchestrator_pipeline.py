from vda.core.orchestrator import (
    Orchestrator,
)
from vda.core.registry import Registry
from vda.llm.mock.provider import (
    MockLLM,
)
from vda.providers.image.mock.provider import (
    MockImageProvider,
)
from vda.providers.video.mock.provider import (
    MockVideoProvider,
)
from vda.services.dispatcher import (
    Dispatcher,
)


class RegistryMockVideoProvider(
    MockVideoProvider
):

    @property
    def name(self):
        return "mock"



def test_orchestrator_runs_full_pipeline():

    registry = Registry()

    registry.register(
        RegistryMockVideoProvider(),
    )

    orchestrator = Orchestrator(
        dispatcher=Dispatcher(
            registry
        ),
        llm=MockLLM(),
        image_provider=MockImageProvider(),
    )

    result = orchestrator.run(
        "AI future city"
    )

    assert result is not None
