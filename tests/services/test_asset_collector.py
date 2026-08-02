from pathlib import Path

from vda.models.enums import (
    AssetType,
)
from vda.services.asset_collector import (
    AssetCollector,
)


def test_asset_collector_registers_video():

    registry = AssetCollector().collect_video(
        [
            Path("scene-001/video.mp4"),
            Path("scene-002/video.mp4"),
        ]
    )

    assets = registry.by_type(
        AssetType.VIDEO
    )

    assert len(assets) == 2

    assert assets[0].id == (
        "video:scene-001"
    )

    assert str(
        assets[0].path
    ) == "scene-001/video.mp4"
