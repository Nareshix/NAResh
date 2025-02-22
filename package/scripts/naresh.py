import click
from package.createBinary import createBinary
from package.removeBinary import removeBinary



ALIAS = {
    "vscodium": "codium"
}


@click.argument('app')
@click.command()
def install(app):
    if app in ALIAS:
        app = ALIAS[app]
    createBinary(app)


@click.argument('app')
@click.command()
def remove(app):
    if app in ALIAS:
        app = ALIAS[app]
    removeBinary(app)

@click.command()
def update():
    pass

@click.command()
def ls():
    pass

@click.command()
def search():
    pass

@click.command()
def show():
    pass


@click.group()
def cli():
    pass

cli.add_command(install)
cli.add_command(remove)

if __name__ == '__main__':
    cli()

