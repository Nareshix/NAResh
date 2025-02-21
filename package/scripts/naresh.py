import click
from package.createBinary import createBinary

@click.argument('app')
@click.command()
def install(app):
    createBinary(app)
    

@click.command()
def remove():
    pass

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

if __name__ == '__main__':
    cli()

