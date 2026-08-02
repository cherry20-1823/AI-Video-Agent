import pytest

from vda.providers.video.base import (
    BaseVideoProvider,
)


def test_base_video_provider_is_abstract():
    with pytest.raises(TypeError):
        BaseVideoProvider()
