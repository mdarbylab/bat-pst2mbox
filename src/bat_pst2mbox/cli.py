import argparse
import sys

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bat-pst2mbox",
        description="Convert a PST file to one mbox per folder, for import into The Bat!.",
    )
    parser.add_argument("--version", action="version", version=__version__)
    return parser


def main(argv: list[str] | None = None) -> int:
    build_parser().parse_args(argv)
    print("bat-pst2mbox: conversion is not implemented yet.", file=sys.stderr)
    return 2
