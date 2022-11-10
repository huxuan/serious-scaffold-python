# -*- coding: utf-8 -*-
"""Command Line Interface."""
import typer

app = typer.Typer()


@app.command()
def hello(name: str = "World"):
    """Hello command."""
    print(f"Hello {name}.")


typer_click_object = typer.main.get_command(app)


if __name__ == "__main__":
    app()  # pragma: no cover
