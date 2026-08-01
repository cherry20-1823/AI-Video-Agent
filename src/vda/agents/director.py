from vda.models.project_plan import (
    MediaType,
    ProjectPlan,
    ScenePlan,
)


class DirectorAgent:
    def create_plan(
        self,
        request: str,
    ) -> ProjectPlan:
        return ProjectPlan(
            title="黑洞纪录片",
            topic=request,
            duration=60,
            style="Documentary",
            audience="General",
            scenes=[
                ScenePlan(
                    id=1,
                    title="什么是黑洞",
                    goal="解释黑洞的基本概念",
                    duration=15,
                    media_type=MediaType.IMAGE,
                ),
                ScenePlan(
                    id=2,
                    title="事件视界",
                    goal="解释事件视界和强大引力",
                    duration=15,
                    media_type=MediaType.VIDEO,
                ),
                ScenePlan(
                    id=3,
                    title="吸积盘",
                    goal="展示吸积盘的形成与发光现象",
                    duration=15,
                    media_type=MediaType.IMAGE,
                ),
                ScenePlan(
                    id=4,
                    title="霍金辐射",
                    goal="介绍霍金辐射理论",
                    duration=15,
                    media_type=MediaType.VIDEO,
                ),
            ],
        )
