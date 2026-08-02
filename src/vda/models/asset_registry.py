from dataclasses import dataclass, field

from vda.models.asset import Asset
from vda.models.enums import AssetType


@dataclass(slots=True)
class AssetRegistry:
    assets: list[Asset] = field(default_factory=list)

    def add(
        self,
        asset: Asset,
    ) -> None:
        self.assets.append(asset)

    def get(
        self,
        asset_id: str,
    ) -> Asset | None:
        for asset in self.assets:
            if asset.id == asset_id:
                return asset

        return None

    def exists(
        self,
        asset_id: str,
    ) -> bool:
        return self.get(asset_id) is not None

    def remove(
        self,
        asset_id: str,
    ) -> bool:
        asset = self.get(asset_id)

        if asset is None:
            return False

        self.assets.remove(asset)
        return True

    def by_type(
        self,
        asset_type: AssetType,
    ) -> list[Asset]:
        return [
            asset
            for asset in self.assets
            if asset.type == asset_type
        ]

    def all(
        self,
    ) -> list[Asset]:
        return list(self.assets)
