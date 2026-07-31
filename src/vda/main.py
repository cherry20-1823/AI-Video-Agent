from vda.core.orchestrator import Orchestrator
from vda.core.registry import Registry
from vda.llm.factory import create_llm
from vda.providers.mock.provider import MockProvider
from vda.services.dispatcher import Dispatcher

registry = Registry()
registry.register(MockProvider())

dispatcher = Dispatcher(registry)

llm = create_llm("mock")

agent = Orchestrator(
    dispatcher=dispatcher,
    llm=llm,
)

project = agent.run(
    topic="黑洞",
)

print()

print("Project:")
print(project.title)

print()

print("Scenes:")

for scene in project.scenes:
    print(f"{scene.id}. {scene.title}")
