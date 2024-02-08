import sys, pathlib

import click

from . import read_srda_docx


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=pathlib.Path))
@click.option(
    "-o",
    "--output",
    default=None,
    help="Output dir or file name",
    type=click.Path(path_type=pathlib.Path),
)
def docx_to_json(input_file, output=None):
    """
    Convert an SRDA docx file to a json file
    """

    if output.is_dir():
        outfile = output / input_file.with_suffix(".json").name
    elif output is None:
        outfile = input_file.with_suffix(".json")
    else:
        outfile = output

    click.echo(f"Converting {input_file} to {outfile}")

    try:
        parsed_data = read_srda_docx(input_file)
        outfile.open("w+").write(parsed_data.to_json())
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    docx_to_json()