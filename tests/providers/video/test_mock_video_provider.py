from pathlib import Path

from vda.providers.video.mock.provider import (
    MockVideoProvider,
)


def test_mock_video_provider_generates_file(
    tmp_path,
):
    output = tmp_path / "video.mp4"

    provider = MockVideoProvider()

    result = provider.generate(
        prompt="hello",
        output_path=str(output),
    )

    assert output.exists()

    assert (
        output.read_text(
            encoding="utf-8"
        )
        == "mock video"
    )

    assert result.provider == "mock-video"

    assert Path(result.local_file) == output
