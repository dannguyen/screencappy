from click.testing import CliRunner
import pytest
import re

from screencappy.cli import main as maincli




def test_main_cli():
    """by default, OUTPUT_PATH is required"""
    result = CliRunner().invoke(maincli)
    assert result.exit_code == 2
    assert '[OPTIONS] OUTPUT_PATH' in result.output

    # test help invocation
    helpr = CliRunner().invoke(maincli, ["--help"])
    assert helpr.exit_code == 0

    assert re.search(r"--help +Show this message and exit", helpr.output)
