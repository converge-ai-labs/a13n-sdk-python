from importlib.metadata import version

import converge_foundation_sdk


def test_package_version_matches_distribution() -> None:
    assert converge_foundation_sdk.__version__ == version("converge-foundation-sdk")
