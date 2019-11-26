import click
from sweepstats.cli import pass_context


@click.command('compute', short_help='Initializes a repo.')
@click.option('--gen-map', type=click.Path(exists=True, file_okay=True,
                                        resolve_path=True),
              help='Changes the folder to operate on.')
@click.argument('vcf_file', required=True, type=click.Path(resolve_path=True))
@click.argument('ancestral_file', required=True, type=click.Path(resolve_path=True))
@pass_context
def cli(ctx, vcf_file):
    """Initializes a repository."""
    ctx.log('Initialized the repository in %s',
            click.format_filename(path))
    
