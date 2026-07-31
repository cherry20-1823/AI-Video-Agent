from typing import Any


class PluginManager:

    def __init__(self):
        self._plugins: dict[str, Any] = {}

    def register(
        self,
        name: str,
        plugin: Any,
    ):
        self._plugins[name] = plugin

    def get(
        self,
        name: str,
    ):
        return self._plugins.get(name)

    def all(self):
        return self._plugins

    def exists(
        self,
        name: str,
    ):
        return name in self._plugins
