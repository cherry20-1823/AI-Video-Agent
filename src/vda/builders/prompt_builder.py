from vda.models.scene import Scene


class PromptBuilder:

    def build(self, scene: Scene) -> str:

        prompt = f"""
Create a cinematic video.

Scene Title:
{scene.title}

Narration:
{scene.narration}

Style:
Ultra realistic.
Cinematic.
8K.
Volumetric lighting.
Smooth camera movement.
Highly detailed.
"""

        return prompt.strip()
