from vda.models.project import Project
from vda.models.scene import Scene


project = Project(
    id="demo",
    title="Black Hole",
    description="Introduction",
    duration=60,
    aspect_ratio="16:9",
)

scene = Scene(
    id=1,
    title="Scene 1",
    narration="A black hole in deep space.",
    duration=6,
)

project.scenes.append(scene)

print(project)
