from vda.models.project_plan import ProjectPlan
from vda.parsers import ProjectPlanParser


class DirectorAgent:

    def __init__(self):
        self.parser = ProjectPlanParser()

    def create_plan(
        self,
        request: str,
    ) -> ProjectPlan:
        data = {
            "title": "黑洞纪录片",
            "topic": request,
            "duration": 60,
            "style": "Documentary",
            "audience": "General",
            "scenes": [
                {
                    "title": "什么是黑洞",
                    "goal": "解释黑洞的基本概念",
                    "duration": 15,
                    "media_type": "image",
                },
                {
                    "title": "事件视界",
                    "goal": "解释事件视界和强大引力",
                    "duration": 15,
                    "media_type": "video",
                },
                {
                    "title": "吸积盘",
                    "goal": "展示吸积盘的形成与发光现象",
                    "duration": 15,
                    "media_type": "image",
                },
                {
                    "title": "霍金辐射",
                    "goal": "介绍霍金辐射理论",
                    "duration": 15,
                    "media_type": "video",
                },
            ],
        }

        return self.parser.parse(data)
