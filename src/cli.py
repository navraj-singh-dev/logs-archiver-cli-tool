import click
from .archiver import LogArchiver
from .config import Config


@click.group()
def cli():
    """Log Archive Tool - Manage and archive log files"""
    pass


@cli.command()
@click.option(
    "--source",
    "-s",
    default=Config.get_source_dir(),
    help="Source directory containing logs",
)
@click.option(
    "--dest",
    "-d",
    default=Config.get_archive_dir(),
    help="Destination directory for saving archives",
)
def archive(source, dest):
    """Create a new archive of log files"""
    archiver = LogArchiver(source, dest)
    archive_path = archiver.create_archive()
    click.echo(f"Archive created: {archive_path}")


@cli.command()
@click.option(
    "--archive-dir",
    "-d",
    default=Config.get_archive_dir(),
    help="Directory containing your saved archives",
)
def list(archive_dir):
    """List all available archives"""
    archiver = LogArchiver("", archive_dir)
    archives = archiver.list_archives()
    if archives:
        click.echo("Available archives:")
        for archive in archives:
            click.echo(f"  - {archive}")
    else:
        click.echo("No archives found")


@cli.command()
@click.argument("archive_name")
@click.option("--extract-path", "-p", help="Path to extract the archive")
@click.option(
    "--archive-dir",
    "-d",
    default=Config.get_archive_dir(),
    help="Directory containing archives",
)
def extract(archive_name, extract_path, archive_dir):
    """Extract a specific archive"""
    archiver = LogArchiver("", archive_dir)
    archiver.extract_archive(archive_name, extract_path)
    click.echo(f"Archive extracted successfully")


if __name__ == "__main__":
    cli()
