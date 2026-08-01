from vda.models.project_plan import (
    MediaType,
    ProjectPlan,
    ScenePlan,
)


class ProjectPlanParser:

    def parse(
        self,
        data: dict,
    ) -> ProjectPlan:

        plan = ProjectPlan(
            title=data["title"],
            topic=data["topic"],
            duration=data["duration"],
            style=data["style"],
            audience=data["audience"],
        )

        for index, scene in enumerate(
            data["scenes"],
            start=1,
        ):
            plan.scenes.append(
                ScenePlan(
                    id=index,
                    title=scene["title"],
                    goal=scene["goal"],
                    duration=scene["duration"],
                    media_type=MediaType(
                        scene["media_type"]
                    ),
                )
            )

        return plan
