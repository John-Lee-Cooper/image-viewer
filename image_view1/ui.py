#!/usr/bin/env python

"""
Provide functions to write info, warning and error messages to the console.
"""


import sys

try:  # Trying to find module on sys.path
    from click import secho
    import config

    CLICK_INSTALLED = True
except ModuleNotFoundError:
    CLICK_INSTALLED = False
    print("import click failed")


def error(message: str, exit_code: int = 1) -> None:
    """ Notify user of a fatal error and exit with error_code """
    if CLICK_INSTALLED:
        secho(message, **config.ERROR_STYLE)
    else:
        print(message)
    sys.exit(exit_code)


def warning(message: str) -> None:
    """ Notify user something has gone wrong """
    if CLICK_INSTALLED:
        secho(message, **config.WARNING_STYLE)
    else:
        print(message)


def info(message: str) -> None:
    """ Notify user message"""
    if CLICK_INSTALLED:
        secho(message, **config.INFO_STYLE)
    else:
        print(message)


if __name__ == "__main__":
    info("info")
    warning("warning")
    error("error")
