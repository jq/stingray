#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stingray` package."""

import pytest

from click.testing import CliRunner

from stingray import stingray
from stingray import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

# if you hit unit test error in python3, check https://stackoverflow.com/questions/36651680/click-will-abort-further-execution-because-python-3-was-configured-to-use-ascii
def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'stingray.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
