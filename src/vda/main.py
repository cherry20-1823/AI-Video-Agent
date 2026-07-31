from vda.config.settings import load_settings
from vda.core.orchestrator import Orchestrator
from vda.core.registry import Registry
from vda.factories import ProviderFactory
from vda.llm.factory import create_llm
from vda.services.dispatcher import Dispatcher

settings = load_settings()

factory = ProviderFactory(settings)

registry = Registry()
registry.register(
    factory.video_provider(),
)

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
