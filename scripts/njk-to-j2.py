#!/usr/bin/env python3

"""
Run njk_to_j2 against the a tree of Nunjucks templates.
"""

from govuk_frontend_jinja.templates import njk_to_j2

from argparse import ArgumentParser
from pathlib import Path
from typing import Iterable, Tuple, Optional


def iter_njk_templates(path: Path, root: Optional[Path] = None) -> Iterable[Tuple[Path, str]]:
    if root is None:
        root = path.resolve()
    if path.is_dir():
        for child in path.iterdir():
            yield from iter_njk_templates(child, root=root)
    elif path.is_file():
        if path.suffix == ".njk":
            f = path.resolve().relative_to(root)
            yield f, path.read_text()


def print_templates(templates: Iterable[Tuple[Path, str]]):
    for path, template in templates:
        print(f"+++ {path}")
        print(template)


def save_templates(templates: Iterable[Tuple[Path, str]], output_path: Optional[Path] = None):
    for path, template in templates:
        if output_path:
            path = output_path / path
        path.write_text(template)


def main(argv=None):
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("input", metavar="DIR", default=".",
                        help="path to directories containing .njk files")
    parser.add_argument("-o", "--output", nargs="?", const=True,
                        help="save output")
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    if args.output:
        if args.output is True:
            output_path = input_path
        else:
            output_path = Path(args.output)

    pipeline = iter_njk_templates(input_path)
    pipeline = ((path, njk_to_j2(template)) for path, template in pipeline)
    if args.output:
        save_templates(pipeline, output_path=output_path)
    else:
        print_templates(pipeline)


if __name__ == "__main__":
    main()
