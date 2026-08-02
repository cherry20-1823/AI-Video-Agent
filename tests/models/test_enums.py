from vda.models.enums import (
    GenerationMode,
)


def test_generation_mode_values():
    assert (
        GenerationMode.IMAGE.value
        == "IMAGE"
    )

    assert (
        GenerationMode.VIDEO.value
        == "VIDEO"
    )
