"""Measure you FPGA circuit!"""

from .version import VERSION

__version__ = VERSION

from .main import _main


def start():
    """Entry point!"""
    _main()
