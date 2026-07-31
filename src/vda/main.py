from vda.models.scene import Scene
from vda.providers.mock.provider import MockProvider


provider = MockProvider()

provider.login()

scene = Scene(
    id=1,
    title="Black Hole",
    narration="A black hole in deep space.",
    duration=5,
)

task = provider.generate(scene)

print(task)

provider.download(task)

provider.logout()
