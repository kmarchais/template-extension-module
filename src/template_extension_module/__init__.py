"""A template extension module for Python."""

import logging

from template_extension_module._core import hello_from_bin
from template_extension_module._version import __version__

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Log a message from the binary extension module."""
    logger.info(hello_from_bin())


__all__ = ["__version__", "main"]
