# -*- coding: utf-8 -*-
"""Tests for cli."""
from typer.testing import CliRunner

from serious_scaffold.cli import app

runner = CliRunner()


def test_app():
    """Test for cli."""
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert result.output.strip() == "Hello World."