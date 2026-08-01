from vda.agents import DirectorAgent


def main():
    request = input(
        "请输入视频需求："
    ).strip()

    if not request:
        print("视频需求不能为空。")
        return

    plan = DirectorAgent().create_plan(
        request
    )

    print()
    print("Project Plan")
    print("============")
    print(f"Title    : {plan.title}")
    print(f"Duration : {plan.duration}s")
    print(f"Style    : {plan.style}")
    print(f"Audience : {plan.audience}")
    print()

    for scene in plan.scenes:
        print(
            f"Scene {scene.id}: "
            f"{scene.title}"
        )
        print(
            f"  Type     : "
            f"{scene.media_type.value}"
        )
        print(
            f"  Duration : "
            f"{scene.duration}s"
        )
        print(
            f"  Goal     : "
            f"{scene.goal}"
        )
        print()


if __name__ == "__main__":
    main()
