"""A template extension module for Python."""

import logging

from template_extension_module import _version
from template_extension_module._core import hello_from_bin

__version__ = _version.__version__

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main() -> None:
    """Log a message from the binary extension module."""
    logging.info(hello_from_bin())


__all__ = ["__version__", "main"]
