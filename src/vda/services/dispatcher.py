from vda.core.registry import Registry


class Dispatcher:

    def __init__(self, registry: Registry):
        self.registry = registry

    def select_provider(self):
        provider = self.registry.get("mock")

        if provider is None:
            raise RuntimeError("No provider registered.")

        return provider
