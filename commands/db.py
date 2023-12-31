import click
import subprocess


@click.group()
def db():
    """Manage database"""


@db.command()
def migrate():
    """Updates your database schema to match your models."""
    subprocess.run(["python", "project/manage.py", "migrate"], check=True)


@db.command()
def superuser():
    """Create a superuser account with administrative privileges."""
    try:
        subprocess.run(
            [
                "python",
                "project/manage.py",
                "createsuperuser",
                "--no-input",
            ],
            check=True,
        )
    except:
        pass
