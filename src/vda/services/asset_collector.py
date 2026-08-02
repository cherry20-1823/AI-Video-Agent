from pathlib import Path

from vda.models.asset import (
    Asset,
)
from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.enums import (
    AssetType,
)


class AssetCollector:

    def collect_video(
        self,
        files: list[Path],
    ) -> AssetRegistry:

        registry = AssetRegistry()

        for index, file in enumerate(files):

            registry.add(
                Asset(
                    id=f"video:scene-{index + 1:03d}",
                    name=file.name,
                    type=AssetType.VIDEO,
                    path=file,
                )
            )

        return registry
