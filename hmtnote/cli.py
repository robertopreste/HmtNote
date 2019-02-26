#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click


@click.command()
def main(args=None):
    """Console script for hmtnote."""
    click.echo("Replace this message by putting your code into "
               "hmtnote.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
