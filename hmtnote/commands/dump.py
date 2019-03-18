#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
from hmtnote.classes import DataDumper


@click.command()
def dump():
    """
    Dump required databases for offline annotation.
    """
    dumper = DataDumper()
    click.echo("Downloading data...")
    dumper.download_data()
    click.echo("Complete.")

    return 0

