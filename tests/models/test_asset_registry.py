from pathlib import Path

from vda.models.asset import Asset
from vda.models.asset_registry import AssetRegistry
from vda.models.enums import AssetType


def test_asset_registry_adds_asset():
    registry = AssetRegistry()

    asset = Asset(
        id="image-001",
        name="Scene 1 image",
        type=AssetType.IMAGE,
        path=Path("scene-001/image.png"),
    )

    registry.add(asset)

    assert registry.assets == [asset]


def test_asset_registry_filters_assets_by_type():
    registry = AssetRegistry()

    image_asset = Asset(
        id="image-001",
        name="Scene 1 image",
        type=AssetType.IMAGE,
        path=Path("scene-001/image.png"),
    )

    prompt_asset = Asset(
        id="prompt-001",
        name="Scene 1 prompt",
        type=AssetType.PROMPT,
        path=Path("scene-001/prompt.txt"),
    )

    registry.add(image_asset)
    registry.add(prompt_asset)

    assert registry.by_type(
        AssetType.IMAGE
    ) == [
        image_asset
    ]

    assert registry.by_type(
        AssetType.PROMPT
    ) == [
        prompt_asset
    ]

    assert registry.by_type(
        AssetType.VIDEO
    ) == []


def test_asset_registry_gets_asset_by_id():
    registry = AssetRegistry()

    asset = Asset(
        id="image-001",
        name="Scene 1 image",
        type=AssetType.IMAGE,
        path=Path("scene-001/image.png"),
    )

    registry.add(asset)

    assert registry.get("image-001") is asset
    assert registry.get("missing") is None


def test_asset_registry_checks_asset_exists():
    registry = AssetRegistry()

    asset = Asset(
        id="prompt-001",
        name="Scene 1 prompt",
        type=AssetType.PROMPT,
        path=Path("scene-001/prompt.txt"),
    )

    registry.add(asset)

    assert registry.exists("prompt-001") is True
    assert registry.exists("missing") is False


def test_asset_registry_removes_asset():
    registry = AssetRegistry()

    asset = Asset(
        id="image-001",
        name="Scene 1 image",
        type=AssetType.IMAGE,
        path=Path("scene-001/image.png"),
    )

    registry.add(asset)

    assert registry.remove("image-001") is True
    assert registry.exists("image-001") is False
    assert registry.remove("image-001") is False


def test_asset_registry_all_returns_copy():
    registry = AssetRegistry()

    asset = Asset(
        id="image-001",
        name="Scene 1 image",
        type=AssetType.IMAGE,
        path=Path("scene-001/image.png"),
    )

    registry.add(asset)

    assets = registry.all()
    assets.clear()

    assert registry.assets == [asset]
