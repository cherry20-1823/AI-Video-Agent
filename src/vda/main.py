from vda.core.registry import Registry
from vda.providers.mock.provider import MockProvider


registry = Registry()

registry.register(MockProvider())

print()

print("Registered Providers")

print("--------------------")

for name, provider in registry.all().items():
    print(name)
