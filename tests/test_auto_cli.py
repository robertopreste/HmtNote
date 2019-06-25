#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from click.testing import CliRunner
from hmtnote import cli


def test_cli():
    """Test the main CLI command."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "Show the version and exit." in result.output
    assert "Show this message and exit." in result.output


def test_cli_help():
    """Test the CLI help (same as invoking without arguments and options)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["--help"])
    assert result.exit_code == 0
    assert "Show the version and exit." in result.output
    assert "Show this message and exit." in result.output
