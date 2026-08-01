from openai import OpenAI

from vda.agents.director import DirectorAgent
from vda.builders.scene_prompt_builder import ScenePromptBuilder
from vda.config.settings import load_settings
from vda.openai.responses import OpenAIResponses
from vda.planners.openai_project_planner import OpenAIProjectPlanner
from vda.providers.image.openai.provider import OpenAIImageProvider
from vda.services.storyboard_generator import StoryboardGenerator
from vda.storage.workspace import Workspace


def main():

    settings = load_settings()

    print("\nGenerating project...")
    print("---------------------")

    planner = OpenAIProjectPlanner(
        responses=OpenAIResponses(
            api_key=settings.openai_api_key,
            model=settings.openai_text_model,
        )
    )

    director = DirectorAgent(
        planner=planner,
    )

    project = director.create_plan(
        "做一个45秒关于人工智能未来的科技纪录片"
    )

    print("✓ Project created")

    client = OpenAI(
        api_key=settings.openai_api_key,
    )

    image_provider = OpenAIImageProvider(
        client=client,
        model=settings.openai_image_model,
    )

    generator = StoryboardGenerator(
        prompt_builder=ScenePromptBuilder(),
        image_provider=image_provider,
        workspace=Workspace(),
    )

    print("\nGenerating all storyboards...")
    print("-----------------------------")

    results = generator.generate_all(
        project=project,
        project_id="project-001",
    )

    print()
    print(
        f"Generated {len(results)} storyboard image(s)."
    )

    for result in results:
        print(f"✓ {result.local_file}")

    print()
    print("Done.")


if __name__ == "__main__":
    main()
