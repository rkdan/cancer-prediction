import sys

import toml
import typer
from streamlit.web import cli as stcli

app = typer.Typer()


@app.command()
def version():
    # get version of app
    pyproject = toml.load("pyproject.toml")
    typer.echo(pyproject["tool"]["poetry"]["version"])


@app.command()
def run():
    sys.argv = ["streamlit", "run", "cancer_prediction/streamlit_app.py"]
    sys.exit(stcli.main())


if __name__ == "__main__":
    app()
