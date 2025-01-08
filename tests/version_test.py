"""Test the version of the package."""

import template_extension_module


def test_version() -> None:
    """Test that the version is correct."""
    assert template_extension_module.__version__ == "0.1.0"
