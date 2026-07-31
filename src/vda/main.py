from vda.core.event_bus import EventBus


bus = EventBus()


def on_project_created(project):

    print()

    print("EVENT -> Project Created")

    print(project)


bus.subscribe(
    "project.created",
    on_project_created,
)

bus.publish(
    "project.created",
    {
        "title": "Black Hole",
        "duration": 60,
    },
)
