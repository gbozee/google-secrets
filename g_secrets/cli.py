import click
import os


@click.command()
def create_secrets():
    click.echo(os.path.abspath("cli.py"))


if __name__ == "__main__":
    create_secrets()
