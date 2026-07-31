from vda.managers.plugin_manager import PluginManager


plugins = PluginManager()

plugins.register(
    "mock",
    {
        "name": "Mock Provider",
        "version": "0.1.0",
    },
)

print()

print("Registered Plugins")

print("------------------")

for name, plugin in plugins.all().items():
    print(name, "->", plugin)
