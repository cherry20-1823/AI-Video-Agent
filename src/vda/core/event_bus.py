from collections import defaultdict
from typing import Any, Callable


class EventBus:

    def __init__(self):
        self._handlers = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        handler: Callable[[Any], None],
    ):
        self._handlers[event_name].append(handler)

    def publish(
        self,
        event_name: str,
        data=None,
    ):
        for handler in self._handlers[event_name]:
            handler(data)
