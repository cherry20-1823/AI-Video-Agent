from vda.models.project_plan import ProjectPlan, ScenePlan


class ScenePromptBuilder:

    def build(
        self,
        project: ProjectPlan,
        scene: ScenePlan,
    ) -> str:
        media_instruction = (
            "Create a cinematic still image."
            if scene.media_type.value == "image"
            else "Create a cinematic video shot."
        )

        prompt = f"""
{media_instruction}

Project:
{project.title}

Topic:
{project.topic}

Scene Title:
{scene.title}

Scene Goal:
{scene.goal}

Project Style:
{project.style}

Target Audience:
{project.audience}

Duration:
{scene.duration} seconds

Visual Direction:
Ultra realistic.
Cinematic composition.
Highly detailed.
Professional documentary lighting.
Strong visual storytelling.
No text, captions, logos, or watermarks.
"""

        return prompt.strip()
