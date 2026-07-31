from vda.llm.base import BaseLLM


class MockLLM(BaseLLM):

    def generate_plan(self, topic: str) -> dict:

        return {
            "title": topic,
            "duration": 60,
            "scenes": [
                {
                    "title": "什么是黑洞",
                    "narration": "介绍黑洞是什么",
                    "duration": 15,
                },
                {
                    "title": "事件视界",
                    "narration": "解释事件视界",
                    "duration": 15,
                },
                {
                    "title": "吸积盘",
                    "narration": "介绍吸积盘",
                    "duration": 15,
                },
                {
                    "title": "霍金辐射",
                    "narration": "介绍霍金辐射",
                    "duration": 15,
                },
            ],
        }
