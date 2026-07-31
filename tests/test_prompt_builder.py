from vda.builders.prompt_builder import PromptBuilder
from vda.models.scene import Scene


def test_prompt_builder_contains_scene_information():
    scene = Scene(
        id=1,
        title="Black Hole",
        narration="A black hole in deep space.",
        duration=5,
    )

    prompt = PromptBuilder().build(scene)

    assert "Black Hole" in prompt
    assert "A black hole in deep space." in prompt
    assert "Cinematic" in prompt
