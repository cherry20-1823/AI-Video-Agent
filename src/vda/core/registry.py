class Registry:

    def __init__(self):
        self._providers = {}

    def register(self, provider):
        self._providers[provider.name] = provider

    def get(self, name):
        return self._providers.get(name)

    def all(self):
        return self._providers

    def exists(self, name):
        return name in self._providers
