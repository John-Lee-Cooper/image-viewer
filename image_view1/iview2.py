#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
iview cli
"""

from typing import List
from pathlib import Path
import typer
import util
import iview


def main(paths: List[Path]):  # = typer.Option(..., prompt="Image path")):
    """
    {app} - a digital photo viewer

    \b
    {app} displays the image specified by PATHS.
    PATHS is a list of image paths or a directory containing images.

    {app} allows you to step forward or backward though all the images
    and/or image directories specified in the arguments.

    \b
    Press
      <SPACE>     to go to the next image.
      <BACKSPACE> to go to the previous image.
      <DELETE>    to delete the current image.
      <ESCAPE>    to exit.
    """

    iview.App(paths)


if __name__ == "__main__":
    util.update_docstring(main, app=Path(__file__).name)
    typer.run(main)
