from vda.core.registry import Registry
from vda.providers.mock.provider import MockProvider
from vda.services.dispatcher import Dispatcher


registry = Registry()

registry.register(MockProvider())

dispatcher = Dispatcher(registry)

provider = dispatcher.select_provider()

print()

print("Selected Provider")

print("-----------------")

print(provider.name)
