#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
from hmtnote.classes import DataDumper


@click.command()
@click.option("--basic", "-b", is_flag=True, default=False,
              help="""Dump the basic database (default: False)""")
@click.option("--crossref", "-c", is_flag=True, default=False,
              help="""Dump the crossref database (default: False)""")
@click.option("--variab", "-v", is_flag=True, default=False,
              help="""Dump the variab database (default: False)""")
@click.option("--predict", "-p", is_flag=True, default=False,
              help="""Dump the predict database (default: False)""")
def dump(basic, crossref, variab, predict):
    """
    Dump required databases for offline annotation.

    If neither --basic, --crossref, --variab nor --predict are
    provided, they will all default to True, and all the available datasets
    will be downloaded for offline use.
    """
    if not basic and not crossref and not variab and not predict:
        basic, crossref, variab, predict = True, True, True, True

    dumper = DataDumper(basic, crossref, variab, predict)
    click.echo("Downloading data...")
    dumper.download_data()
    click.echo("Complete.")

    return 0

