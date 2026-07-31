from vda.core.orchestrator import Orchestrator
from vda.core.registry import Registry
from vda.providers.mock.provider import MockProvider
from vda.services.dispatcher import Dispatcher


registry = Registry()

registry.register(MockProvider())

dispatcher = Dispatcher(registry)

agent = Orchestrator(dispatcher)

project = agent.run()

print()

print(project)
